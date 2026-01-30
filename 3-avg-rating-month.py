import justpy as jp
import pandas as pd

#Creamos un dataframe a partir del archivo csv, añadimos el argumento parse_dates y le asignamos una lista con la columna Timestamp para que los 
#valores de dicha columna sean tratados como fechas en vez de strings  
df = pd.read_csv("reviews.csv", parse_dates=["Timestamp"])
#print(df.head())

#Esta vez submuestrearemos todavía más los datos y obtendremos el conteo/promedio de calficaciones por mes

#Extraemos el mes mediante strftime y lo guardamos en una nueva columna llamada month
df["Month"] = df["Timestamp"].dt.strftime('%Y-%m')

#Ahora agrupamos el dataframe resultante por la columna Month y calculamos el promedio de calificaciones
month_avg = df.groupby(["Month"]).mean(numeric_only=True)
print(month_avg.head())

#Creamos un string con comillas triples que contendrá todo el código del gráfico:
chart_def =  {
  "chart": {
    "type": "spline",
    "inverted": False
  },
  "title": {
    "text": 'Atmosphere Temperature by Altitude'
  },

  "xAxis": {
    "reversed": False,
    "title": {
      "enabled": True,
      "text": 'Fecha'
    },
    "labels": {
      "format": '{value}'
    },
    "accessibility": {
      "rangeDescription": 'Range: 0 to 80 km.'
    },
    "maxPadding": 0.05,
    "showLastLabel": True
  },
  "yAxis": {
    "title": {
      "text": 'Calificación Promedio'
    },
    "labels": {
      "format": '{value}'
    },
    "accessibility": {
      "rangeDescription": 'Range: -90°C to 20°C.'
    },
    "lineWidth": 1
  },
  "legend": {
    "enabled": False
  },
  "tooltip": {
    "headerFormat": '<b>{series.name}</b><br/>',
    "pointFormat": '{point.x} : {point.y}'
  },
  "plotOptions": {
    "spline": {
      "marker": {
        "enable": False
      }
    }
  },
  "series": [{
    "name": 'Calificación Promedio'
  }]
}

def create_app() -> jp.QuasarPage:

    wp = jp.QuasarPage() 
    h3 = jp.QDiv(a=wp, text="Análisis de las reseñas del curso", classes="text-h3 text-center q-pa-md text-weight-medium")  
    p1 = jp.QDiv(a=wp, text="Este gráfico representa un análisis de las reseñas del curso", classes = "q-pl-sm")

    #Creamos una instancia de jp.HighCharts, le pasamos en el constructor nuestra página base y el string que contiene la configuración 
    #del gráfico
    hc = jp.HighCharts(a=wp, options=chart_def)
    #Podemos cambiar el título accediendo al atributo .title.text mediante la sintaxis de punto y asignándole un nuevo valor
    hc.options.title.text = "Calificación promedio por mes"

    #HighCharts no reconocerá las fechas como valores válidos para el eje X si las pasamos directamente, por lo que las pasaremos mediante
    #xAxis.categories, no sin antes convertirlas en una lista
    hc.options.xAxis.categories = list(month_avg.index)

    #Esto nos da una lista, con 0 accedemos al único item de la lista que es un diccionario, y posteriormente a la clave "data" de este
    #diccionario. Ahora podremos modificar las coordenadas del gráfico. Como ya definimos el eje X en la línea anterior, ahora pasaremos
    #solamente el Y
    hc.options.series[0].data = list(month_avg["Rating"])

    #print(type(hc.options))
    return wp

jp.justpy(create_app)