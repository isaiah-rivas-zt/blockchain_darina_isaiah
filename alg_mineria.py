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

    def modificar_nonce(self,incoming_nonce):
        self.nonce = incoming_nonce

    def modificar_timestamp(self,incoming_timestamp):
        self.timestamp = incoming_timestamp

    def obtener_nonce(self):
        return self.nonce

def minar_bloque(bloque, target, nonce_max):
    bloque_encabezado = bloque.obtener_encabezado
    bloque_hash = hashlib.sha256(hashlib.sha256(bloque))

    if bloque_hash < target:
        return bloque_encabezado, bloque_hash
    bloque.modificar_nonce += 1

    if bloque.obtener_nonce > nonce_max:
        bloque.modificar_timestamp = time.time()
        bloque.modificar_nonce = 0

    