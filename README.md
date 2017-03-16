# ada_resco_api

## Instalación

Instalación desde cero...
Instalar python depende de tu sistema operativo, esta vez será para Linux:

1. 'sudo apt-get install python3' // Instalamos python3
2. 'sudo apt-get install python3 virtualenvwrapper' // Instalamos el ambiente virtual
3. 'mkvirtualenv venv -p python3' // Creamos un ambiente virtual "venv" para que sea solo python3
4. 'workon venv' // Seleccionamos el ambiente que acabam0os de crear
5. 'pip install django' // Instalamos Django en ese ambiente
6. 'pip install -r requerimientos.txt' // Instalamos los modulos que necesita el proyecto


## Iniciar el servicio

Para iniciar el servicio solo necesitas correr el servidor Django en el ambiente que has elegido

1. 'workon <venv>' // Seleccionamos el ambiente que has creado
2. 'py manage.py runserver' // Puede que py no funcione puedes usar 'python' o './' para ejecutar el manage.py
    Para este proyecto es importante mencionar que el puerto que utilizamos es 1338, por lo que debes ejecutar:
    'python manage.py runserver 1338' donde 1338 es el puerto de escucha del servidor.
