# Sistema de Automatizacion para Extraccion y Comparacion de Listas de Precios (Price Extractor)

***¿Que problema resuelve?***

Hoy el personal administrativo debe procesar manualmente las listas de precios enviadas por proveedores en formato PDF.
El proceso implica varias operaciones manuales tales como:
- Abrir el archivo
- Copiar las columnas de interes
- Pegarlas en un excel
- Corregir sintaxis
- Guardar archivo
Este proceso demanda tiempo y esta expuesto a errores operacionales.

***Objetivo***

Automatizar la extracción y comparación de listas de precios de diferentes proveedores con el fin de ganar tiempo operativo y optimizar los procesos administrativos.

***Objetivos específicos***

- Detectar automáticamente el proveedor
- Extraer información del archivo
- Exportar la información a Excel
- Comparar las listas
- Detectar aumentos
- Mantener historial

***Beneficios esperados***
- Reducción significativa del tiempo dedicado al procesamiento de listas
- Disminución de errores por carga manual
- Estandarización de la información proveniente de diferentes proveedores
- Comparación automática de listas de precios
- Mayor trazabilidad mediante el historial de listas procesadas
- Escalabilidad para incorporar nuevos proveedores
- Permite mantener actualizada la base de datos de costos, evitando productos con precios inadecuados

***Tecnologías***

- Python
- Pandas
- pdfplumber
- OpenPyXL
- CustomTkinter

***Alcance***

- Versión 1.0 (MVP)
Leer PDF
Extraer información
Generar Excel

- Versión 2.0
Comparador de listas

-Versión 3.0
Dashboard

***Restricciones***
-> No modifica archivos originales
-> No requiere conexión a internet
-> Compatible con Windows