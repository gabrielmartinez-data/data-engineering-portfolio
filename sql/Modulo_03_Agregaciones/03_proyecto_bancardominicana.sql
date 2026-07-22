-- ====================================================================
-- PROYECTO: BANCO DOMINICANA (SISTEMAS FINANCIEROS Y AUDITORÍA)
-- OBJETIVO: Consolidar Módulos 1 al 4 (DDL, JOINs, Filtros y Ventanas)
-- FECHA: Julio 2026
-- ====================================================================

-- ====================================================================
-- FASE 1: ARQUITECTURA DE DATOS (DDL E INSERCIÓN BASE)
-- ====================================================================

-- 1. Catálogo de Cuentas de Clientes (Tabla Maestra)
DROP TABLE IF EXISTS transacciones;
DROP TABLE IF EXISTS cuentas;

CREATE TABLE cuentas (
    id_cuenta INTEGER PRIMARY KEY AUTOINCREMENT,
    titular TEXT,
    tipo_cuenta TEXT
);

-- 2. Histórico de Transacciones en Vivo (Tabla de Hechos)
CREATE TABLE transacciones (
    id_transaccion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cuenta INTEGER,
    tipo_movimiento TEXT, -- 'Deposito' o 'Retiro'
    monto REAL,
    canal_digital TEXT,    -- Puede venir NULL si fue por cajero físico
    fecha_movimiento TEXT
);

-- 3. Inserción de registros de prueba (Datos limpios)
INSERT INTO cuentas (titular, tipo_cuenta) VALUES 
('Gabriel Martinez', 'Ahorros'),
('Starlin Roque', 'Corriente'),
('Consumidor Anonimo', 'Ahorros');

INSERT INTO transacciones (id_cuenta, tipo_movimiento, monto, canal_digital, fecha_movimiento) VALUES 
(1, 'Deposito', 50000.00, 'App Movil', '2026-07-01'),
(1, 'Retiro', 2500.00, 'App Movil', '2026-07-02'),
(2, 'Deposito', 15000.00, 'Web Banking', '2026-07-03'),
(1, 'Retiro', 2500.00, NULL, '2026-07-04'),        
(3, 'Deposito', 8500.00, 'App Movil', '2026-07-05');


-- ====================================================================
-- FASE 2: REPORTES ANALÍTICOS DE AUDITORÍA
-- ====================================================================

-- --------------------------------------------------------------------
-- REPORTE 1: Clasificación de Movimientos por Cliente (Ranking denso)
-- --------------------------------------------------------------------
SELECT 
    transacciones.id_transaccion,
    IFNULL(cuentas.titular, 'Consumidor Anonimo') AS titular_cuenta,
    transacciones.tipo_movimiento,
    transacciones.monto,
    IFNULL(transacciones.canal_digital, 'Cajero Fisico') AS canal_utilizado,
    DENSE_RANK() OVER (
        PARTITION BY transacciones.id_cuenta 
        ORDER BY transacciones.monto DESC
    ) AS ranking_movimiento_cuenta
FROM transacciones
LEFT JOIN cuentas
    ON transacciones.id_cuenta = cuentas.id_cuenta;


-- --------------------------------------------------------------------
-- REPORTE 2: Historial de Saldos Cronológicos (Flujo acumulado)
-- --------------------------------------------------------------------
SELECT 
    transacciones.id_transaccion,
    IFNULL(cuentas.titular, 'Consumidor Anonimo') AS consumidor_final,
    transacciones.tipo_movimiento,
    transacciones.monto,
    IFNULL(transacciones.canal_digital, 'Cajero Fisico') AS canal_digital,
    transacciones.fecha_movimiento,
    SUM(transacciones.monto) OVER (
        PARTITION BY transacciones.id_cuenta 
        ORDER BY transacciones.fecha_movimiento ASC
    ) AS flujo_acumulativo
FROM transacciones
LEFT JOIN cuentas
    ON transacciones.id_cuenta = cuentas.id_cuenta;


-- --------------------------------------------------------------------
-- REPORTE 3: Alertas Globales de Prevención de Lavado (RANK sin partición)
-- --------------------------------------------------------------------
SELECT 
    transacciones.id_transaccion,
    cuentas.titular,
    transacciones.monto,
    IFNULL(transacciones.canal_digital, 'Canal Desconocido / Alerta') AS canal_digital,
    RANK() OVER (
        ORDER BY transacciones.monto DESC
    ) AS ranking_global_alertas
FROM transacciones
LEFT JOIN cuentas
    ON transacciones.id_cuenta = cuentas.id_cuenta
WHERE transacciones.monto >= 5000;


-- ====================================================================
-- FASE 3: MONITOREO DIARIO (TABLAS SUMARIZADAS Y CONTROL)
-- ====================================================================

-- 1. Estructura para guardar métricas consolidadas por día
DROP TABLE IF EXISTS sumario_cuentas_control;

CREATE TABLE sumario_cuentas_control (
    id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_proceso TEXT,
    total_cuentas_registradas INTEGER,
    total_monto_depositado REAL
);

-- 2. Carga automática de historial procesado
INSERT INTO sumario_cuentas_control (fecha_proceso, total_cuentas_registradas, total_monto_depositado) VALUES 
('2026-07-15', 3, 73500.00),
('2026-07-16', 4, 85000.00),
('2026-07-17', 5, 112000.00),
('2026-07-18', 5, 112000.00);

-- 3. Análisis de Crecimiento del Volumen de Depósitos (Running Total)
SELECT 
    fecha_proceso,
    total_monto_depositado,
    SUM(total_monto_depositado) OVER (
        ORDER BY fecha_proceso ASC
    ) AS gran_total_acumulado
FROM sumario_cuentas_control;

-- 4. Comparativa de Volúmenes: Día Actual vs Día Anterior (Uso de LAG)
SELECT 
    fecha_proceso,
    total_monto_depositado,
    LAG(total_monto_depositado) OVER (
        ORDER BY fecha_proceso ASC
    ) AS depositos_dia_anterior    
FROM sumario_cuentas_control;

-- 5. Proyección de Volúmenes Futuros: Día Actual vs Día Siguiente (Uso de LEAD)
SELECT 
    fecha_proceso,
    total_monto_depositado,
    LEAD(total_monto_depositado) OVER (
        ORDER BY fecha_proceso ASC
    ) AS proximo_monto_depositado
FROM sumario_cuentas_control;

SELECT 
    transacciones.id_transaccion,
    IFNULL(cuentas.titular, 'Consumidor Anónimo') AS titular_cuenta,
    transacciones.tipo_movimiento,
    transacciones.monto,
    IFNULL(transacciones.canal_digital, 'Cajero Físico / Ventanilla') AS canal_utilizado,
    -- Ventana 1: Acumulado por cliente (lleva PARTITION BY)
    SUM(transacciones.monto) OVER (
        PARTITION BY transacciones.id_cuenta 
        ORDER BY transacciones.fecha_movimiento ASC
    ) AS flujo_acumulado_cliente,
    -- Ventana 2: Ranking global de todo el banco (SIN PARTITION BY)
    RANK() OVER (
        ORDER BY transacciones.monto DESC
    ) AS ranking_global_banco
FROM transacciones
LEFT JOIN cuentas
    ON transacciones.id_cuenta = cuentas.id_cuenta
WHERE transacciones.monto >= 2500;