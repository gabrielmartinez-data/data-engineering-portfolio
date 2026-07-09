-- ====================================================================
-- PROYECTO: BANCO DOMINICANA (SISTEMAS FINANCIEROS Y AUDITORÍA)
-- OBJETIVO: Consolidar Módulos 1 al 4 mediante análisis transaccional.
-- FECHA: Julio 2026
-- ====================================================================

-- ====================================================================
-- FASE 1: ARQUITECTURA DE DATOS (DDL E INSERCIÓN)
-- ====================================================================

-- 1. Catálogo de Cuentas de Clientes (Tabla Maestra)
CREATE TABLE IF NOT EXISTS cuentas (
    id_cuenta INTEGER PRIMARY KEY AUTOINCREMENT,
    titular TEXT,
    tipo_cuenta TEXT
);

-- 2. Histórico de Transacciones en Vivo (Tabla de Hechos)
CREATE TABLE IF NOT EXISTS transacciones (
    id_transaccion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cuenta INTEGER,
    tipo_movimiento TEXT, -- 'Deposito' o 'Retiro'
    monto REAL,
    canal_digital TEXT,    -- Puede venir NULL si fue por cajero físico
    fecha_movimiento TEXT
);

-- 3. Inserción de registros de prueba con datos sucios/nulos
INSERT INTO cuentas (titular, tipo_cuenta) VALUES 
('Gabriel Martinez', 'Ahorros'),
('Starlin Roque', 'Corriente'),
('Consumidor Anonimo', 'Ahorros');

INSERT INTO transacciones (id_cuenta, tipo_movimiento, monto, canal_digital, fecha_movimiento) VALUES 
(1, 'Deposito', 50000.00, 'App Movil', '2026-07-01'),
(1, 'Retiro', 2500.00, 'App Movil', '2026-07-02'),
(2, 'Deposito', 15000.00, 'Web Banking', '2026-07-03'),
(1, 'Retiro', 2500.00, NULL, '2026-07-04'),        -- Empate de monto y canal NULL
(3, 'Deposito', 8500.00, 'App Movil', '2026-07-05');


-- ====================================================================
-- FASE 2: REPORTES ANALÍTICOS DE AUDITORÍA
-- ====================================================================

-- --------------------------------------------------------------------
-- REPORTE 1: Clasificación de Movimientos por Cliente (Ranking denso)
-- OBJETIVO: Evaluar el comportamiento de DENSE_RANK() ante montos empatados
--           y asegurar que el JOIN use las llaves relacionales correctas.
-- --------------------------------------------------------------------
SELECT 
    transacciones.id_transaccion,
    IFNULL(cuentas.titular, 'Consumidor Anonimo') AS titular_cuenta,
    transacciones.tipo_movimiento,
    transacciones.monto,
    IFNULL(transacciones.canal_digital, 'Cajero Fisico') AS canal_utilizado,
    -- DENSE_RANK(): Crea islas por cuenta y numera de mayor a menor sin dejar huecos
    DENSE_RANK() OVER (
        PARTITION BY transacciones.id_cuenta 
        ORDER BY transacciones.monto DESC
    ) AS ranking_movimiento_cuenta
FROM transacciones
LEFT JOIN cuentas
    ON transacciones.id_cuenta = cuentas.id_cuenta; -- Vinculación por ID de cuenta real


-- --------------------------------------------------------------------
-- REPORTE 2: Historial de Saldos Cronológicos (Flujo acumulado)
-- OBJETIVO: Calcular un 'Running Total' en la RAM ordenando por fecha
--           para ver la evolución de fondos por cada cliente en el tiempo.
-- --------------------------------------------------------------------
SELECT 
    transacciones.id_transaccion,
    IFNULL(cuentas.titular, 'Consumidor Anonimo') AS consumidor_final,
    transacciones.tipo_movimiento,
    transacciones.monto,
    IFNULL(transacciones.canal_digital, 'Cajero Fisico') AS canal_digital,
    transacciones.fecha_movimiento,
    -- SUM() OVER: Acumula el monto cronológicamente respetando la partición de la cuenta
    SUM(transacciones.monto) OVER (
        PARTITION BY transacciones.id_cuenta 
        ORDER BY transacciones.fecha_movimiento ASC
    ) AS flujo_acumulativo
FROM transacciones
LEFT JOIN cuentas
    ON transacciones.id_cuenta = cuentas.id_cuenta;