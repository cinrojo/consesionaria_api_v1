Aquí tienes el README actualizado con todos los detalles adicionales que pediste:

```markdown
# Proyecto: efiConcesionaria

## Descripción
Este proyecto es una aplicación web integral diseñada para la gestión eficiente de una concesionaria de autos. La plataforma permite a los usuarios llevar a cabo diversas operaciones relacionadas con la administración de vehículos, incluyendo la creación, lectura, actualización y eliminación (CRUD) de autos, marcas, modelos, y clientes. Además, ofrece funcionalidades para gestionar categorías, comentarios de los usuarios y la relación con proveedores.

El sistema está construido para diferenciar entre usuarios con diferentes roles, como staff y clientes, proporcionando niveles de acceso adecuados según las necesidades de la concesionaria. Los usuarios con rol de staff pueden administrar los vehículos y acceder a funcionalidades avanzadas, mientras que los clientes pueden interactuar con la plataforma, dejando comentarios y visualizando la información de los autos disponibles.

Esta solución busca mejorar la eficiencia operativa de la concesionaria, facilitar la interacción con los clientes y asegurar un manejo organizado de toda la información relevante para el negocio.

## Tecnologías Utilizadas
- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Python, Django, Django REST Framework
- **Base de Datos**: MySQL
- **Control de Versiones**: Git

## Instalación
1. **Crea un entorno virtual para el proyecto (recomendado) y actívalo:**

   Para crear un entorno virtual con Python 3:
   ```bash
   python3 -m venv nombre_del_entorno
   ```

   **Activa el entorno virtual:**

   En Windows:
   ```bash
   nombre_del_entorno\Scripts\activate
   ```

   En macOS y Linux:
   ```bash
   source nombre_del_entorno/bin/activate
   ```

2. **Crea una nueva carpeta para clonar el repositorio:**
   ```bash
   mkdir nombre_de_la_carpeta
   ```

3. **Accede a la nueva carpeta:**
   ```bash
   cd nombre_de_la_carpeta
   ```

4. **Clona este repositorio en tu máquina local usando el siguiente comando:**
   ```bash
   https://github.com/cinrojo/consesionaria_api_v1.git
   ```

5. **Navega hasta el directorio del proyecto:**
   ```bash
   cd proyect_django
   ```

6. **Instala las dependencias del proyecto:**
   ```bash
   pip install -r requirements.txt
   ```

7. **Ejecuta las migraciones para crear las tablas en la base de datos:**
   ```bash
   python manage.py migrate
   ```

8. **Inicia el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

   Abre un navegador web y accede a [http://localhost:8000](http://localhost:8000) para comenzar a utilizar la aplicación.

## Funcionalidades

### Gestión de Categorías
- **Agregar Categorías:** Los usuarios pueden agregar nuevas categorías para organizar los productos.
- **Actualizar Categorías:** Los usuarios pueden modificar el nombre de las categorías existentes.
- **Eliminar Categorías:** Los usuarios pueden eliminar categorías que ya no sean necesarias.

### Gestión de Productos
- **Agregar Productos:** Los usuarios pueden agregar nuevos productos asociados a una categoría específica.
- **Actualizar Productos:** Los usuarios pueden modificar la información de los productos, como nombre, descripción, precio y stock.
- **Eliminar Productos:** Los usuarios pueden eliminar productos que ya no estén en venta o que sean obsoletos.
- **Visualizar Detalles de Producto:** Los usuarios pueden ver información detallada de cada producto, incluyendo su categoría y características.

## Endpoints de la API
## API Endpoints

### Cliente
- **GET** `/api_v1/clientes/`: Lista todos los clientes.
- **POST** `/api_v1/clientes/{user_id}/crear-cliente/`: Crea un nuevo cliente.
- {
    "telefono": "",
    "direccion": ""
}
- **GET** `/api_v1/clientes/{pk}/`: Obtiene detalles de un cliente específico.
- **PUT** `/api_v1/clientes/{pk}/`: Actualiza un cliente existente.
- {
    "telefono": "",
    "direccion": ""
}
- **DELETE** `/api_v1/clientes/{pk}/`: Elimina un cliente específico.
- **GET** `/api_v1/clientes/{user_id}/crear-cliente/`: Muestra detalles del usuario antes de crear un cliente.
- **POST** `/api_v1/clientes/{user_id}/crear-cliente/`: Crea un cliente para un usuario específico.

### Marca
- **GET** `/api_v1/marcas/`: Lista todas las marcas.
- **POST** `/api_v1/marcas/`: Crea una nueva marca.
- {
    "nombre": ""
}
- **GET** `/api_v1/marcas/{pk}/`: Obtiene detalles de una marca específica.
- **PUT** `/api_v1/marcas/{pk}/`: Actualiza una marca existente.
- {
    "nombre": ""
}
- **DELETE** `/api_v1/marcas/{pk}/`: Elimina una marca específica.
- **GET** `/api_v1/marcas/download-csv/`: Descarga un CSV con todas las marcas.
- **GET** `/api_v1/marcas/latest/`: Obtiene la última marca agregada.

### Usuario
- **GET** `/api_v1/usuarios/`: Lista todos los usuarios.
- **POST** `/api_v1/usuarios/`: Crea un nuevo usuario.
- {
    "username": "",
    "first_name": "",
    "last_name": "",
    "email": "",
    "is_active": false
}
- **GET** `/api_v1/usuarios/{pk}/`: Obtiene detalles de un usuario específico.
- **PUT** `/api_v1/usuarios/{pk}/`: Actualiza un usuario existente.
- {
    "username": "",
    "first_name": "",
    "last_name": "",
    "email": "",
    "is_active": false
}
- **DELETE** `/api_v1/usuarios/{pk}/`: Elimina un usuario específico.

### Auto
- **GET** `/api_v1/cars/`: Lista todos los autos.
- **POST** `/api_v1/cars/`: Crea un nuevo auto.
- {
    "categoria": {
        "nombre": ""
    },
    "precio": null,
    "imagen": null,
    "pais_fabricacion": "",
    "combustible": "",
    "descripcion": "",
    "active": false,
    "modelo": null
}
- **GET** `/api_v1/cars/{pk}/`: Obtiene detalles de un auto específico.
- **PUT** `/api_v1/cars/{pk}/`: Actualiza un auto existente.
- {
    "categoria": {
        "nombre": ""
    },
    "precio": null,
    "imagen": null,
    "pais_fabricacion": "",
    "combustible": "",
    "descripcion": "",
    "active": false,
    "modelo": null
}
- **DELETE** `/api_v1/cars/{pk}/`: Elimina un auto específico.
- **GET** `/api_v1/cars/{pk}/comentarios/`: Obtiene comentarios asociados a un auto.
- **DELETE** `/api_v1/cars/{pk}/comentarios/{comentario_id}/`: Elimina un comentario específico asociado a un auto.
- **GET** `/api_v1/cars/download-csv/`: Descarga un CSV con información de todos los autos.
- **GET** `/api_v1/cars/download-price-stock-csv/`: Descarga un CSV con el precio total de todos los autos.
- **GET** `/api_v1/cars/latest/`: Obtiene el último auto agregado.


## Usuario de Administrador
Para acceder como administrador, utiliza las siguientes credenciales:
- **Usuario**: `superuser`
- **Contraseña**: `1234`

## Autores ✒️
- Franco Emanuel Benitez - [@emanuel079](https://github.com/emanuel079)
- Cintia Gisele Rojo - [@cinrojo](https://github.com/cinrojo)
- Lautaro Palacios - [@Lautaro-Palacios](https://github.com/Lautaro-Palacios)
- Milton Storm- [@MiltonStorm](https://github.com/MiltonStorm)
