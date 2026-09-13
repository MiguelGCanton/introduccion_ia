## Objetivo

Correr ambas notebooks en **Google Colab** con la arquitectura original,
**agregar dos capas** a cada red, volver a entrenar y **comparar** qué cambia
(curva de error/pérdida, velocidad, calidad de la clasificación).

## Archivos a crear / modificar

No modifiques las notebooks originales del repositorio.

1. Sube a Colab una **copia** de cada notebook (o ábrela desde GitHub / Drive).
2. En esas copias, después de la corrida original, deja una **segunda versión**
   de la red con dos capas extra (puedes duplicar celdas para no perder la
   corrida de referencia).

## Requisitos

1. Ejecuta **primero** las dos notebooks **sin cambiar** la topología
   \(4 \times 3 \times 3\). Guarda las gráficas de error/pérdida.
2. Agrega **exactamente dos capas ocultas** a **cada** red. La entrada sigue
   siendo 4 y la **salida sigue siendo 3** (Iris tiene 3 clases). Topología
   pedida:

   \[
   4 \times 3 \times 3 \times 3 \times 3
   \]

   (cuatro capas de 3 neuronas: tres ocultas + salida). Usa **sigmoide** en
   todas las capas, el mismo \(\eta = 0.03\) y las mismas **500 épocas**, para
   que la comparación sea justa.
3. En la notebook **01** debes actualizar **todas** las partes que asumen dos
   capas: tamaños, `init_weights`, el forward de `calculate_error` y el ciclo
   de entrenamiento (propagación **y** retropropagación). No basta con declarar
   dos listas más si el backprop no las usa.
4. En la notebook **02** añade dos `layers.Dense(3, activation="sigmoid", ...)`
   **antes** de la capa de salida. `model.summary()` debe mostrar **4** capas
   `Dense`.
5. El análisis comparativo cubre **cuatro** corridas: original vs. más profunda,
   en implementación a mano **y** en Keras.

## Pasos sugeridos

1. Abre [Google Colab](https://colab.research.google.com/). Sube las notebooks
   (`Archivo` → `Subir notebook`) o ábrelas desde Drive.

2. En Colab, TensorFlow ya está instalado. Ejecuta **Runtime → Run all** en
   cada notebook original. Anota:
   - la curva de error (notebook 01) o de `loss` (notebook 02);
   - el valor de error/pérdida al **final** de las 500 épocas;
   - (notebook 02) el `model.summary()` y una predicción de ejemplo.

3. Duplica las celdas de arquitectura y entrenamiento (o crea una sección
   “red profunda”) y cambia la topología a \(4 \times 3 \times 3 \times 3 \times 3\).

   En Keras el esqueleto queda así (completa nombres y el resto del notebook):

   ```python
   model = keras.Sequential(
     [
       layers.Dense(3, activation="sigmoid", name="layer1", input_shape=(4,)),
       layers.Dense(3, activation="sigmoid", name="layer2"),
       layers.Dense(3, activation="sigmoid", name="layer3"),
       layers.Dense(3, activation="sigmoid", name="layer4"),
     ]
   )
   ```

   En la notebook 01 tendrás `layer1` … `layer4`. El backprop recorre las capas
   **de la salida hacia la entrada**: el \(\delta\) de una capa oculta usa los
   pesos y los \(\delta\) de la capa **siguiente**.

4. Vuelve a entrenar 500 épocas con \(\eta = 0.03\). Guarda las nuevas curvas
   y, si puedes, el tiempo de la celda de entrenamiento.

5. Redacta el análisis comparativo (ver entrega).

## Criterios de aceptación

- Las dos notebooks originales corrieron en **Colab** (no solo en tu máquina).
- Cada red profunda tiene **dos capas extra**; la salida sigue siendo de
  **3** neuronas.
- La notebook 01 actualiza forward **y** backprop (no solo la inicialización).
- Hay evidencias (capturas) de las **cuatro** corridas: curvas y, en Keras,
  `model.summary()` original y profundo.
- El reporte compara implementación a mano vs. Keras **y** red original vs.
  red más profunda; no es un resumen de lo que “debería” pasar sin números.

## Entrega

1. Enlaces de Colab (o archivos `.ipynb`) de las dos notebooks **modificadas**,
   con las corridas originales y las profundas.
2. Capturas: curvas de error/pérdida de las cuatro corridas y los dos
   `model.summary()` de Keras.
3. Un breve reporte (media página a una página) que responda:
   - ¿Bajar más el error al añadir dos capas, o se estancó / empeoró? ¿Igual
     en NumPy y en Keras?
   - ¿Las curvas de la notebook 01 y de Keras se parecen con la misma
     topología? Si no, ¿qué diferencias de implementación podrían explicarlo
     (orden de los datos, inicialización, vectorización, etc.)?
   - Con sigmoides apiladas y MSE, ¿tiene sentido que una red **más profunda**
     no aprenda mejor en Iris? Relaciónalo con lo que viste en las gráficas.
4. Evidencias de haber ejecutado en Colab (captura del entorno Colab o del
   menú Runtime).


links:
04 Multilayer perceptron_modificada.ipynb:
https://colab.research.google.com/drive/1IEzOcxZ_qb8HX8JtiHqOYslHzrKDxzKd?usp=sharing

05 Keras - multilayer perceptron_modificada - iris.ipynb:
https://colab.research.google.com/drive/1_IZGSRB_W05FWQmCAZGknTaoG9W9m0aE?usp=sharing



keras with only two layers

### Model: `sequential_4`

| Layer (type) | Output Shape | Param # |
| :--- | :--- | :---: |
| **layer1** (Dense) | `(None, 3)` | 15 |
| **layer2** (Dense) | `(None, 3)` | 12 |

* **Total params:** 27 (108.00 B)
* **Trainable params:** 27 (108.00 B)
* **Non-trainable params:** 0 (0.00 B)

Keras with four layers

### Model: `sequential_5`

| Layer (type) | Output Shape | Param # |
| :--- | :--- | :---: |
| **layer1** (Dense) | `(None, 3)` | 15 |
| **layer2** (Dense) | `(None, 3)` | 12 |
| **layer3** (Dense) | `(None, 3)` | 12 |
| **layer4** (Dense) | `(None, 3)` | 12 |

* **Total params:** 51 (204.00 B)
* **Trainable params:** 51 (204.00 B)
* **Non-trainable params:** 0 (0.00 B)

Reporte de resultados

Mis resultados son extraños y variables

En el caso de la ejecucion manuel pude observar que la red con solo dos capaz da mejores resultados que la de cuatro para la que a pesar de tener mas filtros termina con un error mayor.


En el caso de keras, se ve un resultado completamente diferente para el caso de dos capaz y de cuatro

en ambos casos la curva de error es distinta a la ejecucion manual,
