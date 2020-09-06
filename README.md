# TrackMatcher
> Aplicación de Data Science en el mundo de la música

## Aspectos generales
Este repositorio presenta un conjunto de módulos que permiten crear una GUI donde, a través de la implementación de algoritmos de Ciencias de datos insertos en las APIs de Musixmatch, es posible:

1. **Encontrar una canción** por un fragmento de la letra, sin previo conocimiento del nombre de la canción y del artista, o también por su nombre.
2. Recibir **recomendaciones** de canciones mejor valoradas de un género dado.
3. Solicitar las **canciones trending** de un país dado.
4. Solicitar los **artistas trending** de un país dado.

Adicionalmente a esto, el programa automáticamente señala a través de Emotion Analysis el tipo de sentimiento que expresa la canción, catalogado en los seis sentimientos más comunes del ser humano: ***disgusto, ira, tristeza, felicidad, sorpresa y miedo.***

## Base de datos
La base de datos usada para poder entrenar el modelo de Recurrent Neural Networks (Redes neuronales recurrentes) fue extraída de la siguiente url: https://www.kaggle.com/yelinnzaw/song-lyrics-dataset.

## Librerías
El programa requiere las librerías ```json``` (no requiere instalación), ```tensorflow``` y ```requests```.

A continuación se presentarán los comandos de línea que se necesitan para el correcto funcionamiento de los módulos del repositorio:

```shell
pip install tensorflow
pip install requests
```

## Ejecución
Para ejecutar el programa se debe correr el archivo ...................
