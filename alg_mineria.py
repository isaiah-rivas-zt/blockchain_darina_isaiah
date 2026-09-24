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
        return encabezado

def minar_bloque(bloque, target, nonce_max):
    bloque_encabezado = bloque.obtener_encabezado()
    bloque_hash = hashlib.sha256(hashlib.sha256(bloque))

    while(True):
        if bloque_hash < target:
            return bloque_encabezado, bloque_hash
        bloque.nonce += 1

        if bloque.nonce > nonce_max:
            bloque.timestamp = time.time()
            bloque.nonce = 0

