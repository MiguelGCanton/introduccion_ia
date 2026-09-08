## Objetivo

Elegir una ruta distinta de Arad → Bucharest, correr BFS, UCS, DFS, DLS e IDS,
y analizar diferencias de camino, costo, profundidad y nodos expandidos.

## Archivos a crear / modificar

No modifiques el código de `romania/` ni de `search/`.

Trabaja solo con los scripts `02`–`06` y los flags `--from-city` y `--to`
(y `--limit` en DLS).

## Requisitos de la instancia

1. Elige un origen y un destino **distintos** de la pareja por defecto
   (`Arad`, `Bucharest`). Ambos deben existir en el mapa (ver
   `01_romania_map.py` o `romania/map.py`).
2. Debe existir **al menos un camino** entre ellos (el grafo no está
   completamente conectado: por ejemplo, Neamt solo llega vía Iasi).
3. Usa la **misma** pareja origen–destino en los cinco algoritmos.
4. Para DLS, prueba **al menos dos** valores de `--limit`: uno que produzca
   `cutoff` y otro que encuentre solución (si existe a esa profundidad).

Las rutas se especifican más abajo

| # | Algoritmo | Configuración | Estado | Ruta | Profundidad | Costo | Expandidos | Generados | Frontera Máx. |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | **Breadth-first search (BFS)** | — | `success` | **Ruta A** | 4 | 535 km | 10 | 22 | 5 |
| **2** | **Uniform-cost search (UCS)** | — | `success` | **Ruta B** | 5 | 503 km | 14 | 34 | 5 |
| **3** | **Depth-first search (DFS)** | — | `success` | **Ruta A** | 4 | 535 km | 4 | 14 | 7 |
| **4** | **Depth-limited search (DLS)** | `limit = 3` | `cutoff` | — | — | — | 9 | 21 | 6 |
| **5** | **Depth-limited search (DLS)** | `limit = 5` | `success` | **Ruta A** | 4 | 535 km | 4 | 6 | 8 |
| **6** | **Iterative deepening (IDS)** | `limit = 4` | `success` | **Ruta A** | 4 | 535 km | 18 | 44 | 8 |

**Detalle de Rutas:**
* **Ruta A (4 saltos / 535 km):** `Urziceni → Bucharest → Fagaras → Sibiu → Arad`
* **Ruta B (5 saltos / 503 km):** `Urziceni → Bucharest → Pitesti → Rimnicu Vilcea → Sibiu → Arad`

```text
┌──────────────────────┐
│  Urziceni  (Inicio)  │
└──────────┬───────────┘
           │ 85 km
┌──────────▼───────────┐
│      Bucharest       │
└──────┬───────────┬───┘
       │           │
211 km │           │ 101 km
(BFS)  │           │ (UCS)
       │           ▼
       │     ┌───────────┐
       │     │  Pitesti  │
       │     └─────┬─────┘
       │           │ 97 km
       ▼           ▼
 ┌───────────┐   ┌────────────────┐
 │  Fagaras  │   │ Rimnicu Vilcea │
 └─────┬─────┘   └─────────┬──────┘
       │ 99 km             │ 80 km
       │                   │
       └───────► ┌─────────▼─┐
                 │   Sibiu   │
                 └─────┬─────┘
                       │ 140 km
                 ┌─────▼──────────┐
                 │  Arad  (Meta)  │
                 └────────────────┘
```


# Reporte

Para este trabajo elegi la combinacion que viaja de Urziceni a Arad.

En el caso de BFS y UCS, no se tuvo el mismo camino

Debigo a que BFS tiene un orden fifo estricto que cumplir asi que primero expande el nodo con Fagaras (211km), en cambio UCS siempre expande el nodo que tenga el menor costo primero, por lo que expande Pitesti (101km).  

En este caso BFS y IDS coincidieron en profundidad,aunque son completamente diferentes en todos los otros resultados

La diferencia entre DLS con los limites diferentes fue impresionante, con el limite 3 genero muchos más nodos que la version con un mayor limite, debe ser a la posicion de la respuesta, ya que con limite 3 no pudo profundizar lo suficiente, mientras que tuvo que generar todos los nodos a su alcance y en limite 5 se encuentra la solucion mucho antes y ya no es necesario tanto trabajo.
