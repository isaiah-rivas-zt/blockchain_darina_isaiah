import hashlib
import time

# Definir clase 

class Bloque:

    def __init__(self, transacciones, hash_anterior, timestamp, nonce=0):
        self.transacciones = transacciones
        self.hash_anterior = hash_anterior
        self.timestamp = timestamp
        self.nonce = nonce

    def obtener_encabezado(self):

        encabezado = (
            str(self.transacciones) +
            str(self.hash_anterior) +
            str(self.timestamp) +
            str(self.nonce)
        )

        return encabezado.encode()

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

