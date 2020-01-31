import hashlib
import datetime
import linecache
import glob


def date_string():
    currentDT = datetime.datetime.now()
    date_time = currentDT.strftime("%Y-%m-%d %H:%M:%S.%f")
    return date_time

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def encrypt_documento(archivopdf):
    BLOCKSIZE = 65536
    hasher = hashlib.sha256()
    with open(archivopdf, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()

def crear_bloque_primero():
    f= open("block1.txt","w+")
    f.write("traer fecha\n")
    f.write(date_string())
    f.write("\n")
    f.write("hash fecha\n")
    d = encrypt_string(date_string())
    f.write(d)
    f.write("\n")
    f.write("enfriptar pdf\n")
    archpdf1 = "prueba1.pdf"
    doc = encrypt_documento(archpdf1)
    f.write(doc)
    f.write("\n")
    f.write("encriptar bloque\n")
    archivoant = encrypt_string("Primer bloque")
    f.write(archivoant)
    f.write("\n")
    x = d + "\n" + doc + "\n" + archivoant + "\n"
    f.write("\n")
    f.write(encrypt_string(x))
    f.write("\n")
    f.close()
    print("block1.txt creado con exito")

def crear_bloque_aut(archivotxt, archtxtmenos):
    archivoant = linecache.getline(archtxtmenos, 10)
    f= open(archivotxt,"w+")
    f.write("traer fecha\n")
    f.write(date_string())
    f.write("\n")
    f.write("hash fecha\n")
    d = encrypt_string(date_string())
    f.write(d)
    f.write("\n")
    f.write("enfriptar pdf\n")
    doc = encrypt_documento(archpdf)
    f.write(doc)
    f.write("\n")
    f.write("encriptar bloque\n")
    f.write(archivoant)
    f.write("\n")
    x = d +"\n"+ doc + "\n" + archivoant
    f.write(encrypt_string(x))
    f.write("\n")
    f.close()
    return encrypt_string(x)

def validar_bloque(n):
    fecha_ant = linecache.getline(archtxtmenos, 4)
    doc_ant = linecache.getline(archtxtmenos, 6)
    block_ant = linecache.getline(archtxtmenos, 8)
    block = linecache.getline(archtxtmenos, 10)
    block2 = block.strip()
    txt_anterior = fecha_ant + doc_ant + block_ant
    txt_ant_hash = encrypt_string(txt_anterior)
    if (block2 != txt_ant_hash):
        return txt_anterior
    return n

if __name__ == "__main__":
    print('Creando Blocks...')
    myPath = 'C:/Users/panch/Desktop/block'

    m= len(glob.glob1(myPath,"*.txt"))
    if (m < 1):
        crear_bloque_primero()
        m=2
    n = 2
    
    Counter = len(glob.glob1(myPath,"*.pdf"))
    while (n <= Counter):
        archpdf = "prueba" + str(n) + ".pdf"
        archtxt = "block" + str(m) + ".txt"
        archtxtmenos = "block" + str(m-1) + ".txt"
        encrypt_documento(archpdf)
        crear_bloque_aut(archtxt, archtxtmenos)
        print(archtxt + " creado con exito")
        m = m + 1
        n=n+1
