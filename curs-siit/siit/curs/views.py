from django.shortcuts import render
from django.utils import timezone

from .models import Student, Curs

# Create your views here.
def hello_world(request):
    def my_func():
        return "salutare"

    class MyObject:
        proprietate = 1

        def __init__(self, id):
            self.id = id

    obj = MyObject(10)

    context = {
        'time': timezone.now(),
        'string': "Salut",
        'lista': [1,2,3],
        'dictionar': {
            'unu': 1,
            'doi': 2,
            'dict2': {
                'cheie': 'valoare'
            },
        
        },
        'functie': my_func,
        'obiect': obj,
        #'cheie': 'Valoare'
    }
    return render(request, "homepage.html", context)


def show_students(request):
    try:
        an_cerut = int(request.GET['an'])
        lista_studenti = Student.objects.filter(an__lte=an_cerut,)
    except KeyError:
        lista_studenti = Student.objects.all()

    try:
        nume = request.GET['nume']
        lista_studenti = lista_studenti.filter(nume__startswith=nume)
    except KeyError:
        pass
    
    promoveaza = request.GET.get("promoveaza")
    if promoveaza is not None:
        lista_studenti.update(an=2)
        # Student.objects.update(an=2) - va modifica toate intrarile din DB
    sterge = request.GET.get("sterge")
    if sterge is not None:
        print(sterge)
        lista_studenti.delete()
        #  Student.objects.delete() - va sterge toate intrarile
    lista_studenti = lista_studenti.order_by("-nume").prefetch_related("cursuri")

    #lista_studenti = Student.objects.boboci()

    context = {
        'studenti': lista_studenti,
        'mesaj': 'Salut'
    }

    return render(request, "lists/list_students.html", context)


def show_curs(request):
    # import pdb; pdb.set_trace()
    # import ipdb; ipdb.set_trace() # pip install ipdb
    id_curs = int(request.GET.get('curs', 0))
    curs = Curs.objects.get(id=id_curs)
    studenti = curs.student_set.all()
    context = {
        'studenti': studenti
    }
    return render(request, "lists/list_curs.html", context)