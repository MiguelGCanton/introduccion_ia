3. Un breve reporte (media página) que responda:
   - ¿Qué agentes lograron salir con el oro en tu mapa y cuáles no?
   - ¿Por qué el **agente de reflejo simple** falla (o tiene suerte) en tu diseño?
   - ¿Cómo cambia el resultado del **agente basado en modelo** si acercas o alejas
     un pit de la casilla inicial?

# Introducción

En mi mapa, yo coloque todos los elementos en el centro de manera que cualquier agente siempre pudiera percibir algo en cualquier cuadricula, excepto la inicial.

![Mapa](.mapa_cargado_correctamente.png)

# Resultados 
Despues de ejecutar todos los comandos descritos en las intrucciones se obtuvieron los siguientes resultados:


| Comando | Resultado | Justificacion |
|-----------|:-----------:|:-----------|
| `python 01_wumpus_world.py  --config config/mi_cueva_4x4.yaml`| Falla | El modelo intenta moverse a una nueva casilla, detecta una brisa y gira en busca de una nueva ruta, este modelo esta limitado por su programacion if-else que al detectar la brisa inmediatamente ejecuta la accion de moverse pero jamas la accion de avanzar en alguna direccion por lo que el personaje se queda atrapado repitiendo la accion de girar hasta que el programa finaliza |
|`python 03_model_based_agent.py  --config config/mi_cueva_4x4.yaml`| Falla | El modelo se mueve a una casilla que segura, pero al moverse inmediatamente detecta peligro, el modelo no tiene la opcion de regresar por lo que intenta buscar una casilla siguiente a la cual moverse y toma la accion por default hasta que se le gastan las acciones|
|` python 05_utility_based_agent.py --config config/mi_cueva_4x4.yaml`| Exito | El modelo logra recorrer exitosamente el laberinto |
|` python 06_learning_agent.py --config config/mi_cueva_4x4.yaml`| Exito | El modelo logra recorrer exitosamente el laberinto |
