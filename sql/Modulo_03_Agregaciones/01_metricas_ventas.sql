-- ====================================================================
-- PROJECT: STORE DATA WAREHOUSE (CORE TABLES)
-- MODULE 03: AGGREGATIONS & METRICS ANALYSIS
-- FILE: 01_metricas_ventas.sql
-- DESCRIPTION: Desarrollo de consultas analíticas avanzadas utilizando 
--              GROUP BY, HAVING, e inmunización de valores NULL.
-- ====================================================================

-- Limpiamos el entorno para evitar duplicados al sobreescribir el script
DROP TABLE IF EXISTS ordenes;
DROP TABLE IF EXISTS clientes;

-- 1. Creación de la Tabla Maestra de Clientes
CREATE TABLE clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_cliente TEXT NOT NULL,
    ciudad TEXT NOT NULL
);

-- 2. Creación de la Tabla de Movimientos (Órdenes de Compra)
CREATE TABLE ordenes (
    id_orden INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER, -- Llave Foránea (conecta con clientes)
    producto TEXT NOT NULL,
    monto REAL NOT NULL,
    metodo_pago TEXT NOT NULL, -- Columna añadida para soportar los filtros analíticos
    fecha_orden TEXT NOT NULL
);

-- ====================================================================
-- INSERCIÓN DE DATOS DE CONTROL (ESCENARIO DE PRUEBA BLINDADO)
-- ====================================================================

-- Corrección: Se cambió 'city' por 'ciudad' para coincidir con la estructura de la tabla
INSERT INTO clientes (nombre_cliente, ciudad) VALUES 
('Gabriel Martinez', 'Santo Domingo Oeste'),
('Starlin Roque', 'Santiago'),
('Merelin Garcia', 'Distrito Nacional'),
('Darling Javier', 'Santo Domingo Este');

-- Inserción con el campo 'metodo_pago' incluido para evitar fallos de ejecución
INSERT INTO ordenes (id_cliente, producto, monto, metodo_pago, fecha_orden) VALUES 
(1, 'Laptop Dell', 45000.00, 'tarjeta', '2026-06-20'),
(1, 'Mouse Logi', 1500.00, 'efectivo', '2026-06-21'),
(2, 'Teclado Mecánico', 3500.00, 'efectivo', '2026-06-22'),
(NULL, 'Monitor Generic (Orphan Order)', 8500.00, 'transferencia', '2026-06-23');

-- ====================================================================
-- EVOLUCIÓN DE CONSULTAS ANALÍTICAS (DE BÁSICO A SENIOR)
-- ====================================================================

-- REPORTE 1: Conteo básico de registros por cliente usando LEFT JOIN
-- Nota: Sirve de base, pero hereda la debilidad de contar filas vacías si no se especifica la columna.
SELECT 
    clientes.nombre_cliente,
    COUNT(ordenes.id_orden) AS numero_de_ordenes
FROM clientes
LEFT JOIN ordenes 
    ON clientes.id_cliente = ordenes.id_cliente
GROUP BY clientes.nombre_cliente;

-- REPORTE 2: Suma acumulada de gastos ordenados de mayor a menor
-- Nota: Expone valores 'NULL' si el cliente no posee transacciones.
SELECT 
    clientes.nombre_cliente,
    SUM(ordenes.monto) AS total_de_gastos
FROM clientes
LEFT JOIN ordenes 
    ON clientes.id_cliente = ordenes.id_cliente
GROUP BY clientes.nombre_cliente 
ORDER BY total_de_gastos DESC;

-- REPORTE 3: Análisis Híbrido Avanzado (Filtro doble con WHERE y HAVING)
-- Lógica RAM: El WHERE filtra filas de efectivo antes de agrupar; el HAVING filtra totales > 50 después de agrupar.
SELECT 
    clientes.nombre_cliente,
    SUM(ordenes.monto) AS total_de_gastos
FROM clientes
LEFT JOIN ordenes 
    ON clientes.id_cliente = ordenes.id_cliente
WHERE ordenes.metodo_pago = 'efectivo' 
GROUP BY clientes.nombre_cliente 
HAVING total_de_gastos > 50
ORDER BY total_de_gastos DESC;

-- REPORTE MASTER: Inmunización completa contra NULL y métricas consolidadas (El Reporte Final de Producción)
-- Lógica: IFNULL fuerza a los clientes sin compras a mostrar un '0' estético. 
--         COUNT(columna) evita la trampa del conteo fantasma del LEFT JOIN.
SELECT 
    clientes.nombre_cliente,
    IFNULL(SUM(ordenes.monto), 0) AS total_de_gastos,
    COUNT(ordenes.id_orden) AS cantidad_de_ordenes
FROM clientes
LEFT JOIN ordenes 
    ON clientes.id_cliente = ordenes.id_cliente
GROUP BY clientes.nombre_cliente
ORDER BY total_de_gastos DESC;