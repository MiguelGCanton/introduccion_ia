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

Parcialmente observable: Puede escuchar la voz, pero solo eso, no hay semantica o algun sensor para medir el contexto en el que se le piden las cosas (comentarios ironicos).
estocástico: Hay ruido en el ambiente por lo que una misma instruccion dada por otra persona o con mucho ruido podria ser ignorada o tener otra respuesta, 
secuencial: Se tiene una platica secuencial donde los detalles anteriores importan(las conversaciones acumulan contexto), 
dinámico: El usuario puede pedir más detalles o cambiar su intruccion mientras aun se trabaja en la primera instruccion.


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

Parcialmente observable: Solo tiene acceso a lo que sus sensores le indican, no puede detectar cambios en la suciedad (nueva suciedad).
Monoagente: Trabaja sola, a no ser que se ayude de alguna camara externa u otra entidad.
Estocástico: El robot podria esparcir suciedad.
Secuencial: Despues de cada accion, se determina la siguiente, si hay bateria, si una zona ya esta limpia, si la siguiente se ensucio.
Dinámico: Siempre hay nuevas fuentes de suciedad como polvo que se acumulan de poco en poco o alguien podria ensuciar una zona ya limpiada.
Continuo: La cantidad de suciedad o cual es mas prioritaria de limpiar conforme al tiempo disponible (bateria) no son valores fijos.

### **4. Vehículo autónomo en ciudad**

Un vehiculo que puede conducirse de manera autonoma pero que tiene que ser tuyo como en el caso de tesla (no como es el waymo que se renta y tiene servicios para contactar a una persona si tienes problemas con el vehiculo)

- **Performance:** número de accidentes, velocidad, tiempo de reaccion ante eventos, tiempo que permanece en la ruta, en el contexto de los autos de bateria y que ejecutar una inteligencia artificial requiere energia, la bateria podria ser un factor, cualquier ley. 
- **Environment:** una ciudad, un sendero en el monte, el estacionamiento de algun lugar o dentro de una casa (porch).
- **Actuators:** volante, freno, camaras, microfonos, gps, luces.
- **Sensors:** camaras, microfono, gps, sensores de temperatura.

#### AIMA

Parcialmente observable: Es imposible ver todos los elementos en la calle siempre hay zonas en reparacion, niebla o algun otro conductor haciendo movimientos impredesibles.
Estocástico: Los cambios en el tráfico, el comportamiento de las personas, el clima y los imprevistos mecánicos son elementos que no se pueden precalcular.
Secuencial: Cualquier acción del vehículo, como elegir un carril, avanzar o frenar, afecta directamente a su posición física futura y desgaste natural.
Dinámico: Cada vez que el vehicula salga van a haber cambios, reglamento, señales, otros vehiculos.
Continuo: Cuanto se gira el volante, que tanto calor hay, cuanto se acelera son valores continuos.


### **5. Agente de trading algorítmico en bolsa**

Una de esos apps de banco que te dicen que oportunidades hay y te envian notificaciones diciendo que esta bajando de precio y te dan los clasicos analisis de tu dinero.

- **Performance:**: dinero ganado, disminucion de perdidas (si detecta que una accion va a bajar mucho la vende lo antes posible), 
- **Environment:** mercados financieros globales; computadoras personales, servidores
- **Actuators:**: funciones para comprar, vender y estimar
- **Sensors:** apis, noticias, historial de precios.

#### AIMA
Parcialmente observable: Por mas informacion que le des, jamas se podra observar todo el mercado para tomar la mejor decision.

Estocástico: Los movimientos del mercado siempre son inciertos e impredecibles.
Secuencial: Cada accion del agente afecta las condiciones a revisar en la proxima compra (liquidez, precio etc.).
Dinámico: El mercado de valores es rápido y cambia continuamente. El precio de un activo puede cambiar entre que lo pides para compra y la compra real de la orden.
Continuo: Los precios de las acciones, los tipos de cambio, las tasas de interés y el tiempo y tiene valores continuos.

