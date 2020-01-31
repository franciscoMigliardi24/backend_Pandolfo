import hashlib
import datetime
import linecache
import glob
import crear




def validar_bloque(n):
    fecha_ant = linecache.getline(archtxtmenos, 4)
    doc_ant = linecache.getline(archtxtmenos, 6)
    block_ant = linecache.getline(archtxtmenos, 8)
    block = linecache.getline(archtxtmenos, 10)
    block2 = block.strip()
    txt_anterior = fecha_ant + doc_ant + block_ant
    txt_ant_hash = crear.encrypt_string(txt_anterior)
    if (block2 != txt_ant_hash):
        return txt_anterior
    return n


if __name__ == "__main__":
    print('Validando blocks...')
    n=2
    myPath = 'C:/Users/panch/Desktop/block'
    counter = len(glob.glob1(myPath,"*.txt"))
    while (n <= counter):
        archtxtmenos = "block" + str(n) + ".txt"
        if (n != validar_bloque(n)):
            print("ERROR AL VALIDAR BLOCK" + str(n))
        else:
            print("BLOCK" + str(n) + " ESTA INTEGRO")
        n=n+1

