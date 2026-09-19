

### 1.1 Configuración inicial
* **Número de muestras:** $N = 2000$ (`random_state=7`).
* **Centros originales (`blob_centers`):**

blob_centers = np.array(
    [[ 0.2,  2.3],
     [-1.5 ,  2.3],
     [-2.8,  1.8],
     [-2.8,  2.8],
     [-2.8,  1.3]])
blob_std = np.array([0.4, 0.3, 0.1, 0.1, 0.1])

* **Dispersiones originales (`blob_std`):**
  
blob_std = np.array([0.4, 0.3, 0.1, 0.1, 0.1])

### 1.2 Configuración Modificada
* **Nuevos centros propuestos (`blob_centers`):**
blob_centers = np.array([
    [-4.0,  3.5],   
    [ 4.0,  3.5],   
    [-4.0, -3.5],   
    [ 4.0, -3.5],   
    [ 0.0,  0.0]    
])



* **Nuevas dispersiones propuestas (`blob_std`):**
  blob_std = np.array([0.35, 0.35, 0.35, 0.35, 0.35])

---

## 2. Comparativa Cuantitativa de Métricas

Valores empíricos obtenidos en Google Colab para $k \in \{1, \dots, 9\}$ en ambas configuraciones:

#### Tabla 2.1 — Inercia y Ganancia Original (Géron)

| $k$ | Inercia ($J$) | Ganancia Marginal ($\Delta J$) |
|:---:|:---:|:---:|
| **1** | 3534.84 | — |
| **2** | 1149.89 | 2384.95 |
| **3** | 653.22 | 496.67 |
| **4** | **261.80** | **391.42** |
| **5** | 224.07 | 37.73 |
| **6** | 173.88 | 50.19 |
| **7** | 141.80 | 32.08 |
| **8** | 127.13 | 14.67 |
| **9** | 109.89 | 17.24 |

---

#### Tabla 2.2 — Inercia y Ganancia Modificada (Blobs Separados)

| $k$ | Inercia ($J_{\text{mod}}$) | Ganancia Marginal ($\Delta J_{\text{mod}}$) |
|:---:|:---:|:---:|
| **1** | 45679.54 | — |
| **2** | 31664.02 | 14015.52 |
| **3** | 16628.11 | 15035.91 |
| **4** | 6172.12 | 10455.99 |
| **5** | **479.38** | **5692.74** |
| **6** | 448.53 | **30.85** |
| **7** | 419.67 | 28.86 |
| **8** | 388.67 | 31.00 |
| **9** | 357.08 | 31.59 |
---

## 3. Registro de Figuras Solicitadas (Original vs Modificado)
 revisar carpeta de evidencias

---

## 4. Análisis y Respuestas a las Preguntas Guía

### 1. En los datos de Géron, ¿por qué el codo “prefiere” $k = 4$ si se usaron 5 centros?

El problema de k=4 surge debido a como k means distribuye los centroides, al tener 3 grupos tan cerca (con la misma x) y dos tan lejos, la inercia casi no se ve afectada cuando se evalua con k=4 y k=5, entonces para la grafica del codo se puede observar que para k=4 y k=5 apenas hay cambio.

---

### 2. Con tus blobs separados, ¿el codo y la silueta coinciden en el mismo $k$? ¿Ese $k$ es 5?

Los dispersé de manera perfecta, asi que 
**Sí, ahora los dos coinciden claramente en k = 5**

Observando la grafica de codo_modificado.png se puede notar como la grafica rapidamente disminuye mientras k va aumentando y despues de llegar a k=6 apenas y hay cambio para todos los otros valores.

Por lo que se puede ver el codo muy claramente en k=5.

Revisando la grafica de silueta en la imagen silueta_modificado.png
se puede apreciar como k=5 distribuye mejor las distancias

---

### 3. Si el codo siguiera en 4, ¿qué te falta mover (distancia entre centros vs. `blob_std`)?

Eso significa que hay dos nubes que se encuentran muy cerca y al aumentar k, la inercia apenas cambia, siempre puedo **alejar los centros** para que al haber más distancia, se puedan notar más los cambios en la inercia o **usar un blob_std más pequeño** para que se dispersen menos y esten mucho más cerca del centroide.

---