### **6. Sistema de diagnóstico médico asistido por IA**

Un aparato que recibe todos los analisis del paciente o los captura por si mismo y entrega los resultados despues de unos dias, pero con el apoyo de personal medico.

- **Performance:** Número de elementos anomalos detectados,tiempo en que da resultados, costo del analisis, numero de falsos positivos y falsos negativos, precisión.
- **Environment:** Una sala de hospital
- **Actuators:** Generar un reporte, consumir reportes de otros analisis, solicitar mas analisis, sugerir tratamientos y mostrar alertas de salud.
- **Sensors:** antenas receptoras, bobinas electromagnéticas y detectores fisiológicos u otras herramientas medicas.



#### AIMA

Parcialmente observable: No se tiene acceso a todo el cuerpo de paciente, solo a unas pequeñas muestras, no se sabe su pasado o habitos.
multi-agente: 
Estocástico: El diagnóstico es sobre datos capturados y los resultados no son siempre certeros, sin contar que la enfermedad sigue haciendo cambios en el paciente.
Secuencial: Hay orden definido en el que se trabaja con cada muestra.
Dinámico: La condición paciente puede empeorar o mejorar mientras el sistema de inteligencia artificial analiza los datos,diagnostica y alerta a doctores.
Continuo: Todos los analisis son numeros continuos, no hay ningun dato fijo.

### **7. Dron de inspección de infraestructura**

Estoy pensando en un dron capaz de revisar el interior y exterior de un edificio

- **Performance:** Capaz de detectar grietas, daños actuales o detectar elementos que posiblemente daran problemas en el futuro, tamaño de las entradas que necesita para entrar (que pueda entrar por una ventana o puerta), calidad de video o de imagenes. 
- **Environment:** Casas, edificios, ciudades, zonas silvestres, fabricas, tuneles.
- **Actuators:** motores de movimiento, cámara, luz, herramienta para transmitir informacion.
- **Sensors:** Camaras (normal, termica, con mucho zoom, etc), sensor de profundidad, gps, nivel de bateria y microfono.

#### AIMA

Parcialmente observable: El dron no conoce el estado completo del edificio o donde podria haber ciertas fallas, al completar todo el chequeo tiene acceso a diferentes partes del edificio en diferentes momentos del dia o de la semana..

Monoagente: Si solo hay un dron, multiagente si hay varios interactuando con el edificio.
Estocástico: Las condiciones de la naturaleza, clima o del edificio podrian cambiar sin aviso.
Secuencial: Cada movimiento que hace, zona que captura o problema en la construccion afecta a su siguiente accion (continuar exploracion, investigar más, avisar).
Dinámico: las condiciones de vuelo como clima o las del dron cambian constantemente.
Continuo: La velocidad de vuelo, altura, cantidad de daño en una pared etc. son valores continuos.


### **8. Agente jugador de ajedrez**

Estoy pensando en las apps de juegos en las que puedes jugar con otras personas en linea.

- **Performance:** cantidad de jugadas correctas (la mejor jugada que se puede hacer), en caso de que solo se puedan hacer malas jugadas, elegir la menos perjudicial, detectar estrategias comunes.
- **Environment:** un celular, tableta, navegador web.
- **Actuators:** las acciones que tiene en el juego, mover fichas y rendirse.
- **Sensors:** detectar las fichas del tablero, las jugadas del oponente

#### AIMA

Totalmente observable: El agente tiene acceso completo al estado del juego y a las posiciones exactas de cada ficha.
Monoagente: eres tu contra el agente de ajedrez.
Determinista: Se sabe cuales son todas las opciones que tiene el otro jugador en todo momento.
Secuencial: Cada jugada cambia las siguientes (la mejor jugada, o si defender o bloquear etc.).
Estático: Solo importa el tablero, no hay cambios en el mundo que importen.
Discreto: Hay un numero limitado de fichas y reglas, ambos son conocidos y fijos.
