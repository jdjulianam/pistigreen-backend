# Pistigreen

Es una red social dedicada a conectar personas interesadas en la ecología y sostenibilidad. La aplicación está desarrollada con Vue 3, Pinia para la gestión del estado, Vue Router para la navegación, Axios para las peticiones HTTP y Django en el backend.

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).




## Tabla de Contenidos
- [Características](#características)
- [Tecnologías](#tecnologías)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)


## Características
- Publicación y visualización de posts ecológicos
- Sistema de comentarios y likes
- Gestión de perfiles de usuario
- Sugerencias de amigos
- Tendencias y temas populares

## Tecnologías
### Frontend
- Vue 3
- Pinia
- Vue Router
- Axios

### Backend
- Django
- Django REST Framework

## Instalación
### Backend
1. Clona el repositorio:
    ```sh
    git clone https://github.com/Eddu-ER-Tech/pistigreen-backend.git
    
    ```

2. Crea y activa un entorno virtual:
    ```sh
    python -m venv env
   env\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Realiza las migraciones y ejecuta el servidor:
    ```sh
    python manage.py migrate
    python manage.py runserver
    ```

### Frontend
1.Clona el repositorio:
     ```sh
    git clone https://github.com/jdjulianam/pistigreen_frontend.git
    cd front
    ```

2. Instala las dependencias:
    ```sh
    npm install
    ```

3. Ejecuta la aplicación en modo desarrollo:
    ```sh
    npm run serve
    ```

## Uso
- Accede a `http://localhost:8000` para el backend.
- Accede a `http://localhost:8080` para el frontend.

## Estructura del Proyecto

pistigreen_frontend/
├── back/pistigreen-backend
│ ├── acount
│ ├── backend-pistigreen
│ ├── env
│ ├── notification
│ ├── post
│ ├── post_attachments
│ ├── search
│ ├── .gitinore
│ ├── db.sqlite3
│ ├── gitignore.txt
│ ├── manage.py
│ ├── package-lock.json
│ ├── pip
│ ├── README.md
│ ├── requirements.txt
├── front/
│ ├── public/
│ ├── src/
│ │ ├── assets/
│ │ ├── components/
| | ├── router.js
│ │ ├── views/
│ │ ├── store/
│ │ ├── App.vue
│ │ ├── main.js
├── .browserslistrc
├── jsonconfig.json
├── package-lock.json
├── package.json
├── postcss.config.js
├── README.md
├── tailwind.config.js
├── vue.config.js




## Enlace del video explicativo
<a href="https://youtu.be/TYdzIIdHnx4">Parte 1</a> 
<a href=" https://youtu.be/-U9rAecn2WY">Parte 2</a>
<a href="https://youtu.be/TYdzIIdHnx4">Parte 3</a> 


## Enlace del despliegue
<a href="https://front-tau-nine.vercel.app/ ">Despliegue</a>

