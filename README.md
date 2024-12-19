# TechTrack

**TechTrack** es una solución para la administración de equipos y servicios en una red empresarial. La aplicación permite gestionar el inventario de equipos, así como configurar y monitorear servicios como SSH y SMB, proporcionando una interfaz de API documentada con Swagger.

---

## 🚀 Características

- **Gestión de Equipos**: Registra, edita y elimina equipos de la red.
- **Gestión de Servicios**: Configura y supervisa servicios como SSH y SMB.
- **API Documentada**: Documentación interactiva de la API utilizando Swagger (DRF Spectacular).
- **Base de Datos**: Conexión eficiente a PostgreSQL utilizando `asyncpg`.
- **Modularidad**: Separación clara en módulos (`equipment`, `services`) para una fácil escalabilidad.
- **Compatibilidad**: Diseñado para integrarse con redes empresariales de hasta 50 dispositivos o más.

---

## 📂 Estructura del Proyecto

TechTrack/ 
├── equipment/ # Módulo para gestión de equipos 
├── migrations/ # Migraciones de base de datos │ 
├── models.py # Modelos de base de datos para equipos │ 
├── serializers.py # Serializadores para la API │ 
├── views.py # Vistas para gestionar equipos │
└── urls.py # Rutas específicas del módulo │ 
├── services/ # Módulo para gestión de servicios (SSH, SMB) 
│ ├── migrations/ 
│ ├── models.py 
│ ├── serializers.py 
│ ├── views.py 
│ └── urls.py 
│ ├── tech_track/ # Configuración principal del proyecto 
│ ├── settings.py # Configuraciones generales y de la base de datos 
│ ├── urls.py # Rutas principales del proyecto 
│ └── wsgi.py # Configuración del servidor WSGI 
│ └── README.md # Documentación del proyecto

---

## 🛠️ Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/techtrack.git
cd techtrack

### 2. Crear y Activar un Entorno Virtual
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

### 3. Instalar Dependencias
pip install -r requirements.txt

### 4. Configurar la Base de Datos
Asegúrate de tener PostgreSQL instalado y crea una base de datos llamada pc-register. Actualiza las credenciales en settings.py si es necesario:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pc-register',
        'USER': 'postgres',
        'PASSWORD': 'tu-contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

### 5. Ejecutar Migraciones
python manage.py makemigrations
python manage.py migrate

### 6. Crear un Superusuario
python manage.py createsuperuser

### 7. Iniciar el Servidor
python manage.py runserver
Visita http://127.0.0.1:8000/ para acceder a la API y http://127.0.0.1:8000/schema/swagger-ui/ para ver la documentación interactiva.

## 📖 Uso de la API
Endpoints Principales

Equipos (/api/equipment/):
GET /: Lista todos los equipos.
POST /: Agrega un nuevo equipo.
PUT /<id>/: Actualiza un equipo existente.
DELETE /<id>/: Elimina un equipo.

Servicios (/api/services/):
GET /: Lista todos los servicios.
POST /: Agrega un nuevo servicio.
PUT /<id>/: Actualiza un servicio existente.
DELETE /<id>/: Elimina un servicio.

Consulta la documentación completa en Swagger para más detalles.

## 🧑‍💻 Tecnologías Utilizadas
Lenguaje: Python 3.10+
Framework: Django Rest Framework
Base de Datos: PostgreSQL
Backend: asyncpg como adaptador de base de datos
Documentación: Swagger (DRF Spectacular)
Herramientas: Docker (opcional para despliegue), Git

---

## 📝 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

---

## 📧 Contacto
Desarrollado por Elias Higuera Acosta.
Si tienes preguntas o sugerencias, no dudes en contactarme:
Email: eliashigueraacosta@gmail.com
GitHub: https://github.com/MrMoss12-cmd

