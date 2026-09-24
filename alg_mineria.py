import hashlib
import time

# Definir clase 



def minar_bloque_2(encabezado, target, nonce_max):
    bloque_hash = hashlib.sha256(hashlib.sha256(encabezado))

    if bloque_hash < target:
        return encabezado, bloque_hash

    if nonce > nonce_max:
        encabezado

    

def minarbloque(transacciones, hash_bloque_anterior, target):


    while True:
        hash_resultado = hashlib.sha256(hashlib.sha256(encabezado))
        if hash_resultado < target : 
            return encabezado, hash_resultado
        encabezado.nonce+=1

        if encabezado.nonce > nonce_max :
            encabezado.timestamp = time.time()
            encabezado.nonce=0

