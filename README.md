# Destroyer-Rocket
1. Idea general
La idea fue simplemente un videjuego tipo space invaders, con una nave de movimiento horizontal que disparara para destruir cosas, en este caso, meteoros.
2. Clases

Jugador: Consiste en su sprite, y su movimento (como los de todas las cosas que se mueven) se da por mover 5 pixeles, por cada iteracion en el evento de presionar la tecla izquierda o derecha, y disparar con la tecla de espacio.

Meteoro: Es una serie de imagenes de distintos meteoros, donde cada que aparece uno se elige por medio de la bibioteca random un sprite para el meteoro que saldra, siendo 10 en pantalla por normalidad (Desde arriba, con una coordenada elegida por la biblioteca random), donde si es destruido ya sea por chocar con la nave, chocar con un laser o salir de la pantalla, se generara otro para reemplazarlo inmediatamente.

Laser: Consiste en la imagen del laser moviendose siempre hacia arriba con velocidad constante con origen en el punto medio del jugador.

Explosion: Para facilidad del proceso de que la explosion generase un gif, se le convirtio en una clase, con un funcionamiento especial, resuta que basandose en los frames que pasan en su ejecucion, muestra un sprite diferente para generar a iusion del gif.

3. Funciones

Pantalla de inicio y final: Al inicio y al final tenemos la pantalla que muestra el titulo, donde basta con presionar una tecla para empezar a jugar.

Colision laser-meteoro: En esta colision tenemos en cuenta que se desaparecen ambos, pero debe regenerarse el meteoro, ademas de ser el momento en que se genera nuestra explosion, con todo y su sonido.

Barra de vida: Tenemos una barra de vida, que resiste exactamente 10 colisiones de la nave con meteoros, al llegar a cero, aparece la pantalla del inicio.

Colision nave-meteoro: En esta interaccion, el meteoro se regenera, y la barra de vida se reduce en un 10%.

Disparo: Al presionar la tecla espacio se genera el disparo ya mencionado, con su respectivo sonido.

Musica: Tenemos musica de fondo, en todo momento.

Pausa: Tenemos un menu de pausa, que se trata de un ciclo While que se finaiza al presionar de nuevo la tecla "p", cuando el jugador la presiona mientras el juego se esta ejecutando, la ejecucion se pausa, aparece la leyenda de pausa, con sus instrucciones, y ademas la musica baja su volumen, para salir de este basta con presionar la tecla "p" o salir del juego.
