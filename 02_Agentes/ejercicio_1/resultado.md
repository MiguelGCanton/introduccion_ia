
   - ¿Cómo cambia el resultado del **agente basado en modelo** si acercas o alejas
     un pit de la casilla inicial?

# Introducción

En mi mapa, yo coloque todos los elementos en el centro de manera que cualquier agente siempre pudiera percibir algo en cualquier cuadricula, excepto la inicial.

![Mapa](.mapa_cargado_correctamente.png)

# Resultados 
Despues de ejecutar todos los comandos descritos en las intrucciones se obtuvieron los siguientes resultados:


| Comando | Resultado | Justificacion |
|-----------|:-----------:|:-----------|
| `02_simple_reflex_agent.py  --config config/mi_cueva_4x4.yaml`| Falla | El modelo intenta moverse a una nueva casilla, detecta una brisa y gira en busca de una nueva ruta, este modelo esta limitado por su programacion if-else la cual al detectar la brisa, inmediatamente ejecuta la accion de moverse pero jamas la accion de avanzar en alguna direccion por lo que el personaje se queda atrapado repitiendo la accion de girar hasta que el programa finaliza |
|`python 03_model_based_agent.py  --config config/mi_cueva_4x4.yaml`| Falla | El modelo siempre se mueve a una casilla que considere segura, pero al moverse, si detecta peligro, entonces el modelo marca la posicion como insegura e intenta buscar un nuevo camino, por lo que intenta buscar una casilla segura para moverse, pero no encuentra ninguna y toma la accion por default hasta que se le gastan las acciones|
|`python 04_goal_based_agent.py   --config config/mi_cueva_4x4.yaml`| Exito | El modelo logra recorrer exitosamente el laberinto |
|`python 05_utility_based_agent.py --config config/mi_cueva_4x4.yaml`| Exito | El modelo logra recorrer exitosamente el laberinto |
|`python 06_learning_agent.py --config config/mi_cueva_4x4.yaml`| Exito | El modelo logra recorrer exitosamente el laberinto |



  - ¿Cómo cambia el resultado del **agente basado en modelo** si acercas o alejas
     un pit de la casilla inicial?

  El modelo inicia su funcionamiento normal, avanza a una casilla y detecta el peligro, al hacer eso ya no agrega elementos al camino seguro y se queda sin lugares que recorrer, por lo que solo realiza su accion por default.
