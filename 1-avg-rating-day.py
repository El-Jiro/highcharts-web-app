import justpy as jp

#Creamos un string con comillas triples que contendrá todo el código del gráfico:
chart = """ {
  chart: {
    type: 'spline',
    inverted: false
  },
  title: {
    text: 'Atmosphere Temperature by Altitude'
  },
  subtitle: {
    text: 'According to the Standard Atmosphere Model'
  },
  xAxis: {
    reversed: false,
    title: {
      enabled: true,
      text: 'Altitude'
    },
    labels: {
      format: '{value} km'
    },
    accessibility: {
      rangeDescription: 'Range: 0 to 80 km.'
    },
    maxPadding: 0.05,
    showLastLabel: true
  },
  yAxis: {
    title: {
      text: 'Temperature'
    },
    labels: {
      format: '{value}°'
    },
    accessibility: {
      rangeDescription: 'Range: -90°C to 20°C.'
    },
    lineWidth: 2
  },
  legend: {
    enabled: false
  },
  tooltip: {
    headerFormat: '<b>{series.name}</b><br/>',
    pointFormat: '{point.x} km: {point.y}°C'
  },
  plotOptions: {
    spline: {
      marker: {
        enable: false
      }
    }
  },
  series: [{
    name: 'Temperature',
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

    #En un caso de uso real tendríamos un array de valores para el eje X y otro para el eje Y, de esta forma:
    x = [3, 6, 8]
    y= [4, 7, 9]
    #Esto nos da una lista, con 0 accedemos al único item de la lista que es un diccionario, y posteriromente a la clave "data" de este
    #diccionario. Ahora podremos modificar las coordenadas del gráfico, usamos zip para unir los elementos de x e y en pares. Deberemos
    #convertir el objeto en una lista antes de asignarlo
    hc.options.series[0].data = list(zip(x, y))

    #print(type(hc.options))
    return wp

jp.justpy(create_app)