QA End-to-End Automation Framework - SauceDemo + AWS
Descripción del Proyecto
Este proyecto tiene como objetivo crear un framework de automatización de pruebas QA para una aplicación de ejemplo llamada SauceDemo, utilizando herramientas modernas como Playwright y Selenium. El framework está diseñado para ser flexible, escalable y capaz de ejecutarse de manera eficiente en entornos locales o en la nube (AWS).

Estructura del Proyecto
El proyecto está estructurado de la siguiente manera:

copy
download
cloudqa-plus/
│
├── tests/
│   ├── ui/
│   │   └── pages/
│   └── api/
│
├── reports/
├── pipeline/
├── dashboards/
├── alerts/
├── infra/
│
├── requirements.txt
├── .env
└── README.md
Dependencias
El proyecto usa un entorno virtual de Python para gestionar las dependencias. Asegúrate de crear y activar el entorno virtual antes de instalar las librerías necesarias.

Instalación del Entorno Virtual
Crear el entorno virtual:

copy
download
python -m venv venv
Activar el entorno virtual:

En Windows:
copy
download
venv\Scripts\activate
Actualizar pip:

copy
download
pip install --upgrade pip
Instalar Dependencias
Para instalar las librerías necesarias, ejecuta:

copy
download
pip install -r requirements.txt
Esto instalará las siguientes librerías esenciales para el proyecto:

pytest: Framework de pruebas.
selenium: Automatización de pruebas para interfaces web.
webdriver-manager: Gestión automática de controladores de navegador.
pytest-xdist: Ejecución paralela de pruebas.
pytest-html: Generación de informes en formato HTML.
pytest-mock: Herramienta para realizar pruebas controladas con mocks.
pytest-cov: Medición de la cobertura de pruebas.
playwright: Automación de navegadores modernos (Chromium, Firefox, WebKit).
Instalar Navegadores para Playwright
Después de instalar Playwright, necesitas instalar los navegadores compatibles (Chromium, Firefox, WebKit) con el siguiente comando:

copy
download
python -m playwright install
Estructura de Carpetas
La estructura de carpetas está organizada de la siguiente manera para facilitar el mantenimiento del proyecto:

tests/: Contiene las pruebas, separadas en subcarpetas como ui para pruebas de interfaz de usuario y api para pruebas de API.
reports/: Aquí se generarán los informes de las pruebas.
pipeline/: Archivos y configuraciones relacionadas con la integración continua (CI/CD).
dashboards/: Archivos y paneles relacionados con los informes y métricas de pruebas.
alerts/: Configuraciones para notificaciones y alertas durante las pruebas.
infra/: Archivos relacionados con la infraestructura (por ejemplo, configuración de AWS).