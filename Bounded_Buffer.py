import threading

### Mario rocha - 23501, Luis Pedro Lira - 23669, Diego Rosales - 23258

capacidad = int(input("Ingrese la capacidad del parqueo: "))
num_hilos = int(input("Ingrese número de hilos: "))

carros = 0
lock = False
contador_global = 0

CICLOS_SIMULACION = 2000 


def adquirir_lock():
    global lock
    while lock:
        pass
    lock = True

def liberar_lock():
    global lock
    lock = False



def estudiante(id_hilo):
    global carros, contador_global

    while True:

        # Terminar simulación cuando se alcance el límite
        if contador_global >= CICLOS_SIMULACION:
            break

        # Generador determinístico de acciones (sin random)
        if (id_hilo + contador_global) % 2 == 0:
            accion = "entrar"
        else:
            accion = "salir"

        print(f"[Hilo {id_hilo}] quiere {accion}")

        adquirir_lock()
        print(f"[Hilo {id_hilo}] >>> ENTRA sección crítica")

        if accion == "entrar":
            if carros < capacidad:
                carros += 1
                print(f"[Hilo {id_hilo}] entró. Carros: {carros}")
            else:
                print(f"[Hilo {id_hilo}] parqueo LLENO")

        else:  # salir
            if carros > 0:
                carros -= 1
                print(f"[Hilo {id_hilo}] salió. Carros: {carros}")
            else:
                print(f"[Hilo {id_hilo}] parqueo VACÍO")

        print(f"[Hilo {id_hilo}] <<< SALE sección crítica")

        contador_global += 1

        liberar_lock()


# ==========================
# Crear Hilos
# ==========================

hilos = []

for i in range(num_hilos):
    t = threading.Thread(target=estudiante, args=(i,))
    hilos.append(t)
    t.start()

for t in hilos:
    t.join()

print("\nSimulación terminada.")