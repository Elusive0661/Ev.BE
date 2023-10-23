from django.shortcuts import render

# Create your views here.
def app2(request):
    return render(request,'evT\EvTemp.html')

def wlfmster(request):
    data={
        "titulo":"Wlfmster",
        "imagen":"imagenes/wlfmster.png",
        "dato1":"Monster Siren Records",
        "dato2":"3:35",
    }
    return render(request, 'evT\EvTemp.html', data)

def oldYellowBricks(request):
    data={
        "titulo":"Old Yellow Bricks",
        "imagen":"imagenes/oldYellowBricks.jpg",
        "dato1":"Artic Monkeys",
        "dato2":"3:14",
    }
    return render(request, 'evT\EvTemp.html', data)

def IGИIS(request):
    data={
        "titulo":"IGИIS",
        "imagen":"imagenes/ignis.jpg",
        "dato1":"Uroboros",
        "dato2":"4:24",
        }
    return render(request, 'evT\EvTemp.html', data)