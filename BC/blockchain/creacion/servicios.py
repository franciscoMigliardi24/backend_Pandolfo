import docx
import hashlib
import datetime
from .models import Bloque

def hash_archivo (archivo):
    doc = docx.Document(archivo)
    texto = ''
    hasheador = hashlib.sha256()
    for parr in doc.paragraphs:
        parr.text
        texto+=parr.text
        hasheador.update(texto.encode('utf-8'))
    hash_archivo = hasheador.hexdigest()
    return str(hash_archivo)

def string_fecha():
    fecha_actual = datetime.datetime.now()
    fecha_hora = fecha_actual.strftime("%Y-%m-%d %H:%M:%S.%f")
    return str(fecha_actual)

def hash_bloque_anterior():
    index = len(Bloque.objects.all())-1
    hash_a = Bloque.objects.all()[index].hashActual
    return str(hash_a)

def crear_bloque(archivo):
    bloque = Bloque()
    bloque.timestamp = string_fecha()
    bloque.archivo = hash_archivo(archivo)
    bloque.hashAnterior = hash_bloque_anterior()
    bloque.hashActual = calcular_hash(bloque)
    bloque.save()
    return bloque.archivo, bloque.hashActual, bloque.timestamp, bloque.id

def calcular_hash(bloque):
    contenido = bloque.hashAnterior + bloque.timestamp + bloque.archivo
    hasheador = hashlib.sha256()
    hasheador.update(contenido.encode('utf-8'))
    hash_actual = str(hasheador.hexdigest())
    return hash_actual

def validar_bc(index, archivo):
    # bloque_v = Bloque.objects.all()[int(index)-1]
    bloque_v = Bloque.objects.raw('SELECT * FROM creacion_bloque WHERE id = %s', [int(index)])[0]
    bloque_v.archivo = hash_archivo(archivo)
    bloque_v.hashActual = calcular_hash(bloque_v)
    hash_a = bloque_v.hashActual
    lista_bloques = Bloque.objects.raw('SELECT * FROM creacion_bloque WHERE hashActual = %s', [hash_a])
    if len(lista_bloques) == 0:
        return False, bloque_v.archivo
    return True, bloque_v.archivo, bloque_v.hashActual


   




