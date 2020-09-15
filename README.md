# TrackMatcher
> Aplicación de Data Science en el mundo de la música

## Aspectos generales
Este repositorio presenta un conjunto de módulos que permiten crear una GUI donde, a través de la implementación de algoritmos de Ciencias de datos insertos en las APIs de Musixmatch, es posible:

1. *Encontrar una canción* usando un fragmento de la letra, sin previo conocimiento del nombre de la canción y del artista. También es posible encontrar la letra de una canción, sabiendo su nombre.
2. Recibir *recomendaciones* de las canciones mejor valoradas de un género dado.
3. Solicitar las *canciones trending* de un país dado. Se puede seleccionar el número top de canciones deseado, por ejemplo: Top 10; Top 25: Top 100.
4. Solicitar los *artistas trending* de un país dado. Se puede seleccionar el número top de artistas deseado, por ejemplo: Top 10; Top 25: Top 100.

Adicionalmente a esto, el programa automáticamente señala a través de Sentiment Analysis el tipo de sentimiento que expresa la canción, catalogado en los seis sentimientos más comunes del ser humano: **Disgusto, Ira, Tristeza, Felicidad, Sorpresa y Miedo.**



## Base de datos
La base de datos usada para poder entrenar el modelo de Recurrent Neural Networks (Redes neuronales recurrentes) fue extraída de las siguientes url's: https://www.kaggle.com/yelinnzaw/song-lyrics-dataset, https://www.kaggle.com/yelinnzaw/songlyric. Ambas bases de datos contienen las mismas columnas, pero son registros distintos. Lo que se hizo para entrenar el modelo fue tomar todos los datos del primer url y parte de los registros del segundo url. Para testear el modelo se uso el remanente de este último url.

## Librerías
El programa si bien usa las librerías que no requieren instalación, tales como ```os```, ```csv``` y ```json```, también requiere ciertas instalaciones de librería externas como ```tensorflow```, ```numpy```, ```requests``` y ```pyqt5```.

Si se desea descargar el repositorio y probarlo en el sistema local, existen dos maneras de llevar a cabo la instalación de las librerías.

### (Recomendada) Descarga de librerías a través de requirements.txt
El repositorio cuenta con un archivo de extensión .txt que contiene todas las librerías necesarias con sus respectivas versiones. Teniendo este archivo, y yendo al terminal o cmd de su sistema local debe ingresar el siguiente código:

```shell
pip install -r requirements.txt
```

### Descarga de librerías manualmente en el prompt
A continuación se presentarán los comandos de línea que se necesitan ingresar en el shell para el correcto funcionamiento de los módulos del repositorio:

```shell
pip install tensorflow
pip install numpy
pip install requests
pip install pyqt5
```

## Ejecución 
Para ejecutar las funcionalidades de el buscador de canciones y/o letras se debe ejecutar el código del archivo ```musixmatch_api.py```. Al final de este código se deben especificar los parámetros de la búsqueda de la siguiente manera:

1. Para buscar una canción se debe modificar la llamada de la función ```music_matcher```:

    * Si se desea buscar por la letra de la canción, debe especificar 'by_lyrics': True,'lyrics': <LETRA DE LA CANCIÓN>,'artist': <NOMBRE ARTISTA> (Artista es un parámetro opcional).
  
    * Si se desea buscar por el nombre de la canción, debe especificar 'by_lyrics': False, 'track': <NOMBRE CANCION>, 'artist': <NOMBRE ARTISTA> (Artista es un parámetro opcional).
  
2. Para buscar las canciones mejor valoradas de un género musical dado, se debe modificar la llamada de la función ```recommendations_genre```, asignando como parámetros: 'top': <CANTIDAD SOLICITADA>, 'genre': <GÉNERO MUSICAL>.
  
3. Para buscar el top de canciones de un país dado, se debe modificar la llamada de la función ```top_tracks```, asignando como parámetros: 'top': <CANTIDAD SOLICITADA>, 'country': <PAÍS>.
  
4. Para buscar el top de artistas de un país dado, se debe modificar la llamada de la función ```top_artists```, asignando como parámetros: 'top': <CANTIDAD SOLICITADA>, 'country': <PAÍS>.

Para ejecutar el programa de Sentiment Analysis de una canción se debe ejecutar el archivo ```neural_network.ipynb```, correr todas las celdas de código hasta el proceso de "Tokenización".


## Visualización
Nuestra noción a futuro es que el usuario se enfrente a una Interfaz de Usuario utilizando la librería ```PyQt5``` donde podrá interactuar con el programa a través de la selección de botones e ingreso de texto.

El usuario tendrá la posibilidad de presionar 2 grandes botones. El primero, “SEARCH”, le permitirá usar la función de buscar una canción desconocida usando una parte del texto de la canción o alternativamente encontrar el texto de una canción, sabiendo su nombre. El segundo, “EXPLORE”, le permitirá al usuario usar las otras tres funciones de la aplicación. Estas son descubrir canciones de un genero dado, el Top de canciones de un país dado, o  el Top de artistas de un país dado.
