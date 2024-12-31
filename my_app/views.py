#django tiene mucho modulos, que podemos utilizar
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here. send files html
def index(request):
    #podemos usar cualquier tipo de instruciones para devolver cualquier cosa
    # html = """
    #     <h2>HTML</h2>
    #     <p>AÑOS HASTA EL 2050!</p>
    #     <ul>
    # """
    # year = 2021
    # while year <= 2050:
    #     if year % 2 == 0:
    #         html += f"<li>{str(year)}</li>"
    #     year +=1
    # html += "</ul>"
    nombre = 'OscarSnva15'
    lenguajes = ['Python','JavaScript','C++','Java']
    #lenguajes = []

    #en lugar de generar a1ui la vista o rederizarla se hace el llamado de un template
    return render(request, 'index.html', {
        'title':'Inicio',
        'nombre':nombre,
        'mi_variable':'soy un dato que esta en la vista',
        'lenguajes':lenguajes
        })#pasar el nombre de la template que queremos cargar

def abouth(request):
    return render(request,'abouth.html')

def proyect(request):
    return render(request,'proyect.html')

def contacs(request):
    return render(request,'contacs.html')