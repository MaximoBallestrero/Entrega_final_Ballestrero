Hola, aca dejo la entrega final.    
La verdad es que no sabia donde mas documentar los casos de prueba asi que los voy a dejar aca.    
Caso 1:  
Objetivo: Checkear que los Enters se muestren/guarden cuando lees un review, y en el bio de los usuarios.  
Pasos:  
1: Pongo a andar el servidor  
2: Creo un review (desde admin, todavia no hice que se puedan hacer desde la pagina) y pongo varios Enters.  
3: Voy a la pagina para leer ese review.  
4: No figuran.  
Solucion:  
Me fije en admin en la review que habia creado, y cuando puse para editarla, los Enters estaban ahi en el formulario. Esto significa que se guardaron perfecto, y el tema es hacer que se vean en el template. Despues de investigar un poco, descubri que para que se vean, hay que agregar al {{review.texto}} esto:  
{{review.texto|linebreaks}}  
Despues de agregarlo, me ando perfecto.

