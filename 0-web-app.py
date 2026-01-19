import justpy as jp

"""
Para crear una web app con justpy, primeramente deberemos definir una función que cree una instancia de jp.QuasarPage, este objeto 
representará la página web base. Posteriormente, iremos añadiendo elementos a dicha página, tales como encabezados, párrafos, tablas,
imágenes, etc, y, por último, retornamos el objeto QuasarPage . Esta función no recibe parámetros
"""

def create_app() -> jp.QuasarPage:

    #llamaremos a nuestra instancia wp, que son las siglas de web page
    wp = jp.QuasarPage() 
    #Para empezar a añadir elementos, usamos el método Qdiv, al cual le pasaremos mínimamente dos argumentos de palabra clave con el nombre
    #que queramos, el primero es el objeto padre (wp), y el segundo el texto a mostrar
    h1 = jp.QDiv(a=wp, text= "Análisis de las Calificaciones de los Cursos")
    p1 = jp.QDiv(a=wp, text="Estos gráficos representan el análisis de las calificaciones de los cursos")

    #Definimos wp como valor de retorno de la función
    return wp

"""
Para desplegar la página y mostrarla en el navegador, usamos el método justpy de jp, al cual le pasamos la referencia de nuestra función
create_app como argumento
"""
jp.justpy(create_app)