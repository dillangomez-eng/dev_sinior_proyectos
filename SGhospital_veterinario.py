from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_rol(self):
        pass
    

class Veterinario(Persona):
    def __init__(self, nombre, documento, especialidad):
        super().__init__(nombre, documento)
        self.especialidad = especialidad

    def mostrar_rol(self):
        return f"Veterinario: {self.nombre}, Especialidad: {self.especialidad}"
    
    def atender_mascota(self, mascota):
        return f"{self.nombre} está atendiendo a {mascota.nombre}."
    
class Recepcionista(Persona):
    def __init__(self, nombre, documento, ):
        super().__init__(nombre, documento)
    
    def mostrar_rol(self):
        return f"Recepcionista: {self.nombre}"
    
    def registrar_cita(self, mascota, fecha):
        return f"{self.nombre} ha registrado una cita para {mascota.nombre} el {fecha}."
    
class Cliente(Persona):
    def __init__(self, nombre, documento):
        super().__init__(nombre, documento)
        self.mascotas = []

    def mostrar_rol(self):
        return f"Cliente: {self.nombre}"
    
    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
        return f"{mascota.nombre} ha sido agregada a la lista de mascotas de {self.nombre}."
    
    def mostrar_mascotas(self):
        if not self.mascotas:
            return f"{self.nombre} no tiene mascotas registradas."
        return f"{self.nombre} tiene las siguientes mascotas: " + ", ".join(mascota.nombre for mascota in self.mascotas)
    

class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def mostrar_info(self):
        return f"Mascota: {self.nombre}, Especie: {self.especie}, Edad: {self.edad} años, Peso: {self.peso} kg"
    

class Consulta:
    def __init__(self, mascota, veterinario, motivo, diagnostico):
        self.mascota = mascota
        self.veterinario = veterinario
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.tratamientos = []
        
    def agregar_tratamiento(self, tratamiento, duracion, costo):
        nuevo_tratamiento = Tratamiento(tratamiento, duracion, costo)
        self.tratamientos.append(nuevo_tratamiento)
        return f"Tratamiento '{self.tratamientos[0].nombre}' ha sido agregado a la consulta de {self.mascota.nombre}."
    
    def mostrar_resumen(self):
        resumen = f"Consulta para {self.mascota.nombre} con el veterinario {self.veterinario.nombre}.\n"
        resumen += f"Motivo: {self.motivo}\n"
        resumen += f"Diagnóstico: {self.diagnostico}\n"
        if self.tratamientos:
            resumen += "Tratamientos:\n" + "\n".join(f"- {tratamiento.nombre} (Duración: {tratamiento.duracion_dias} días): ${tratamiento.costo}" for tratamiento in self.tratamientos)
        else:
            resumen += "No se han registrado tratamientos."
        return resumen
    
    def calcular_costo_consulta(self):
        costo_base = 15000  # Costo base de la consulta
        costo_tratamientos = sum(costo for _, costo in self.tratamientos)  # Costo adicional por cada tratamiento
        return costo_base + costo_tratamientos


class Tratamiento:
    def __init__(self, nombre, duracion_dias, costo):
        self.nombre = nombre
        self.duracion_dias = duracion_dias
        self.costo = costo

    def mostrar_info(self):
        return f"Tratamiento: {self.nombre}, Duracion: {self.duracion_dias} días, Costo: ${self.costo}"
    
    
class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass
    
class PagoTarjeta(MetodoPago):
    def __init__(self, numero_tarjeta, titular):
        self.numero_tarjeta = numero_tarjeta
        self.titular = titular

    def procesar_pago(self, monto):
        return f"Procesando pago de ${monto} con tarjeta de crédito a nombre de {self.titular}."

class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto):
        return f"Procesando pago de ${monto} en efectivo."  

class PagoTransferencia(MetodoPago):
    def __init__(self, numero_cuenta, titular):
        self.numero_cuenta = numero_cuenta
        self.titular = titular

    def procesar_pago(self, monto):
        return f"Procesando pago de ${monto} por transferencia bancaria a nombre de {self.titular}."
    
class Factura:
    def __init__(self, consulta, subtotal, impuesto, total):
        self.consulta = consulta
        self.subtotal = subtotal
        self.impuesto = impuesto
        self.total = total

    def calcular_total(self):
        self.total = self.subtotal + self.impuesto
        return self.total
    
    def pagar(self, metodo_pago):
        return metodo_pago.procesar_pago(self.total)
    
    def mostrar_detalles(self):
        detalles = f"Factura para la consulta de {self.consulta.mascota.nombre}:\n"
        detalles += f"Tratarmentos:\n" + "\n".join(f"- {tratamiento[0]}: ${tratamiento[1]}" for tratamiento in self.consulta.tratamientos) + "\n"
        detalles += f"Subtotal: ${self.subtotal}\n"
        detalles += f"Impuesto: ${self.impuesto}\n"
        detalles += f"Total a pagar: ${self.total}\n"
        return detalles
    
    
