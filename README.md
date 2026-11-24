# Análisis de Respuestas a Publicaciones en X

Este trabajo utiliza el conjunto de datos empleado en el estudio <em>Assessing the Impact of Contextual Information in Hate Speech Detection</em>[2].

Los datos fueron recopilados entre marzo de 2020 y marzo de 2021, en el contexto de la pandemia de COVID-19, período caracterizado por un incremento del discurso de odio en las redes sociales. El conjunto de datos comprende publicaciones realizadas en Twitter (actualmente X) [3] por los medios de comunicación argentinos La Nación, Clarín, Infobae, Perfil y Crónica, junto con sus respectivas respuestas de primer orden [1]. Para la construcción del corpus, se consideraron exclusivamente aquellas publicaciones que contenían enlaces a artículos periodísticos relacionados con la pandemia y más de cincuenta respuestas.

## Diccionario de Datos

|Columna|Descripción|
|-------|-----------|
|id|Identificador de respuesta.|
|title|Título de la publicación.|
|text|Texto de la respuesta.|
|context_tweet|Publicación del medio de comunicación.|
|body|Texto completo del artículo en el sitio de noticias.|
|HATEFUL|Etiqueta de discurso de odio: 0-No, 1-Si.|
|CALLS|Etiqueta de llamada a la violencia: 0-No, 1-Si.|
|WOMEN|Etiqueta de discurso en contra de las mujeres: 0-No, 1-Si.|
|LGBTI|Etiqueta de discurso en contra de la comunidad LGBTI: 0-No, 1-Si.|
|RACISM|Etiqueta de discurso en contra de una etnia: 0-No, 1-Si.|
|CLASS|Etiqueta de discurso en contral de una clase social: 0-No, 1-Si.|
|POLITICS|Etiqueta de discurso en contra de un partido político: 0-No, 1-Si.|
|DISABLED|Etiqueta de discurso en contra de las personas discapacitadas: 0-No, 1-Si.|
|APPEARANCE|Etiqueta de discurso en contra de personas con cierta apariencia física: 0-No, 1-Si.|
|CRIMINAL|Etiqueta de discurso en contra de delincuentes o presos: 0-No, 1-Si.|

## Limpieza de Comentarios

Como etapa previa a la aplicación de técnicas de clasificación automática para la detección de discurso discriminatorio, resulta necesario realizar un preprocesamiento de los textos [4]. En el contexto de este trabajo, dicho procedimiento se aplica a los comentarios que conforman el corpus de estudio.

1. Eliminar URLs
1. Eliminar hashtags
1. Eliminar menciones
1. Eliminar espacios y comillas
1. Eliminar vocales repetidas (ej. amooooor)
1. Reemplazar emoticones por palabras que los representen (ej.. reemplazar :) con sonrisa)
1. Reemplazar negaciones (i.e., replace can’t, don’t, never
with not)
8. Reemplazar slang (i.e., replace
l8 with late)
9. Reemplazar variaciones de palabras con su raíz. (i.e., Replace words like
‘‘great,’’ ‘‘greatly,’’ ‘‘greatest,’’ and ‘‘greater’’ with the
single word ‘‘great,’’ reducing entropy and improving
the relevance of the concept of ‘‘great’’)

## Referencias
1. Perez, J., Luque, F., Zayat, D., Kondratzky, M., Moro, A., Serrati, P., Zajac, J., Miguel, P., 		Debandi, N., Grabano, A. y Cotik, V. (2023). Assessing the Impact of Contextual 		Information in Hate Speech Detection. IEEE Access.
\
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10076443
1. Pérez, J., Cotik, V., Luque, F., Moro, A., Serrati, Pablo., Miguel, P., Debandi, N., Gravano, A. 	(2024). Contextualized Hate Speech. Consejo Nacional de Investigaciones 		Científicas y Técnicas. (dataset).\
http://hdl.handle.net/11336/235509
1. When Did Twitter Become X? (2026).\
https://tweetfull.com/blog/when-did-twitter-become-x-timeline-dates-and-key-changes/
1. Al-Qablan, T.A., Mohd Noor, M., Al-Betar, M.A. et al. (2023). A survey on sentiment analysis and its applications. Neural Comput & Applic 35, 21567–21601. https://doi.org/10.1007/s00521-023-08941-y