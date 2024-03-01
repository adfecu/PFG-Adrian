# PFG-Adrian
Desarrollo de un sistema basado en inteligencia artificial para la clasificación de muestras de Papanicolaou

Voy a desarrollar e implementar un modelo de IA para clasificar las muestras de Papanicolaou en normal y anormal.

La tasa de verdaderos positivos y negativos del PAP convencional varían según los estudios. Sitúan una tasa de verdaderos positivos del 55 al 80 por ciento y una tasa de
verdaderos negativos del 75 al 99 por ciento. Actualmente, el proceso de inspeccionar una placa de PAP es completamente manual y depende de la habilidad del patólogo, lo
que puede resultar en un resultado inadecuado de esta prueba diagnóstica, junto con otras variables. He investigado el estado del arte de los modelos de IA que pueden
analizar una muestra de Papanicolaou y suelen funcionar mejor que los humanos. Es factible crear un modelo como estos y lograr resultados que puedan ayudar al patólogo
a tomar mejores decisiones.

La empresa me proporcionará 500 muestras de Papanicolaou convencionales y en base líquida que han sido etiquetadas por un equipo de patólogos. Después, las
escanearé utilizando un escáner para portaobjetos de patología digital. Después podré realizar una exploración de los datos, para evaluar features que utilizaré en el modelo.
Estas imágenes de portaobjetos son archivos de tipo .svs, que son aquellos archivos para imágenes de patología digital (whole slide images) de gran tamaño y resolución. El
modelo primero dividirá la imagen en mosaicos pequeños para trabajar con estos archivos. Aunque divida la imagen y no tenga las etiquetas de los mosaicos individuales, no
necesitaré anotaciones adicionales de patólogos. Para clasificar las muestras a partir de los mosaicos individuales, usaré un modelo de aprendizaje multi-instancia.

Voy a entrenar, validar y probar el modelo con las 500 muestras escaneadas. Una vez satisfecho con las métricas de rendimiento, voy a desplegar el modelo en una
aplicación de ordenador. La empresa probará el modelo con muestras previamente no vistas y me podrá dar retroalimentación de su uso en el workflow de la empresa.