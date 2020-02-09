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

def table_record():
    sql_select_Query = "select * from block"
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of Blocks is: ", cursor.rowcount)
    for row in records:
        print("Id = ", row[0], )
        print("hash_file = ", row[1])
        print("hash_time = ", row[2])
        print("hash_block  = ", row[3])
        print("hash_prev  = ", row[4], "\n")
    
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


def crear_bloque():
    cursor.execute("SELECT b.hash_block FROM block b WHERE id=(SELECT max(id) FROM block);")
    block_prev = cursor.fetchone()
    hash_prev = block_prev[0]
    hash_time = encrypt_string(date_string())
    hash_file = encrypt_documento('test.pdf')
    hash_block = encrypt_string(hash_prev +"\n"+ hash_time + "\n" + hash_file)
    sql = "INSERT INTO block (hash_file,hash_time,hash_block,hash_prev) VALUE (%s, %s, %s, %s)"
    val = (hash_file,hash_time,hash_block,hash_prev)
    cursor.execute(sql,val)
    connection.commit()

crear_bloque()
table_record()
    



