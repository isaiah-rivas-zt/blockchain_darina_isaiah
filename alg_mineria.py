import hashlib
import time

def minarbloque(transacciones, hash_bloque_anterior, target):

    encabezado = {
        "transacciones": transacciones,
        "hash_anterior": hash_bloque_anterior,
        "timestamp": time.time(),
        "nonce": 0
    }

    while True:
        hash_resultado = hashlib.sha256(hashlib.sha256(encabezado))
        if hash_resultado < target : 
            return encabezado, hash_resultado
        encabezado.nonce+=1

        if encabezado.nonce > nonce_max :
            encabezado.timestamp = time.time()
            encabezado.nonce=0

