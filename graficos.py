import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')


def generarGrafico(csvPath, outputImg, tituloGrafico):

    try:

        dataFrame = pd.read_csv(csvPath)

        plt.figure(figsize=(12, 6))
        
        plt.plot(dataFrame['Tiempo_s'], dataFrame['Cruda_m'], label='Lectura Cruda ($z_k$)', color='#e74c3c', alpha=0.4, linewidth=1)

        plt.plot(dataFrame['Tiempo_s'], dataFrame['Filtrada_m'], label='Filtro Media Móvil (Ventana 5)', color='#3498db', alpha=0.8, linewidth=1.5)

        plt.plot(dataFrame['Tiempo_s'], dataFrame['Kalman_m'], label='Estimación Filtro de Kalman', color='#2ecc71', linewidth=2)

        plt.title(tituloGrafico, fontsize=14, fontweight='bold', pad=15)

        plt.xlabel('Tiempo (segundos)', fontsize=12, fontweight='bold')

        plt.ylabel('Distancia al Obstáculo (metros)', fontsize=12, fontweight='bold')

        plt.xlim(dataFrame['Tiempo_s'].min(), dataFrame['Tiempo_s'].max())

        plt.ylim(0, dataFrame['Cruda_m'].max() * 1.1)

        plt.legend(loc='upper right', fontsize=11, frameon=True, facecolor='white', edgecolor='none')

        plt.grid(True, linestyle='--', alpha=0.6)

        plt.tight_layout()

        plt.savefig(outputImg, dpi=300)

        plt.close()

        print(f"Grafico generado con exito: {outputImg}")

    except FileNotFoundError:

        print(f"Error: No se encontro el archivo en {csvPath}")


generarGrafico('controlEscenario1/datos_escenario1.csv', 'grafico_escenario1.png', 'Análisis de Señales - Escenario 1 (Entorno Simple)')

generarGrafico('controlEscenario2/datos_escenario2.csv', 'grafico_escenario2.png', 'Análisis de Señales - Escenario 2 (Entorno Complejo)')