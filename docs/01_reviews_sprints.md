***Sprint -1 Review:***
Este sprint fue dedicado a construir una visión clara de la identidad del proyecto antes de escribir una sola línea de código. Se plantearon preguntas relacionadas a qué hace el proyecto, que busca optimizar, a quién va dirigido, cuales son sus restricciones y las tecnologías utilizadas. Comprendí la necesidad de este tipo de análisis para desarrollar una suerte de mapa que me acompañe durante todas las etapas del proyecto, permitiendo alinear las decisiones de desarrollo con el objetivo primigenio del aplicativo.

***Sprint 0 Review:***
Durante este sprint me encontré con varios desafíos a resolver debido a mi poca experiencia en la preparación de proyectos utilizando Python y VS Code. Fue necesario investigar y comprender conceptos fundamentales como la creación de entornos virtuales, la configuración de políticas de ejecución de PowerShell, la creación y sincronización de proyectos locales y remotos en Git y GitHub y la organización inicial del proyecto.
Como resultado, el proyecto está en sólidas condiciones con respecto a su estructura y su configuración, preparado para iniciar el desarrollo.

***Sprint 1 Review***
Se realizó la primera prueba del programa de punto a punto mediante la inclusión de un proceso de lectura y extracción de datos para un único proveedor con un formato determinado. 
Luego de las correcciones pertinentes, el programa realiza todos los objetivos planificados:
- Lectura de PDF
- Detección automática del proveedor
- Extracción de datos
- Filtrado de datos
- Exportación a formato Excel
La problemática principal erradicó en cómo resolver la lectura del documento y la extracción de los datos pertinentes. Ambas cuestiones se resolvieron primero integrando una clase encargada de las acciones a realizar sobre el PDF (lectura) y luego, dentro del extractor correspondiente, desarrollando expresiones regulares que permitan extraer los datos buscados.
Para el próximo sprint se buscará ampliar el número de proveedores para realizar extracciones sobre distintos documentos y adaptar cada proceso al formato de los mismos.

***Sprint 2 Review***
Fue agregado un nuevo proveedor con un formato de lista de precio diferente. Se realizó la modificación del código de extracción para el mismo, actualizando e incorporando expresiones regulares más robustas con el fin de evitar errores en la obtención de datos. 
Posteriormente, se desarrolló la extracción dinámica de proveedores existentes dentro de la clase RegistryExtractor a partir de los módulos pertenecientes al paquete 'providers'. Está funcionalidad es clave ya que nos desliga de la idea de registrar nuevos proveedores cada vez que sea necesario agregar uno nuevo.
Las dificultades principales erradicaron en como utilizar las librerías pkgutil, importlib e inspect para realizar el recorrido por el paquete providers, identificar sus modulos y dentro de los mismos sus clases, para, a partir de ahí, agregarlas al registro de proveedores.
Para el próximo Sprint se cargará una cantidad mayor de proveedores, adaptando los códigos de extracción de cada uno, con el fin de cubrir la demanda de extracción de costos existente.