class Menu:
    def __init__(self):
        self.cliente = None
        self.veterinario = None
        self.mascota = None
        self.consulta = None
        self.factura = None
    
    def mostrar_menu(self):
        print("\n--- Menú Principal ---")
        print("1. Registrar Cliente")
        print("2. Registrar Veterinario")
        print("3. Crear Mascota para Cliente")
        print("4. Registrar consulta")
        print("5. Agregar tratamiento a consulta")
        print("6. Generar factura")
        print("7. Pagar factura")
        print("8. Salir")
        print("----------------------")
    
    def registrar_cliente(self):
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        documento_cliente = input("Ingrese el documento del cliente: ")
        self.cliente = Cliente(nombre_cliente, documento_cliente)
        print(self.cliente.mostrar_rol())
    
    def registrar_veterinario(self):
        nombre_veterinario = input("Ingrese el nombre del veterinario: ")
        documento_veterinario = input("Ingrese el documento del veterinario: ")
        especialidad_veterinario = input("Ingrese la especialidad del veterinario: ")
        self.veterinario = Veterinario(nombre_veterinario, documento_veterinario, especialidad_veterinario)
        print(self.veterinario.mostrar_rol())
    
    def crear_mascota(self):
        if not self.cliente:
            print("Primero debe registrar un cliente.")
            return
        
        agregar_mas = "s"
        while agregar_mas.lower() == "s":
            nombre_mascota = input("Ingrese el nombre de la mascota: ")
            especie_mascota = input("Ingrese la especie de la mascota: ")
            edad_mascota = int(input("Ingrese la edad de la mascota: "))
            peso_mascota = float(input("Ingrese el peso de la mascota: "))
            self.mascota = Mascota(nombre_mascota, especie_mascota, edad_mascota, peso_mascota)
            print(self.cliente.agregar_mascota(self.mascota))
            agregar_mas = input("¿Desea agregar otra mascota? (s/n): ")
    
    def registrar_consulta(self):
        if not self.veterinario or not self.mascota:
            print("Primero debe registrar un veterinario y una mascota.")
            return
        
        
        print("Mascotas registradas:")
        for i, mascota in enumerate(self.cliente.mascotas):
            print(f"{i+1}. {mascota.nombre} - {mascota.especie}")
        try:
            indice_mascota = int(input("Seleccione el número de la mascota: ")) - 1
            self.mascota = self.cliente.mascotas[indice_mascota]
        except (ValueError, IndexError):
            print("Selección inválida.")
            return
        motivo_consulta = input("Ingrese el motivo de la consulta: ")
        diagnostico_consulta = input("Ingrese el diagnóstico de la consulta: ")
        self.consulta = Consulta(self.mascota, self.veterinario, motivo_consulta, diagnostico_consulta)
        print(self.consulta.mostrar_resumen())
    
    def agregar_tratamiento(self):
        if not self.consulta:
            print("Primero debe registrar una consulta.")
            return
        
        agregar_mas = "s"
        while agregar_mas.lower() == "s":
            nombre_tratamiento = input("Ingrese el nombre del tratamiento: ")
            duracion_tratamiento = int(input("Ingrese la duración del tratamiento en días: "))
            costo_tratamiento = float(input("Ingrese el costo del tratamiento: "))
            print(self.consulta.agregar_tratamiento(nombre_tratamiento, duracion_tratamiento, costo_tratamiento))
            agregar_mas = input("¿Desea agregar otro tratamiento? (s/n): ")
    
    def generar_factura(self):
        if not self.consulta:
            print("Primero debe registrar una consulta.")
            return
        
        subtotal_factura = self.consulta.calcular_costo_consulta()
        impuesto_factura = subtotal_factura * 0.15
        self.factura = Factura(self.consulta, subtotal_factura, impuesto_factura, 0)
        self.factura.calcular_total()
        print(self.factura.mostrar_detalles())
    
    def pagar_factura(self):
        if not self.factura:
            print("Primero debe generar una factura.")
            return
        
        print("Seleccione el método de pago:")
        print("1. Tarjeta de crédito")
        print("2. Efectivo")
        print("3. Transferencia bancaria")
        metodo_pago_opcion = input("Opción: ")
        
        if metodo_pago_opcion == "1":
            numero_tarjeta = input("Ingrese el número de tarjeta: ")
            titular_tarjeta = input("Ingrese el nombre del titular de la tarjeta: ")
            metodo_pago = PagoTarjeta(numero_tarjeta, titular_tarjeta)
        elif metodo_pago_opcion == "2":
            metodo_pago = PagoEfectivo()
        elif metodo_pago_opcion == "3":
            numero_cuenta = input("Ingrese el número de cuenta: ")
            titular_cuenta = input("Ingrese el nombre del titular de la cuenta: ")
            metodo_pago = PagoTransferencia(numero_cuenta, titular_cuenta)
        else:
            print("Opción de método de pago no válida.")
            return
        
        print(self.factura.pagar(metodo_pago))
    
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.registrar_cliente()
            elif opcion == "2":
                self.registrar_veterinario()
            elif opcion == "3":
                self.crear_mascota()
            elif opcion == "4":
                self.registrar_consulta()
            elif opcion == "5":
                self.agregar_tratamiento()
            elif opcion == "6":
                self.generar_factura()
            elif opcion == "7":
                self.pagar_factura()
            elif opcion == "8":
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__": 
    menu = Menu()
    menu.ejecutar()