# Chat Project

## Configuración del proyecto

Para ejecutar este proyecto en tu entorno local, sigue los siguientes pasos:

### Pre-requisitos

- Python
- pip (gestor de paquetes de Python)
- Docker y Docker Compose (para ejecutar la base de datos PostgreSQL)

### Instalación

Primero, clona el repositorio en tu máquina local y cambia al directorio del proyecto.

```bash
git clone https://github.com/bry4/django_chat.git
cd django_chat
```

Instala las dependencias necesarias utilizando `pip`:

```bash
pip install -r requirements.txt
```

Comprueba la versión de Django para asegurarte de que está instalada correctamente:

```bash
python -m django --version
```

Levanta el servicio de PostgreSQL utilizando Docker Compose:

```bash
docker compose up -d
```

[En caso uses una BD postgres existente]
Debes configurar la conexion en prj_chat/settings.py con tus credenciales

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_chat',
        'USER': 'user_chat',
        'PASSWORD': 'password_chat',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Realiza las migraciones necesarias para preparar tu base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Crea el usuario administrador

Ejecuta el siguiente comando para crear el usuario, y sigue las instrucciones dadas:

```bash
python manage.py createsuperuser
```

### Ejecución del servidor de desarrollo

Para iniciar el servidor de desarrollo, ejecuta:

```bash
python manage.py runserver
```

Ahora podrás acceder a la aplicación de chat en:

Para administrar usuarios, ingresas con tu superuser y creas nuevos usuarios
`http://localhost:8000/admin`

Para ingresar al login y luego al chat
`http://localhost:8000/`

