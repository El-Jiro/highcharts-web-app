import justpy as jp
import pandas as pd

#Creamos un dataframe a partir del archivo csv, añadimos el argumento parse_dates y le asignamos una lista con la columna Timestamp para que los 
#valores de dicha columna sean tratados como fechas en vez de strings  
df = pd.read_csv("reviews.csv", parse_dates=["Timestamp"])

#Extraemos el mes mediante strftime y lo guardamos en una nueva columna llamada month
df["Month"] = df["Timestamp"].dt.strftime('%Y-%m')
#print(df["Month"])

#Agrupamos por curso y mes, calculamos el promedio y guardamos todo en la variable month_avg_crs. La estructura del dataframe resultante 
#es algo confusa, básicamente tenemos un grupo de filas en cada mes, por lo que aplicaremos el método unstack  para hacerlo más claro y 
#legible, ahora cada columna es un curso y cada fila un mes.
month_avg_crs = df.groupby(["Month", "Course Name"]).mean(numeric_only=True).unstack()
#print(month_avg_crs.head())

#print(month_avg_crs.index)
#Creamos un diccionario que contendrá todo el código del gráfico:

chart_def = {

    "chart": {
        "type": "streamgraph",
        "zooming": {
            "type": "x"
        }
    },

     "tooltip": {
        "shared": True,
        "valueDecimals": 1,
    },

    "title": {
        "floating": True,
        "align": "center",
        "text": "Promedio de calificaciones por curso y mes"
    },

    "xAxis": {

        "maxPadding": 0,
        "type": "category",
        "crosshair": True,
        "categories": [
        ],

        "title": {
            "text": "Fecha"
        },
        "labels": {
            "align": "left",
            "reserveSpace": True,
        },
        "lineWidth": 0,
        "tickWidth": 0
    },

    "yAxis": {
        "visible": False,
        "startOnTick": False,
        "endOnTick": False,
        "minPadding": 0.1,
        "maxPadding": 0.15
    },

    "legend": {
        "enabled": False
    },

    "annotations": [{
        "labels": [
            {
                "point": {"x": 5.5, "xAxis": 0, "y": 30, "yAxis": 0},
                "text": "Cancelled<br>during<br>World War II"
            },
            {
                "point": {"x": 18, "xAxis": 0, "y": 90, "yAxis": 0},
                "text": "Soviet Union fell,<br>Germany united"
            },
            {
                "point": {"x": 24.25, "xAxis": 0, "y": 140, "yAxis": 0},
                "text": "Russia banned from<br>the Olympic Games<br> in 2017"
            }
        ],
        "labelOptions": {
            "backgroundColor": "rgba(255,255,255,0.5)",
            "borderColor": "silver"
        }
    }],

    "plotOptions": {
        "series": {
            "label": {
                "enable": True,
                "minFontSize": 5,
                "maxFontSize": 15,
                "allowOverlap": False,
                "style": {
                    "color": "rgba(255,255,255,0.75)",
                    "fontweight": "bold",
                    "textOutline": None
                }
            },
            "accessibility": {
                "exposeAsGroupOnly": True
            }
        }
    },

    "series": [],

    "exporting": {
        "sourceWidth": 800,
        "sourceHeight": 600
    }
}


def create_app() -> jp.QuasarPage:

    wp = jp.QuasarPage() 
    h3 = jp.QDiv(a=wp, text="Análisis de las reseñas del curso", classes="text-h3 text-center q-pa-md text-weight-medium")  
    p1 = jp.QDiv(a=wp, text="Este gráfico representa un análisis de las reseñas del curso", classes = "q-pl-sm")

    #Creamos una instancia de jp.HighCharts, le pasamos en el constructor nuestra página base y el string que contiene la configuración 
    #del gráfico
    hc = jp.HighCharts(a=wp, options=chart_def)

    #Colocamos la información de nuestro index en el eje X
    hc.options.xAxis.categories = list(month_avg_crs.index)
    
    #Rotamos los labels para que no se amontonen
    hc.options.xAxis.labels = {
    "rotation": -60
    }
    
    #Forzamos a mostrar todas las etiquetas
    hc.options.xAxis.min = 0
    hc.options.xAxis.max = 39

    #Creamos una lista para almacenar los valores de los distintos cursos, y usamos la comprensión de listas para reemplazar v1
    #por el nombre de cada columna iterando sobre la lista de columnas. Para obtener los datos de cada columna usamos una comprensión 
    #anidada, iterando sobre las filas de dicha columna
    hc_data = [{"name": v1[1], "data": [v2 for v2 in month_avg_crs[v1]]} for v1 in month_avg_crs.columns]

    print(hc_data)
    
    #Asignamos la lista al atributo series de hc
    hc.options.series = hc_data

    return wp

jp.justpy(create_app)