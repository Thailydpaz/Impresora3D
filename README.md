## Diseño y manufactura de una impresora 3D

## Descripción
Este proyecto es una impresora 3D que te permite convertir modelos digitales en objetos físicos tridimensionales.

## Características Principales
- Construcción capa por capa para precisión detallada.
- Esta impresora 3D esta aaptada para utilizar PLA como material de impresión.
- Fácil instalación y configuración.

## Requisitos del Sistema
- IDE Arduino
- Marlin 1.1.9
- Repetier 

## Instrucciones de Uso
-[1] Descargar el IDE  de arduino  				//https://www.arduino.cc/en/software
-[2] Debes instalar la siguiente libreria  
	//https://minkafab.com/docs/U8glib.rar
 una vez descargada y descomprimida, se debe colocar la carpeta ""U8glib"" dentro de \Documentos\Arduino\libraries, (Si no existe la carpeta libraries puedes crearla)
-[3] Descargar y descomprimir el firmware pre-configurado  
	//https://minkafab.com/docs/Impresora%20Minkafab.rar
-[4] Abrimos la carpeta \Impresora Minkafab\Marlin , aquí debemos buscar el archivo Marlin.ino, este archivo lo podemos abrir con el programa Arduino (Cuando abramos el archivo, se desplegarán en pestañas todos los archivos necesarios que Marlin necesita).
-[5] Conectamos nuestra computadora a la impresora, del puerto usb al puerto serial del Arduino Mega (La computador automáticamente la reconocerá y nos asignará un puerto serial COM).
-[6] Damos clic en Herramientas\Placa y seleccionamos la placa: Arduino/Genuino Mega or Mega 2560.
-[7] También seleccionamos el puerto COM asignado haciendo clic en  Herramientas\Puerto
-[8] Finalmente subimos el nuevo firmware dando clic en el icono "subir", que se muestra como una flecha hacia la derecha.
-[9] Esto tardará un poco, y al final nos aparecerá en consola que el programa se subió con éxito, recuerda que debes colocar la librería U8glib, descrita en el paso 2 , para que pueda compilar y subirse el programa.
-[10] Instalamos en software repetier 
	//https://www.repetier.com/download-now/
una vez descargado el archivo, lo descomprimimos y lo ejecutamos.

##Como imprimir
- Se crea la pieza en 3D en el software CAD de preferencia y se guarda como .STL
- Una vez guardado el archivo .STL lo abrimos en el programa Repetier. 
- Ajustamos losmparametros de impresión.
- Guardamos el archivo .gcode en una memoria SD 
- Colocamos la memeria SD en la controladora 
- Seleccionamos el archivo a imprimir y aceptamos.


##Lista de materiales materiales:
-Arduino mega
-Ramps 1.4 
-4 drivers a4988
-3 motores a pasos nema 17
-Extrusora MK8
-LCD 12864
-Cama caliente 
-Fleje magnetico y sobre cama 
-Guias lineales 6mm, 8mm y 10mm de diametro 
-Tornillo sin fin 
-Tornillo de bola
-Husillo
-Soporte BK10
-Soporte BF10
-Acoplamiento flexible 
-2 Poleas dentadas GT2 5mm
-10 Poleas dentadas GT2 8mm
-Filamento PLA
-Perfil de aluminio 
-Perfil de aluminio 
-Lamina fría 
-Soporte fijo SK10
-Tornillos 
-Cable 
-Conectores dupon 
-Finales de carrera 
-Termopar 
-Acrilico 
-Fuente de poder 12VCD


## Contribución
¡Agradecemos contribuciones! Si deseas colaborar, envia un mensaje al correo [l201080406@iztapalapa.tecnm.mx].

## Problemas y Sugerencias
Si encuentras problemas o tienes sugerencias, por favor contáctanos en [l201080406@iztapalapa.tecnm.mx].

## Licencia
Este proyecto está bajo la licencia [GPLv3, creative common].

---

**¡Comienza a imprimir tus ideas hoy!**
