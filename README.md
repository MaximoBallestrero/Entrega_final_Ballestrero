Hola, aca dejo la entrega final.    
Aca el link donde lo explico: https://youtu.be/xhwhlENzoFw  
La verdad es que no sabia donde mas documentar los casos de prueba asi que los voy a dejar aca.    
Caso 1:  
Objetivo: Checkear que los Enters se muestren/guarden cuando lees un review, y en el bio de los usuarios.  
Pasos:  
1: Pongo a andar el servidor  
2: Creo un review (desde admin, todavia no hice que se puedan hacer desde la pagina) y pongo varios Enters.  
3: Voy a la pagina para leer ese review.  
Resultado: No figuran.  
Solucion:  
Me fije en admin en la review que habia creado, y cuando puse para editarla, los Enters estaban ahi en el formulario. Esto significa que se guardaron perfecto, y el tema es hacer que se vean en el template. Despues de investigar un poco, descubri que para que se vean, hay que agregar al {{review.texto}} esto:  
{{review.texto|linebreaks}}  
Despues de agregarlo, me ando perfecto.  
Caso 2:  
Objetivo: Asegurarse que en los campos para imagenes (posters y avatars) solo te deje subir imagenes, y no otro tipo de archivo.  
Pasos:  
1: Pongo a andar el servidor.  
2: Entro a la pagina para crear reviews. Y completo todos los campos menos el de imagen.  
3: Trato de subir varios archivos (videos, archivos de python, html y mas)  
Resultado: No me deja subir ningun archivo que no sea imagen :)  
Caso 3:  
Objetivo: ver que pasa si cambio el max_length del campo 'pelicula' de mi form para crear reviews con inspect  
Pasos:  
1: Pongo a andar el servidor.  
2: Voy a la pagina para crear reviews. Pongo inspect, y voy a donde dice el max length del campo pelicula. Lo extiendo a 80 (es 40).  
3: Veo que ahora me deja escribir mas de 40 caracteres.  
4: Completo los otros campos y apreto el boton para crear reviews.  
Resultado: A pesar de que en el campo me dejo escribir mas, cuando lo envio, no se guarda y me da un mensaje de error por la cantidad de caracteres de mas que puse.


