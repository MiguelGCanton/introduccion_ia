## Aplicaciones a analizar

Describe PEAS para cada una de estas aplicaciones:

1. **Asistente virtual de voz** (p. ej. Siri, Alexa o Google Assistant en un altavoz inteligente).
2. **Robot aspirador doméstico** (p. ej. Roomba u otro robot que limpia pisos de un departamento).
3. **Sistema de recomendación de streaming** (p. ej. Netflix o Spotify que sugiere películas o canciones).
4. **Vehículo autónomo en ciudad** (conducción sin conductor en calles urbanas con tráfico y peatones).
5. **Agente de trading algorítmico en bolsa** (compra y venta automática de acciones en mercados financieros).
6. **Sistema de diagnóstico médico asistido por IA** (apoya a un médico a interpretar síntomas e imágenes clínicas).
7. **Dron de inspección de infraestructura** (revisa grietas, corrosión o fugas en puentes, tuberías o líneas eléctricas).
8. **Agente jugador de ajedrez** (programa que compite contra un humano u otro agente en partidas completas).

## Instrucciones

Para **cada** aplicación entrega una sección con este formato:

```markdown
### N. Nombre de la aplicación

- **Performance:** ...
- **Environment:** ...
- **Actuators:** ...
- **Sensors:** ...
```

### **1. Asistente virtual de voz**

Estoy pensando en la alexa de mi casa que tiene un uso domestico y esta conectada a los servicios de amazon y de spotify.

- **Performance:** Contestar adecuadamente a cada solicitud del usuario, capaz de entender el problema, tiempo de respuesta; satisfacción del usuario; solo se activa con los comandos.
- **Environment:** Una casa, oficina o cualquier otra habitacion.
- **Actuators:** reproducir música, crear recordatorios, alarmas, realizar llamadas, consultar APIs (clima, noticias) y interactuar con todos los dispositivos que se puedan conectar con internet de las cosas, apis de amazon y otros servicios registrados.
- **Sensors:** microfono, reloj.

#### AIMA
Parcialmente observable: el usuario puede saber si alexa entendio la solicitud y puede ver la accion resultante, pero jamas que hizo para conseguir la informacion en algunos casos ni se sabe que servicios llama.

### **2. Robot aspirador doméstico**

Me imagino la clasica aspiradora que recorre cada parte de la habitacion.

- **Performance:** Cantidad de suciedad en el piso antes de limpiar, cantidad de suciedad en el piso despues de limpiar, tiempo que permanece la suciedad en el piso.
- **Environment:** Una casa, oficina o cualquier otra habitacion.
- **Actuators:** herramientas para limpiar y las llantas que usa para moverse.
- **Sensors:** sensor de suciedad, sensor para detectar el espacio de una habitacion.

#### AIMA

Secuencial: el robot determina las areas para limpiar y las acciones anteriores (zonas que limpio anteriormente) afectaran las siguientes areas para limpiar.

### **3. Sistema de recomendación de streaming**

Estoy pensando en el sistema de netflix que te da una lista cuando abres la app.

- **Performance:** Cantidad de peliculas recomendadas, que tanto son elegidas las peliculas que recomienda, si las que recomendo fueron disfrutadas por el usuario.
- **Environment:** Cualquier hardware en el que se pueda ejecutar.
- **Actuators:** Todos los dispositivos que se puedan conectar con internet de las cosas, apis y otros servicios registrados.
- **Sensors:** Historial de peliculas del usuario, intereses registrados por el usuario, data de usuarios similares.

#### AIMA

Secuencial: dependiendo de si el usuario toma o no las recomendaciones, el sistema podria usar esa informacion para elegir futuras recomendaciones.

### **4. Vehículo autónomo en ciudad**

Un vehiculo que puede conducirse de manera autonoma pero que tiene que ser tuyo como en el caso de tesla (no como es el waymo que se renta y tiene servicios para contactar a una persona si tienes problemas con el vehiculo)

- **Performance:** número de accidentes, velocidad, tiempo de reaccion ante eventos, tiempo que permanece en la ruta, en el contexto de los autos de bateria y que ejecutar una inteligencia artificial requiere energia, la bateria podria ser un factor, cualquier ley. 
- **Environment:** una ciudad, un sendero en el monte, el estacionamiento de algun lugar o dentro de una casa (porch).
- **Actuators:** volante, freno, camaras, microfonos, gps, luces.
- **Sensors:** camaras, microfono, gps, sensores de temperatura.

#### AIMA

Parcialmente observable: a pesar de que las camaras y sensores capturan lo que hay en el ambiente, cuando le agregas otras variables como neblina, humedad o velocidad el sistema tal vez no sea capaz de detectar cosas que en un estado mas tranquilo si podria.


### **5. Agente de trading algorítmico en bolsa**

Una de esos apps de banco que te dicen que oportunidades hay y te envian notificaciones diciendo que esta bajando de precio y te dan los clasicos analisis de tu dinero.

- **Performance:**: dinero ganado, disminucion de perdidas (si detecta que una accion va a bajar mucho la vende lo antes posible), 
- **Environment:** mercados financieros globales; computadoras personales, servidores
- **Actuators:**: funciones para comprar, vender y estimar
- **Sensors:** apis, noticias, historial de precios.

#### AIMA
Secuencial: Todas las acciones anteriores afectaran a la desicion de comprar o vender despues.

### **6. Sistema de diagnóstico médico asistido por IA**

Un aparato que recibe todos los analisis del paciente o los captura por si mismo y entrega los resultados despues de unos dias, pero con el apoyo de personal medico.

- **Performance:** Número de elementos anomalos detectados,tiempo en que da resultados, costo del analisis, numero de falsos positivos y falsos negativos, precisión.
- **Environment:** Una sala de hospital
- **Actuators:** Generar un reporte, consumir reportes de otros analisis, solicitar mas analisis, sugerir tratamientos y mostrar alertas de salud.
- **Sensors:** antenas receptoras, bobinas electromagnéticas y detectores fisiológicos


#### AIMA

Estático: Una vez que los sensores capturaron la informacion del paciente, la informacion de entrada no va a cambiar.



### **7. Dron de inspección de infraestructura**

Estoy pensando en un dron capaz de revisar el interior y exterior de un edificio

- **Performance:** Capaz de detectar grietas, daños actuales o detectar elementos que posiblemente daran problemas en el futuro, tamaño de las entradas que necesita para entrar (que pueda entrar por una ventana o puerta), calidad de video o de imagenes. 
- **Environment:** Casas, edificios, ciudades, zonas silvestres, fabricas, tuneles.
- **Actuators:** motores de movimiento, cámara, luz, herramienta para transmitir informacion.
- **Sensors:** Camaras (normal, termica, con mucho zoom, etc), sensor de profundidad, gps, nivel de bateria y microfono.

#### AIMA

Dinámico: hay muchas cosas que pueden cambiar, como ligeras variaciones en el estado del edificio o el clima.


### **8. Agente jugador de ajedrez**

Estoy pensando en las apps de juegos en las que puedes jugar con otras personas en linea.

- **Performance:** cantidad de jugadas correctas (la mejor jugada que se puede hacer), en caso de que solo se puedan hacer malas jugadas, elegir la menos perjudicial, detectar estrategias comunes.
- **Environment:** un celular, tableta, navegador web.
- **Actuators:** las acciones que tiene en el juego, mover fichas y rendirse.
- **Sensors:** detectar las fichas del tablero, las jugadas del oponente

#### AIMA

Observable: Se puede observar todas las fichas en el tablero en todo momento.
