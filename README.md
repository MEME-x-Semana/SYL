![Texto Alternativo](https://res.cloudinary.com/dciovdqaf/image/upload/v1702669538/Portada_smogaf.png)

# Documentación del Proyecto de Desarrollo Web "See You Later"

## Introducción
Este repositorio contiene la documentación detallada del proyecto de desarrollo web "See You Later", realizado como parte del curso/beca de "Codo a Codo": Full Stack Python 2023. Nuestro equipo, compuesto por cuatro miembros, trabajó de manera colaborativa en la creación de una página tipo landing page para la agencia ficticia de cruceros "See You Later", con el propósito de vender pasajes de cruceros de distintas compañías.

## Equipo
- Axel Criado
- Fabricio Barreto
- Flavia S. Briglia
- Karina Bianco

## Fase de Inicio
En el primer mes de nuestro proyecto, llevamos a cabo reuniones virtuales para conocernos, debatir las ideas y establecer los objetivos del proyecto.

## Diseño y Planificación
- Se utilizó la herramienta Figma para crear el diseño y wireframe del sitio.
- El diseño fue revisado y aprobado por todo el equipo, antes de proceder a la implementación.

## Desarrollo Frontend
El frontend se realizó utilizando HTML, CSS, JavaScript y Bootstrap. Se aseguró la funcionalidad responsive para distintos dispositivos.

## Integración con Django Backend
- Se instaló Django dentro de un entorno virtual (.venv).
- Se creó el proyecto Django e integró el frontend con el backend, configurando los archivos estáticos (media, css y scripts) para la correcta unión entre ambas partes.
- Se configuraron los modelos y se realizaron las migraciones necesarias para gestionar los viajes de cruceros.
- Se configuraron vistas y templates para la administración de viajes, detalles, actualización y eliminación.
- Se implementó la conexión con la base de datos MySQL en lugar de SQLite.


## Funcionalidades Destacadas
- Diseño Responsive para móviles, tablets y desktop.
- Utilización de la API Rest de FormSubmit para el formulario de contacto.
- Uso extensivo de Jinja en todos los templates, permitiendo la integración entre frontend y backend.
- Implementación de la lógica dinámica para mostrar imágenes de compañías de cruceros según el nombre de la compañía.
- Personalización de vistas en `views.py` para el manejo de DeleteView y la incorporación de lógica adicional para el manejo de solicitudes de eliminación, sumado a la configuración de funcionalidades adicionales como Sweet Alert 2 para el manejo de mensajes y acciones en la interfaz de usuario.


## Deploy
Se realizó un deploy inicial en PythonAnywhere.


## Problemas Actuales
- Problemas encontrados durante el despliegue en Python Anywhere, actualmente en proceso de resolución.


## Referencias

- Enlaces a recursos utilizados:
    - Fuentes: [Google Fonts](https://fonts.googleapis.com/css2?family=Inika&display=swap)
    - FormSubmit: [FormSubmit](https://formsubmit.co/)

- Enlace al Proyecto

    - [See You Later Landing Page](https://kbianco.pythonanywhere.com/)
    
- Información de Contacto
    - axelivancriado@gmail.com
    - fabrib40@gmail.com
    - fbrig87@gmail.com
    - karina_bianco@hotmail.com
