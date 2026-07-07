-- ====================================================================
-- PROJECT: STORE DATA WAREHOUSE (CORE TABLES)
-- MODULE 04: ADVANCED ANALYTICAL WINDOW FUNCTIONS
-- FILE: 02_funciones_ventanas.sql
-- DESCRIPTION: Implementación de funciones de ventana (Window Functions)
--              para el cálculo de totales acumulados y estados de cuenta.
-- ====================================================================

-- --------------------------------------------------------------------
-- REPORTE 1: Introducción a Ventanas y Preservación de Filas
-- OBJETIVO: Calcular el gran total por cliente manteniendo el detalle
--           de cada orden individual (sin colapsar los registros).
-- --------------------------------------------------------------------
SELECT
    ordenes.id_orden,
    ordenes.id_cliente,
    clientes.nombre_cliente,
    ordenes.producto,
    ordenes.monto,
    ordenes.fecha_orden,
    -- PARTITION BY: Divide mentalmente los datos en "islas" por cliente.
    -- ORDER BY ASC: Obliga al motor a calcular fila por fila cronológicamente,
    --               generando un total acumulado (Running Total) tipo banco.
    SUM(ordenes.monto) OVER(
        PARTITION BY ordenes.id_cliente
        ORDER BY ordenes.fecha_orden ASC
    ) AS gasto_total_cliente
FROM ordenes
LEFT JOIN clientes
    ON ordenes.id_cliente = clientes.id_cliente;


-- --------------------------------------------------------------------
-- REPORTE 2: Análisis de Comportamiento Híbrido (Nivel Producción)
-- OBJETIVO: Consolidar el historial de compras limpiando las órdenes 
--           huérfanas y manteniendo el tracking acumulado del dinero.
-- --------------------------------------------------------------------
SELECT
    ordenes.id_orden,
    -- IFNULL: Detecta valores vacíos en las órdenes sin registrar (NULL)
    --         y les asigna estéticamente la etiqueta 'Consumidor Final'.
    IFNULL(clientes.nombre_cliente, 'Consumidor Final') AS nombre_del_cliente,
    ordenes.producto,
    ordenes.monto,
    -- La ventana opera sobre el ID crudo asegurando la separación matemática,
    -- independientemente de la máscara estética aplicada arriba.
    SUM(ordenes.monto) OVER(
        PARTITION BY ordenes.id_cliente
        ORDER BY ordenes.fecha_orden ASC
    ) AS gasto_acumulado
FROM ordenes
LEFT JOIN clientes
    ON ordenes.id_cliente = clientes.id_cliente;

-- --------------------------------------------------------------------
-- REPORTE 3: Análisis de Competencia y Posicionamiento de Productos
-- OBJETIVO: Clasificar los productos más caros comprados por cada cliente
--           evaluando el comportamiento de empates en la memoria RAM.
-- --------------------------------------------------------------------
SELECT 
    ordenes.id_orden,
    IFNULL(clientes.nombre_cliente, 'Consumidor Final') AS nombre_de_cliente,
    ordenes.producto,
    ordenes.monto,
    -- RANK(): Asigna puestos dejando huecos si hay empates.
    -- Si hay dos productos en el puesto 2, el siguiente puesto saltará al 4.
    RANK() OVER (
        PARTITION BY ordenes.id_cliente 
        ORDER BY ordenes.monto DESC
    ) AS con_RANK,
    -- DENSE_RANK(): Asigna puestos continuos sin importar los empates.
    -- Aunque haya dos productos en el puesto 2, el siguiente puesto será el 3.
    DENSE_RANK() OVER (
        PARTITION BY ordenes.id_cliente 
        ORDER BY ordenes.monto DESC
    ) AS con_DENSE_RANK
FROM ordenes
LEFT JOIN clientes 
    ON ordenes.id_cliente = clientes.id_cliente;