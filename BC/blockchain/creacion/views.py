from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm, FormActualizar
from .servicios import crear_bloque, validar_bc


def procesar(request):
    return render(request, 'creacion/crear.html')


def vista_val(request):
    return render(request, 'creacion/validacion.html')


def subir(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['file']
            variables = crear_bloque(archivo)
            hashArchivo = variables[0]
            hashBloque = variables[1]
            timestamp = variables[2]
            numId = variables[3]
            return render(request, 'creacion/exito.html', {'hashArchivo': hashArchivo, 'hashBloque': hashBloque, 'timestamp': timestamp, 'numId': numId})
        else:
            form = UploadFileForm()
        return render(request, 'creacion/nanay.html', {'form': form})


def validar(request):
    if request.method == 'POST':
        form = FormActualizar(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['file']
            index = form.cleaned_data['index']
            variables = validar_bc(index, archivo)
            condicion = variables[0]
            hashArchivo = variables[1]
            mensajeTrue = "El archivo no ha sido modificado."
            mensajeFalse = "El archivo fue modificado."
            if condicion:
                hashBloque = variables[2]
                return render(request, 'creacion/validado.html', {'hashArchivo': hashArchivo, 'hashBloque': hashBloque, "mensaje": mensajeTrue, "condicion": condicion})
            return render(request, 'creacion/validado.html', {'hashArchivo' : hashArchivo, "mensaje" : mensajeFalse, 'condicion': condicion})
        else:
            form = UploadFileForm()
        return render (request, 'creacion/nanay.html', {'form' : form})
