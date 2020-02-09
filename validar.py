import hashlib
import datetime
import linecache
import glob
import mysql.connector

connection = mysql.connector.connect(   host='localhost',
                                        database='blockchain',
                                        user='Joaquin-PC\Joaquin',
                                        port=3306)
cursor = connection.cursor()

def validar_bloque():
    hash_file =encrypt_documento('test.pdf')
    sql = r"SELECT * FROM block WHERE hash_file='" + hash_file + "';"
    print(sql)
    cursor.execute(sql)
    if (cursor.rowcount > 0):
        print("archivo no alterado!")
    else:
        print("archivo alterado!")

def encrypt_documento(archivopdf):
    BLOCKSIZE = 65536
    hasher = hashlib.sha256()
    with open(archivopdf, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()

validar_bloque()
    

