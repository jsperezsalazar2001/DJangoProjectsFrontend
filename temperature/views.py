from django.shortcuts import render, HttpResponse
import requests

def temperature(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        dataType = request.GET['dataType']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': dataType, 'value': value}
            response = requests.post('http://127.0.0.1:8000/temperatures/', args)
            # Convierte la respuesta en JSON
            temperature_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/temperatures/')
    # Convierte la respuesta en JSON
    temperatures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "temperature/temperature.html", {'temperatures': temperatures})


def mediciones(request):
    if 'valor' in request.GET:
        fecha = request.GET['fecha']
        origen = request.GET['origen']
        valor = request.GET['valor']
        codigos = request.GET['codigos']
        observacion = request.GET['observacion']

        # Verifica si el value no esta vacio
        if valor:
            # Crea el json para realizar la petición POST al Web Service
            args = {'fecha': fecha, 'origen': origen, 'valor': valor, 'codigos': codigos, 'observacion': observacion}
            print(args)
            response = requests.post('http://127.0.0.1:8000/mediciones/', args)
            # Convierte la respuesta en JSON
            medicion_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/mediciones/')
    # Convierte la respuesta en JSON
    mediciones = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "temperature/mediciones.html", {'mediciones': mediciones})

# Create your views here.
