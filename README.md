# 🏘️ MicroRed Social para Comunidad Local

Plataforma web desarrollada en Django para la gestión y comunicación vecinal. Permite conectar a vecinos de barrios o conjuntos residenciales, reemplazando la informalidad de los chats grupales con una estructura organizada.

## 📋 Integrantes
* **[Apaza Villanueva Rodrigo Antonio]**
* **[Choque Valencia Delma Fernanda]**
* **[Guarachi Mamani Cristhian Manuel]**
* **[Tinta López Grissel Noemi]**
* **[Yujra Paye Alejandro Andrés]**


## 🚀 Funcionalidades Principales
* **Gestión de Usuarios:** Registro, Login y Perfiles.
* **Grupos Temáticos:** Creación de grupos por barrio o actividad (Ej: "Seguridad", "Deportes").
* **Interacción:** Publicación de novedades y sistema de comentarios anidados.
* **Privacidad:** Sistema de membresía (Unirse/Salir) para visualizar contenido.
* **Moderación:** Herramientas para administradores (Expulsar miembros, eliminar posts/grupos).

## 🛠️ Tecnologías
* **Backend:** Python, Django 5.
* **Base de Datos:** MySQL (Conector PyMySQL).
* **Frontend:** HTML5, Bootstrap 5.

## ⚙️ Instalación Local

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/fernanda7v/PROYECTO-MICRORED
    ```

2.  **Crear entorno virtual e instalar dependencias:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # En Windows
    pip install -r requirements.txt
    ```

3.  **Configurar Base de Datos:**
    * Crear base de datos en MySQL llamada `microred_db`.
    * Configurar credenciales en `settings.py`.

4.  **Ejecutar migraciones:**
    ```bash
    python manage.py migrate
    ```

5.  **Crear Superusuario (Admin):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Correr el servidor:**
    ```bash
    python manage.py runserver