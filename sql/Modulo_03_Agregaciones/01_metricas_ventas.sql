-- ====================================================================
-- PROJECT: STORE DATA WAREHOUSE (CORE TABLES)
-- MODULE 01: RELATIONAL MECHANICS & COMPLEX UNIFICATIONS
-- ====================================================================

-- Limpiamos el entorno para evitar duplicados al sobreescribir
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
    fecha_orden TEXT NOT NULL
);

-- ====================================================================
-- INSERCIÓN DE DATOS DE CONTROL (ESCENARIO DE PRUEBA)
-- ====================================================================

INSERT INTO clientes (nombre_cliente, city) VALUES 
('Gabriel Martinez', 'Santo Domingo Oeste'),
('Starlin Roque', 'Santiago'),
('Merelin Garcia', 'Distrito Nacional'),
('Darling Javier', 'Santo Domingo Este');

INSERT INTO ordenes (id_cliente, producto, monto, fecha_orden) VALUES 
(1, 'Laptop Dell', 45000.00, '2026-06-20'),
(1, 'Mouse Logi', 1500.00, '2026-06-21'),
(2, 'Teclado Mecánico', 3500.00, '2026-06-22'),
(NULL, 'Monitor Generic (Orphan Order)', 8500.00, '2026-06-23');

SELECT 
    clientes.nombre_cliente,
    COUNT(ordenes.id_orden) AS numero_de_ordenes
FROM clientes
LEFT JOIN ordenes 
    ON clientes.id_cliente = ordenes.id_cliente
GROUP BY clientes.nombre_cliente;

SELECT 
    clientes.nombre_cliente,
    SUM(ordenes.monto) AS total_de_gastos
FROM clientes
LEFT JOIN ordenes 
    ON clientes.id_cliente = ordenes.id_cliente
GROUP BY clientes.nombre_cliente 
ORDER BY total_de_gastos DESC; -- <--- Ordenamos por el alias del dinero en reversa

SELECT 
    clientes.nombre_cliente,
    SUM(ordenes.monto) AS total_de_gastos
FROM clientes
LEFT JOIN ordenes 
    ON clientes.id_cliente = ordenes.id_cliente
WHERE ordenes.metodo_pago = 'efectivo' -- <-- Sin punto y coma y con comillas simples
GROUP BY clientes.nombre_cliente 
HAVING total_de_gastos > 50
ORDER BY total_de_gastos DESC; -- <-- El punto y coma va aquí, al cerrar todo