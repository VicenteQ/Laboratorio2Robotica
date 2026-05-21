# **Laboratorio 2 Robótica**
---
## **Integrantes:**
- Vicente Nills Quezada
- Yamil Soleman Fernandez
- Sebastián García V
- Ignacio Matus de la Parra
- Vicente Aburto Falcón

## **Asignatura**
- ICI4150-2

---

## 📊 Parámetros de Muestreo y Registro de Datos

Para garantizar la correcta discretización y análisis de las curvas temporales del sistema de control, se extrajeron y analizaron los parámetros fundamentales de muestreo directamente desde el controlador reactivo de Webots, sincronizados mediante el reloj de simulación básica (`robot.getBasicTimeStep()`).

A continuación, se detallan las variables de muestreo utilizadas de manera idéntica en ambos escenarios de prueba:

| Parámetro de Muestreo | Valor Calculado | Unidad | Descripción Técnica |
| :--- | :--- | :--- | :--- |
| **Tiempo de Muestreo ($T_s$)** | `0.032` | Segundos (s) | Intervalo de tiempo discreto fijado por el paso básico de Webots (32 ms) entre iteraciones consecutivas del bucle de control. |
| **Frecuencia de Muestreo ($f_s$)** | `31.25` | Hertz (Hz) | Tasa de refresco del procesamiento digital, calculada mediante la relación formal matemática: $f_s = \frac{1}{T_s}$. |
| **Total de Muestras Registradas** | `5.926` | Muestras | Cantidad total de estados discretos exportados al archivo CSV durante el recorrido completo del robot. |


### 📈 Gráficos de Señales Comparativas (Cruda vs. Filtrada vs. Kalman)

Utilizando los datos analíticos recolectados, se generaron las curvas continuas de distancia métrica con el propósito de evaluar el comportamiento del ruido electrónico del sensor frontal y el rendimiento de mitigación de los algoritmos implementados.

#### Escenario 1: Entorno Simple
![Análisis de Señales - Escenario 1](grafico_escenario1.png)


#### Escenario 2: Entorno Complejo (Pasillos)
![Análisis de Señales - Escenario 2](grafico_escenario2.png)
