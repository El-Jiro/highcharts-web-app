import justpy as jp

"""
Para crear una web app con justpy, primeramente deberemos definir una función que cree una instancia de jp.QuasarPage, este objeto 
representará la página web base. Posteriormente, iremos añadiendo elementos a dicha página, tales como encabezados, párrafos, tablas,
imágenes, etc, y, por último, retornamos el objeto QuasarPage. Esta función no recibe parámetros
"""

#Creamos un diccionario con la definición del gráfico
chart_def = {

    "chart": {
        "type": "pie",
        "zooming": {
            "type": "xy"
        },
        "panning": {
            "enabled": True,
            "type": "xy"
        },
        "panKey": "shift"
    },

    "title": {
        "text": "Egg Yolk Composition"
    },

    "tooltip": {
        "valueSuffix": "%"
    },

    "subtitle": {
        "text": (
            'Source:<a href="https://www.mdpi.com/2072-6643/11/3/684/htm" '
            'target="_default">MDPI</a>'
        )
    },

    "plotOptions": {
        "pie": {
            "allowPointSelect": True,
            "cursor": "pointer",
            "dataLabels": [
                {
                    "enabled": True,
                    "distance": 20
                },
                {
                    "enabled": True,
                    "distance": -40,
                    "format": "{point.percentage:.1f}%",
                    "style": {
                        "fontSize": "1.2em",
                        "textOutline": "none",
                        "opacity": 0.7
                    },
                    "filter": {
                        "operator": ">",
                        "property": "percentage",
                        "value": 10
                    }
                }
            ]
        }
    },

    "series": [
        {
            "name": "Percentage",
            "colorByPoint": True,
            "data": [
                {
                    "name": "Water",
                    "y": 55.02
                },
                {
                    "name": "Fat",
                    "sliced": True,
                    "selected": True,
                    "y": 26.71
                },
                {
                    "name": "Carbohydrates",
                    "y": 1.09
                },
                {
                    "name": "Protein",
                    "y": 15.5
                },
                {
                    "name": "Ash",
                    "y": 1.68
                }
            ]
        }
    ]
}


def create_app() -> jp.QuasarPage:

    #llamaremos a nuestra instancia wp, que son las siglas de web page
    wp = jp.QuasarPage() 
    #Para empezar a añadir elementos, usamos el método Qdiv, al cual le pasaremos mínimamente dos argumentos de palabra clave con el nombre
    #que queramos, el primero es el objeto padre (wp), y el segundo el texto a mostrar. Para añadir estilos usamos el argumento de classes 
    #y pasamos los nombres de las clases css de Quasar, como por ejemplo text-h1. Podemos añadir varias clases separadas por espacios
    h3 = jp.QDiv(a=wp, text= "Análisis de las Calificaciones de los Cursos", classes="text-h3 text-center q-pa-md text-weight-medium")  
    p1 = jp.QDiv(a=wp, text="Estos gráficos representan el análisis de las calificaciones de los cursos")

       #Creamos una instancia de jp.HighCharts, le pasamos en el constructor nuestra página base y el string que contiene la configuración 
    #del gráfico
    hc = jp.HighCharts(a=wp, options=chart_def)

    #Definimos wp como valor de retorno de la función
    return wp

"""
Para desplegar la página y mostrarla en el navegador, usamos el método justpy de jp, al cual le pasamos la referencia de nuestra función
create_app como argumento
"""
jp.justpy(create_app)