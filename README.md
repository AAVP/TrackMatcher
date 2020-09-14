# TrackMatcher
> Aplicación de Data Science en el mundo de la música

## Aspectos generales
Este repositorio presenta un conjunto de módulos que permiten crear una GUI donde, a través de la implementación de algoritmos de Ciencias de datos insertos en las APIs de Musixmatch, es posible:

1. **Encontrar una canción** por un fragmento de la letra, sin previo conocimiento del nombre de la canción y del artista, o también por su nombre.
2. Recibir **recomendaciones** de canciones mejor valoradas de un género dado.
3. Solicitar las **canciones trending** de un país dado.
4. Solicitar los **artistas trending** de un país dado.

Adicionalmente a esto, el programa automáticamente señala a través de Sentiment Analysis el tipo de sentimiento que expresa la canción, catalogado en los seis sentimientos más comunes del ser humano: ***disgusto, ira, tristeza, felicidad, sorpresa y miedo.***

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
Para ejecutar el programa se debe correr el archivo ...................
