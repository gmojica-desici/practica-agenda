# Practica agenda para contactos

Esta es la base para la practica de un CRUD de una agenda, apoyandonos de django.

## Antes de iniciar

Configure su entorno virtual para desarrollar

* Para Linux y OS X

```
python3 -m venv venv
```

* Si esta en Windows

```
python -m venv venv
```

Inicie su entorno virtual

* Para Linux y OS X

```
source venv/bin/activate
```

* Si esta en Windows

```
venv\Scripts\activate
```

Una vez iniciado su entorno virtual, ejecute el siguiente comando

```
python -m pip install --upgrade pip
```

Instale las dependecias necesarias para este proyecto

```
pip install -r requirements.txt
```

Inicie la base de datos

```
python manage.py migrate
```

Cree un super usuario

```
python manage.py createsuperuser
```

Inicie el servicio

```
python manage.py runserver
```

Para verificar que todo a iniciado correctamente, inicie su navegador y escriba la siguiente url

```
http://localhost:8000/admin
```

Si ve la siguiente pantalla de inicio de sesión, todo esta correcto.

![pantalla 1!](/static/img/pantallas/pantalla001.png "pantalla 1")

* Pruebe a iniciar sesión con las credenciales de superusuario que creo.

## ¿Qué es lo que debemos hacer?

Con la anterior configuración estamos listos para crear nuestro CRUD para la agenda de contactos.

En nuestro proyecto tenemos la app `agenda`, la cual cuenta con los modelos necesarios para que comience con el desarrollo de nuestro poyecto frontend.

Los modelos con los que cuenta esta app son:

* Contacto
* Dirección
* Telófono

Con los modelos anteriores se deberán realizar las siguientes actividades.

**Genere una pantalla de inicio**

![pantalla 2!](/static/img/pantallas/pantalla002.png "pantalla 2")

**Genere una pantalla para capturar la información básica de un contacto**

![pantalla 3!](/static/img/pantallas/pantalla003.png "pantalla 3")

**Cuando se guarde el contacto y si todos los datos son correctos, debe ir a la pantalla para editar la información del contacto y capturar la información adicional de este**

![pantalla 4!](/static/img/pantallas/pantalla004.png "pantalla 4")

**Pestaña para editar información de dirección**

![pantalla 5!](/static/img/pantallas/pantalla005.png "pantalla 5")

**Pestaña para editar información de teléfonos**

![pantalla 6!](/static/img/pantallas/pantalla006.png "pantalla 6")

**Los teléfonos deberan ser agregados en la misma pantalla**

![pantalla 7!](/static/img/pantallas/pantalla007.png "pantalla 7")

![pantalla 8!](/static/img/pantallas/pantalla008.png "pantalla 8")

El botón `Cancelar` debe cancelar el registro de ese teléfono.

**Si ya existen teléfonos, el texto del botón debe cambiar**

![pantalla 9!](/static/img/pantallas/pantalla009.png "pantalla 9")

El botón `Eliminar` debe eliminar el teléfono del contacto.

**La pantalla de inicio debe ser actualizada con una lista de los contactos que ya se guardaron**

![pantalla 10!](/static/img/pantallas/pantalla010.png "pantalla 10")

Tome en cuenta las acciones de `Editar` y `Eliminar` para cada contacto, las cuales deberán ser realizadas, es decir que el botón `Editar` debe mostrar la pantalla donde se edita la información del contacto y el botón `Eliminar` debe eliminar el contacto de la agenda.


