






| Métrica / Parámetro | Greedy Best-First Search | A* Search |
|:---|:---|:---|
| **Problema** | Timisoara → Eforie | Timisoara → Eforie |
| **Heurística** | Distancia euclidiana a Eforie | Distancia euclidiana a Eforie |
| **Estado** | `success` | `success` |
| **Profundidad (*Depth*)** | 9 carreteras | **8 carreteras** |
| **Costo Total** | 884 km | **805 km** *(Óptimo)* |
| **Nodos Expandidos** | **9 nodos** | 15 nodos |
| **Nodos Generados** | **24 nodos** | 40 nodos |
| **Frontera Máxima** | 6 | 6 |
| **Ruta Encontrada** | Timisoara → Lugoj → Mehadia → Drobeta → Craiova → Pitesti → Bucharest → Urziceni → Hirsova → Eforie | Timisoara → Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest → Urziceni → Hirsova → Eforie |





En tu reporte queda claro:
si Greedy y A* devolvieron el mismo camino o no, y por qué;
qué heurística se usó (tabla AIMA vs. euclidiana);
en al menos un punto de decisión, cómo h(n) (Greedy) frente a f(n) = g(n) + h(n) (A*) explica la ciudad que cada algoritmo expandió.


No devolvieron el mismo camino debido a la manera en que deciden que camino tomar, greedy siempre fue a ciudades que parecieran mas cercanas, mientras que a* ademas de considerar eso toma en cuenta el costo de la ruta. 

Greedy inicia en Timisoara, ve sus opciones, Arad que tiene un h mayor (511)  y Lugoj que tiene un h menor (406) y desde ahi el camino ya es distinto. 

En cambio A* desarrolla varios caminos considerando el camino ya recorrido y la heuristica y conforme se va a expandiendo considera todas las rutas posibles por lo que logra una solucion mejor (optima).

La euristica fue el de distancia euclideana en ambos casos.
