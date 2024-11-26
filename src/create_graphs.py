import matplotlib.pyplot as plt

# Clase base para gráficos
class BaseGraph:
    def __init__(self, data):
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

    # Configuración común para todos los gráficos
    def configure_plot(self):
        plt.figure(figsize=self.figsize, dpi=self.dpi)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.grid(self.grid)
        plt.legend([self.label] if self.legend else [], loc="best")
        if self.tight_layout:
            plt.tight_layout()

# Clase para gráficos de barras
class BarGraph(BaseGraph):
    def __init__(self, data):
        super().__init__(data)
        self.xticks = data.get("xticks", [])
        self.yticks = data.get("yticks", [])
        self.rotation_x = data.get("rotation_x", 0)
        self.rotation_y = data.get("rotation_y", 0)
        self.range_x = data.get("range_x", [0, 10, 1])
        self.range_y = data.get("range_y", [0, 10, 1])
        self.fontsize_x = data.get("fontsize_x", 12)
        self.fontsize_y = data.get("fontsize_y", 12)

    def plot(self):
        self.configure_plot()

        # Configuración de los ticks
        plt.xticks(
            range(self.range_x[0], self.range_x[1], self.range_x[2]),
            rotation=self.rotation_x,
            fontsize=self.fontsize_x,
        )
        plt.yticks(
            range(self.range_y[0], self.range_y[1], self.range_y[2]),
            rotation=self.rotation_y,
            fontsize=self.fontsize_y,
        )
        bars = plt.bar(self.data_x, self.data_y, color=self.colours[0])
        total = sum(self.data_y)
        for bar in bars:
            height = bar.get_height()
            percentage = f"{(height / total) * 100:.1f}%" if total > 0 else "0%"
            plt.text(
                bar.get_x() + bar.get_width() / 2, 
                height,  
                percentage,  
                ha="center",  
                va="bottom",  
                fontsize=10,  
                color="black",  
            )
        plt.show()

# Clase para gráficos circulares (Pie Graph)
class PieGraph(BaseGraph):
    def __init__(self, data):
        super().__init__(data)
        self.porcentages = data.get("porcentages", [])
        self.labels = data.get("labels", [])
        self.legend_title = data.get("legend_title", " ")  
        self.loc = data.get("loc", "upper right")
        self.bbox_to_anchor = data.get("bbox_to_anchor", [1.1, 1]) 

    def plot(self):
        plt.figure(figsize=self.figsize, dpi=self.dpi)
        plt.pie(self.porcentages, labels=self.labels, autopct='%1.1f%%', colors=self.colours)
        plt.title(self.title)
        plt.show()


        