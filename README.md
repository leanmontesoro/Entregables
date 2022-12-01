# Entregables
## Objetivo
La web tiene el objetivo de ser un repositorio de carga de jugadores, equipos y técnicos de fútbol.
- - -
## Funcionalidades desarrolladas
A continuación  se describirá como acceder a cada funcionalidad solicitada por la primer entrega del proyecto final.

- **Herencia de HTML:** template_padre.html posee en las lineas 38 y 74 el código jinja que permite luego reutilizar este template. Un ejemplo: AppEntregable1\templates\tecnicoFormulario.html
- **Clases Models:** Se generaron 3 clases en models, para modelar a los Jugadores, equipos y técnicos: AppEntregable1\models.py
- **Formulario para insertar datos:** Esta funcionalidad se encuentra sobre los Jugadores. Desde el botón superior "Jugadores", luego "Formulario de jugadores" se puede insertar un jugador.
- **Formulario de busqueda:** Esta funcionalidad se encuentra sobre los Jugadores. La clave para la busqueda es el equipo. Desde el botón superior "Jugadores", luego "Busqueda de jugadores", ingresando un equipo se listan los jugadores que tengan en su atributo equipo alguna coincidencia con lo ingresado. La lógica de la busqueda se encuentra en AppEntregable1\views.py:94
 
