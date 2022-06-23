<h1> RSA</h1>
1. Objetivo: Se creó un algoritmo que permite generar el sistema de cifrado RSA, incluyendo una variante que permite determinar diferentes valores RSA dependiendo la cantidad de bits.<br> 2. Función Fermat: Esta función recursiva nos permite resolver códigos de estructura (a^x) mod n de manera más eficiente y reduciendo la cantidad de exponenciaciones que se realice para resolver el problema.<br> <img align="center" src="https://user-images.githubusercontent.com/85748915/175205411-e2f1bd90-6c43-4dcc-af69-4b2684a960bd.png" alt="carlossalvadordiaz" /></p> <br>3. Función Es_Compuesto: La Función permite la determinación de un número como compuesto false o primo true.<br> <img align="center" src="https://user-images.githubusercontent.com/85748915/175205540-ce34961a-6bb7-4a03-b86f-c888f557bf9f.png" alt="carlossalvadordiaz" /></p><br> 4. Función Miller : Esta función pone en practica el Test de primalidad de Miller Rabin para ello recibe 2 argumentos, siendo el “n” el número que se debe determinar si es primo o no, mientras que “s” es el número de bases para las cuales se va a probar el “n”. Una vez ejecutada, la función nos va a retornar como resultado un booleano. <br><img align="center" src="https://user-images.githubusercontent.com/85748915/175205683-3d02ef51-c492-4f00-b458-253791316e27.png" alt="carlossalvadordiaz" /></p> <br>5. Función Randombits: Tiene por finalidad crear un número impar de b cantidad de bits, el cual se usará mas adelante para generar números primos.<br> <img align="center" src="https://user-images.githubusercontent.com/85748915/175205889-4484c2f9-39b2-451b-8b50-184b7a322147.png" alt="carlossalvadordiaz" /></p><br>6. Función Randomgen: Tiene por finalidad generar números primos, usando como número base al resultado de la función Randombits, para luego aplicarle el Test de Miller, el cual nos devolverá, mediante un bucle, nos devolverá un número que pase el test, es decir que sea primo.<br> <img align="center" src="https://user-images.githubusercontent.com/85748915/175206046-08e1f32a-17b9-4b43-94bf-245bc490c8b4.png" alt="carlossalvadordiaz" /></p><br> 7. Función Euclides: Tiene la finalidad de calcular el MCD de dos números. <img align="center" src="https://user-images.githubusercontent.com/85748915/175206209-cf5541d6-66fe-4f49-b9e8-c78f51f49078.png" alt="carlossalvadordiaz" /></p><br> 8. Función Euclides Extendido: Tiene la misma finalidad que el Euclides normal, pero también podemos usarlo para obtener el inverso de un determinado número. Le asociamos una función extra para extraer el inverso de una manera más adecuada, la función INVERSO. <br><img align="center" src="https://user-images.githubusercontent.com/85748915/175388003-71e0fa37-47d2-4aa2-b462-2a4add9e4d47.png" alt="carlossalvadordiaz" /></p> <br>9. Función RSA_KEY_GENERATOR: Esta función es la protagonista, la cual calculará el sistema RSA con sus respectivos valores para comenzar con el cifrado y descrifado <br><img align="center" src="https://user-images.githubusercontent.com/85748915/175207333-5745c59f-daf1-440a-9a59-9557ccfe2d56.png" alt="carlossalvadordiaz" /></p><br> 10. Función Cifrado: Permite cifrar el mensaje que queremos con los valores exactos, mediante Fermat <img align="center" src="https://user-images.githubusercontent.com/85748915/175207463-d8f3f55d-2cd1-41c4-9b22-d7d4150e5ab3.png" alt="carlossalvadordiaz" /></p> <br>11. Función Descifrado: Descifra lo anterioremente cifrado, comprobando lo bien que funciona el código<br> <img align="center" src="https://user-images.githubusercontent.com/85748915/175207672-6d3bfec3-6721-4204-a88a-a9d7364c55d3.png" alt="carlossalvadordiaz" /></p><br> 12. Implementación de todo lo que hemos hecho: Aquí usaremos todas las funciones para cifrar y descifrar un elemento, comprobando la viabilidad del código <br>
<img align="center" src="https://user-images.githubusercontent.com/85748915/175387658-dd4c7812-d940-4966-8ba8-5b8b327fb2df.png" alt="carlossalvadordiaz" /></p><br>
13. Imprimir tabla: esta sección imprimirá 10 valores para probar la efectividad del código con diferentes parámetros
<br>
<img align="center" src="https://user-images.githubusercontent.com/85748915/175387731-e256a74d-344f-4e02-842b-7f929edf3bc5.png" alt="carlossalvadordiaz" /></p>


