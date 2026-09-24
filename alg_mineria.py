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
    while(True):
        bloque_encabezado = bloque.obtener_encabezado()
        bloque_hash = hashlib.sha256(hashlib.sha256(bloque_encabezado.encode("utf-8")).digest()).hexdigest()
    
        if bloque_hash < target:
            print(f"¡Bloque minado! Nonce: {bloque.nonce}, Hash: {bloque_hash}")
            return bloque_encabezado, bloque_hash
        bloque.nonce += 1

        if bloque.nonce > nonce_max:
            print("Nonce máximo alcanzado. Actualizando timestamp...")
            bloque.timestamp = time.time()
            bloque.nonce = 0

if __name__ == "__main__":
    dificultad_ceros = 4
    target_dummy = "0" * dificultad_ceros + "f" * (64 - dificultad_ceros)
    limite_nonce = 500000

    bloque_ejemplo = Bloque(
            transacciones="Alice -> Bob: 5 BTC; Bob -> Charlie: 2 BTC",
            hash_anterior="0" * 64,  # Hash del bloque génesis
            timestamp=time.time(),
            nonce=0,
    )
    inicio = time.time()
    encabezado_final, hash_final = minar_bloque(
            bloque=bloque_ejemplo, target=target_dummy, nonce_max=limite_nonce
        )
    fin = time.time()

    print("\n=== RESUMEN ===")
    print(f"Hash \t  {hash_final}  \n")
    print(f"Nonce  \t {bloque_ejemplo.nonce} \n")
