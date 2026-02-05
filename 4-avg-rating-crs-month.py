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
        "type": "spline"
    },

    "title": {
        "text": "Promedio de calificaciones por curso y mes"
    },

    "legend": {
        "layout": "vertical",
        "align": "left",
        "verticalAlign": "top",
        "x": 120,
        "y": 70,
        "floating": False,
        "borderWidth": 1,
        "backgroundColor": "var(--highcharts-background-color, #ffffff)"
    },

    "xAxis": {
        "title": {
            "text": "Fecha"
        },
        "plotBands": [
            {
                "from": 2020,
                "to": 2023,
                "color": "rgba(68, 170, 213, .2)"
            }
        ]
    },

    "yAxis": {
        "title": {
            "text": "Calificación"
        }
    },

    "tooltip": {
        "shared": True,
        "headerFormat": "<b>Calificaciones en la fecha de {point.x}</b><br>"
    },

    "credits": {
        "enabled": False
    },

    "plotOptions": {
        "areaspline": {
            "fillOpacity": 0.5
        }
    },

    "series": [
        {
            "name": "Moose",
            "data": [
                38000, 37300, 37892, 38564, 36770, 36026,
                34978, 35657, 35620, 35971, 36409, 36435,
                34643, 34956, 33199, 31136, 30835, 31611,
                30666, 30319, 31766, 29278, 27487, 26007
            ]
        },
        {
            "name": "Deer",
            "data": [
                22534, 23599, 24533, 25195, 25896, 27635,
                29173, 32646, 35686, 37709, 39143, 36829,
                35031, 36202, 35140, 33718, 37773, 42556,
                43820, 46445, 50048, 52804, 49317, 52490
            ]
        }
    ]
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