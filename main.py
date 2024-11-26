from src import load_data
from src import BarGraph, PieGraph 

df_survey = load_data("data/processed/survey_clean_data.csv")
#print(df_survey.head())
#print(df_survey.describe())

# Gráficas de barras : Edades
ages = df_survey["Edad"].value_counts().sort_index()
graph_config = {
        "data-x": ages.index,
        "data-y": ages.values,
        "figsize": [12, 7],
        "title": "Grupos de Edad Representados en la Encuesta",
        "xlabel": "Edad",
        "ylabel": "Frecuencia",
        "range_x": [1,80,1],
        "range_y":[1,32,2],
        "colours": ["#19324d"]
    }

graph = BarGraph(graph_config)
graph.plot()

# Gráfica circular : Porcentaje de generos
gender_percentage = df_survey["Genero"].value_counts()

graph_config = {
    "figsize": [12, 7],
    "title": "Proporción de Géneros entre los Encuestados",
    "colours": ["#66b3ff", "#f44","#ff8c1a"],
    "porcentages": gender_percentage,  
    "labels": ["Hombre", "Mujer","Otro"], 
    "legend_title": "Proporción de Géneros entre los Encuestados",  
    "loc": "upper right",
    "bbox_to_anchor": [1.1, 1],
}

graph = PieGraph(graph_config)
graph.plot()

# Gráfica circular : Personas que si usan plataformas de streaming
use_platforms_streaming = df_survey["Usa plataformas de streaming"].value_counts()
graph_config = {
    "figsize": [12, 7],
    "title": "Usuarios de Plataformas de Streaming en Relación al Total de Encuestados",
    "colours": ["#2b5988", "#ff8c1a"],
    "porcentages": use_platforms_streaming,  
    "labels": ["Si", "No"], 
    "loc": "upper right",
    "bbox_to_anchor": [1.2, .9],
}

graph = PieGraph(graph_config)
graph.plot()

# Gráfica circular : Frecuencia del uso de las plataformas streaming 
frequency_use_ps = df_survey["Frecuencia de uso de plataformas de streaming"].value_counts()
graph_config = {
    "figsize": [12, 7],
    "title": "Frecuencia de Uso de Plataformas de Streaming",
    "colours": ["#004d4d", "#008080","#00cccc"],
    "porcentages": frequency_use_ps,  
    "labels": ["Diario", "Cada semana", "Cada mes"], 
    "loc": "upper right",
    "bbox_to_anchor": [1.2, .9],
}
graph = PieGraph(graph_config)
graph.plot()

# Gráfica circular : Frecuencia del uso de TV abierta
frequency_use_TV = df_survey["Frecuencia de uso de TV abierta"].value_counts()
graph_config = {
    "figsize": [12, 7],
    "title": "Frecuencia sobre el uso de TV abierta",
    "colours": ["#004d4d", "#008080","#00cccc"],
    "porcentages": frequency_use_ps,  
    "labels": ["Nunca", "Varias veces a la semana", "Diario"], 
    "loc": "upper right",
    "bbox_to_anchor": [1.2, .9],
}
graph = PieGraph(graph_config)
graph.plot()

# Gráfica de barras : Conteo de plataformas favoritas 
df_survey["Plataformas de streaming favorita"] = df_survey["Plataformas de streaming favorita"].apply(lambda x: x.split(", "))
df_survey_exploded = df_survey["Plataformas de streaming favorita"].explode()
favorites_platforms = df_survey_exploded.value_counts().sort_values(ascending=False)

graph_config = {
        "data-x": favorites_platforms.index,
        "data-y": favorites_platforms.values,
        "figsize": [12, 7],
        "title": "Preferencia por Plataformas de Streaming",
        "xlabel": "Plataformas",
        "ylabel": "Plataformas de Streaming",
        "range_x": [0,6,1],
        "range_y":[1,80,2],
        "colours": ["#19324d"]
    }

graph = BarGraph(graph_config)
graph.plot()

# Gráfica de barras : Tipos de contenido que consumes
 
df_survey["Tipo de contenido que consume"] = df_survey["Tipo de contenido que consume"].apply(lambda x: x.split(", "))
df_survey_exploded = df_survey["Tipo de contenido que consume"].explode()
content_type_frequency = df_survey_exploded.value_counts().sort_values(ascending=False)

graph_config = {
        "data-x": content_type_frequency.index,
        "data-y": content_type_frequency.values,
        "figsize": [12, 7],
        "title": "Tipos de Contenido Consumido",
        "xlabel": "Tipo de contenido",
        "ylabel": "Frecuencia",
        "range_x": [0,6,1], 
        "range_y":[1,80,2],
        "colours": ["#19324d"]
    }

graph = BarGraph(graph_config)
graph.plot()

# Gráfica de barras : Factores que se consideran al elegir una plataforma de streaming  
df_survey["Caracteristicas mas importantes"] = df_survey["Caracteristicas mas importantes"].apply(lambda x: x.split(", "))
df_survey_exploded = df_survey["Caracteristicas mas importantes"].explode()
important_factors = df_survey_exploded.value_counts().sort_values(ascending=False)

graph_config = {
        "data-x": important_factors.index,
        "data-y": important_factors.values,
        "figsize": [12, 7],
        "title": "Criterios para Seleccionar una Plataforma de Streaming",
        "xlabel": "Factores",
        "ylabel": "Frecuencia",
        "range_x": [0,6,1], 
        "range_y":[0,80,2],
        "colours": ["#19324d"]
    }

graph = BarGraph(graph_config)
graph.plot()