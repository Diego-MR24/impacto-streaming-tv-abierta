# **Afectaciones de las Plataformas de Streaming a la Televisión Abierta**

Este proyecto tiene como objetivo analizar cómo el crecimiento de las plataformas de streaming ha afectado la audiencia de la televisión abierta, utilizando datos recopilados a través de encuestas y análisis de comportamiento del consumidor. Los resultados de estos análisis se visualizan mediante gráficos generados con Matplotlib.

## **Estructura del Proyecto**

El proyecto consta de varios scripts que se encargan de cargar los datos, procesarlos y generar las visualizaciones correspondientes. La estructura del código está organizada de la siguiente manera:

- `load_data.py`: Carga de los datos.
- `create_graphs.py`: Generación de gráficos.
- `__init__.py`: Importación de módulos.

## **Instalación**

Para instalar y ejecutar este proyecto, asegúrate de tener Python 3.x instalado en tu sistema. Luego, sigue los siguientes pasos:

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

## **Descripción del Código**

### **1. `load_data.py`**

Este archivo contiene una función para cargar los datos desde un archivo CSV.

```python
import pandas as pd  

def load_data(url):
    data = pd.read_csv(url)
    return data
```

**Función principal**:
- **`load_data(url)`**: Esta función recibe una URL o ruta de archivo como parámetro y carga los datos en formato CSV usando la librería `pandas`. Devuelve un DataFrame con los datos cargados.

### **2. `create_graphs.py`**

Este archivo contiene clases para crear gráficos personalizados usando la librería `matplotlib`.

#### **Clase `BaseGraph`**

La clase `BaseGraph` es la clase base para todos los tipos de gráficos. Establece los parámetros comunes como el tamaño de la figura, los títulos de los ejes y otras configuraciones básicas para el gráfico.

```python
class BaseGraph:
    def __init__(self, data):
        # Inicializa los parámetros del gráfico
        self.data_x = data.get("data-x", [])
        self.data_y = data.get("data-y", [])
        self.figsize = data.get("figsize", [10, 6])
        self.title = data.get("title", "Gráfico")
        self.xlabel = data.get("xlabel", "Eje X")
        self.ylabel = data.get("ylabel", "Eje Y")
        self.colours = data.get("colours", ["b"])
        self.legend = data.get("legend", False)
        self.grid = data.get("grid", False)
        self.label = data.get("label", "")
        self.dpi = data.get("dpi", 100)
        self.tight_layout = data.get("tight_layout", True)
    
    def configure_plot(self):
        # Configura los parámetros comunes del gráfico
        plt.figure(figsize=self.figsize, dpi=self.dpi)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.grid(self.grid)
        plt.legend([self.label] if self.legend else [], loc="best")
        if self.tight_layout:
            plt.tight_layout()
```

#### **Clase `BarGraph`**

La clase `BarGraph` hereda de `BaseGraph` y está diseñada para crear gráficos de barras. Configura los ticks, las etiquetas y el texto de porcentaje en cada barra.

```python
class BarGraph(BaseGraph):
    def __init__(self, data):
        super().__init__(data)
        # Configuración específica de los gráficos de barras
        self.xticks = data.get("xticks", [])
        self.yticks = data.get("yticks", [])
        self.rotation_x = data.get("rotation_x", 0)
        self.rotation_y = data.get("rotation_y", 0)
        self.range_x = data.get("range_x", [0, 10, 1])
        self.range_y = data.get("range_y", [0, 10, 1])
        self.fontsize_x = data.get("fontsize_x", 12)
        self.fontsize_y = data.get("fontsize_y", 12)

    def plot(self):
        # Genera el gráfico de barras
        self.configure_plot()
        plt.xticks(range(self.range_x[0], self.range_x[1], self.range_x[2]), rotation=self.rotation_x, fontsize=self.fontsize_x)
        plt.yticks(range(self.range_y[0], self.range_y[1], self.range_y[2]), rotation=self.rotation_y, fontsize=self.fontsize_y)
        bars = plt.bar(self.data_x, self.data_y, color=self.colours[0])
        total = sum(self.data_y)
        for bar in bars:
            height = bar.get_height()
            percentage = f"{(height / total) * 100:.1f}%" if total > 0 else "0%"
            plt.text(bar.get_x() + bar.get_width() / 2, height, percentage, ha="center", va="bottom", fontsize=10, color="black")
        plt.show()
```

#### **Clase `PieGraph`**

La clase `PieGraph` también hereda de `BaseGraph` y está destinada a crear gráficos circulares (pie charts).

```python
class PieGraph(BaseGraph):
    def __init__(self, data):
        super().__init__(data)
        # Configuración específica de los gráficos circulares
        self.porcentages = data.get("porcentages", [])
        self.labels = data.get("labels", [])
        self.legend_title = data.get("legend_title", " ")
        self.loc = data.get("loc", "upper right")
        self.bbox_to_anchor = data.get("bbox_to_anchor", [1.1, 1])

    def plot(self):
        # Genera el gráfico circular
        plt.figure(figsize=self.figsize, dpi=self.dpi)
        plt.pie(self.porcentages, labels=self.labels, autopct='%1.1f%%', colors=self.colours)
        plt.title(self.title)
        plt.show()
```

### **3. `__init__.py`**

Este archivo inicializa el paquete e importa las funciones y clases principales del proyecto.

```python
from .load_data import load_data
from .create_graphs import BarGraph
from .create_graphs import PieGraph
```

---


## **Uso**

Una vez que los datos han sido cargados con la función `load_data(url)`, puedes crear gráficos de barras o gráficos circulares utilizando las clases `BarGraph` y `PieGraph`, respectivamente. A continuación se muestra un ejemplo básico:

```python
# Cargar datos
df_survey = load_data("ruta/a/archivo.csv")

# Configuración para el gráfico de barras
ages = df_survey["Edad"].value_counts().sort_index()
graph_config = {
        "data-x": ages.index,
        "data-y": ages.values,
        "figsize": [12, 7],
        "title": "Grupos de Edad Representados en la Encuesta",
        "xlabel": "Edad",
        "ylabel": "Frecuencia",
        "range_x": [1, 80, 1],
        "range_y": [1, 32, 2],
        "colours": ["#19324d"]
    }

# Crear y mostrar el gráfico de barras
graph = BarGraph(graph_config)
graph.plot()
```
