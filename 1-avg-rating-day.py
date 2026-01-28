import justpy as jp
import pandas as pd

#Creamos un dataframe a partir del archivo csv, añadimos el argumento parse_dates y le asignamos una lista con la columna Timestamp para que los 
#valores de dicha columna sean tratados como fechas en vez de strings  
df = pd.read_csv("reviews.csv", parse_dates = ["Timestamp"])
#print(df.head())

"""
Antes de graficar el promedio de las calificaciones por día, deberemos procesar los datos para convertirlos en información, primeramente 
añadimos aldataframe una nueva columna llamada Day, la cual tendrá como valor únicamente la parte de fecha de la columna Timestamp.
"""

df["Day"] = df["Timestamp"].dt.date

#Aplicamos el método groupby, el cual recibe como argumento el nombre de la columna entre corchetes, le concatenamos el método mean que 
#debe recibir el argumento de palabra clave numeric_only con el valor True, de otra manera nos saltará un TypeError, y guardamos el 
#resultado en day_avg
day_avg = df.groupby(["Day"]).mean(numeric_only= True)
print(day_avg.head())

#Creamos un string con comillas triples que contendrá todo el código del gráfico:
chart = """ {
  chart: {
    type: 'spline',
    inverted: false
  },
  title: {
    text: 'Atmosphere Temperature by Altitude'
  },

  xAxis: {
    reversed: false,
    title: {
      enabled: true,
      text: 'Date'
    },
    labels: {
      format: '{value}'
    },
    accessibility: {
      rangeDescription: 'Range: 0 to 80 km.'
    },
    maxPadding: 0.05,
    showLastLabel: true
  },
  yAxis: {
    title: {
      text: 'Average Rating'
    },
    labels: {
      format: '{value}'
    },
    accessibility: {
      rangeDescription: 'Range: -90°C to 20°C.'
    },
    lineWidth: 0.5
  },
  legend: {
    enabled: false
  },
  tooltip: {
    headerFormat: '<b>{series.name}</b><br/>',
    pointFormat: '{point.x} : {point.y}'
  },
  plotOptions: {
    spline: {
      marker: {
        enable: false
      }
    }
  },
  series: [{
    name: 'Average Rating',
    data: [
      [0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
      [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]
    ]
  }]
}
"""


def create_app() -> jp.QuasarPage:

    wp = jp.QuasarPage() 
    h3 = jp.QDiv(a=wp, text= "Analysis of Course Reviews", classes="text-h3 text-center q-pa-md text-weight-medium")  
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis", classes = "q-pl-sm")

    #Creaamos una instancia de jp.HighCharts, le pasamos en el constructor nuestra página base y el string que contiene las opciones del
    #gráfico
    hc = jp.HighCharts(a=wp, options = chart)
    #Podemos cambiar el título accediendo al atributo .title.text mediante la sintaxis de punto y asignándole un nuevo valor
    hc.options.title.text = "Average Rating by Day"

    #HighCharts no reconocerá las fechas como valores válidos para el eje X si las pasamos directamente, por lo que las pasaremos mediante
    #xAxis.categories, no sin antes convertirlas en una lista
    hc.options.xAxis.categories = list(day_avg.index)

    #Esto nos da una lista, con 0 accedemos al único item de la lista que es un diccionario, y posteriormente a la clave "data" de este
    #diccionario. Ahora podremos modificar las coordenadas del gráfico. Como ya definimos el eje X en la línea anterior, ahora pasaremos
    #solamente el Y
    hc.options.series[0].data = list(day_avg["Rating"])

    #print(type(hc.options))
    return wp

jp.justpy(create_app)