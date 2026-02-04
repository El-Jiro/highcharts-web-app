import justpy as jp
import pandas as pd

#Creamos un dataframe a partir del archivo csv, añadimos el argumento parse_dates y le asignamos una lista con la columna Timestamp para que los 
#valores de dicha columna sean tratados como fechas en vez de strings  
df = pd.read_csv("reviews.csv", parse_dates=["Timestamp"])

#Extraemos el mes mediante strftime y lo guardamos en una nueva columna llamada month
df["Month"] = df["Timestamp"].dt.strftime('%Y-%m')

#Ahora agrupamos el dataframe resultante por la columna Month y calculamos el promedio de calificaciones
month_avg = df.groupby(["Month"]).mean(numeric_only=True)
print(month_avg.head())

#Creamos un diccionario que contendrá todo el código del gráfico:
chart_def = {
    "chart": {
        "type": "spline"
    },

    "title": {
        "text": "Moose and deer hunting in Norway, 2000 - 2024"
    },

    "subtitle": {
        "text": 'Source: <a href="https://www.ssb.no/jord-skog-jakt-og-fiskeri/jakt" target="_blank">SSB</a>'
    },

    "legend": {
        "layout": "vertical",
        "align": "left",
        "verticalAlign": "top",
        "x": 120,
        "y": 70,
        "floating": True,
        "borderWidth": 1,
        "backgroundColor": "var(--highcharts-background-color, #ffffff)"
    },

    "xAxis": {
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
            "text": "Quantity"
        }
    },

    "tooltip": {
        "shared": True,
        "headerFormat": "<b>Hunting season starting autumn {point.x}</b><br>"
    },

    "credits": {
        "enabled": False
    },

    "plotOptions": {
        "series": {
            "pointStart": 2000
        },
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

    #print(type(hc.options))
    return wp

jp.justpy(create_app)