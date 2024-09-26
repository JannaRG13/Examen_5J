print (" -- EXAMEN -- ")
print ("Janna Ramirez MAt:22308051281287")

    # CREACION DE CLASES
class Vehiculos1287: 
    def __init__ (self, idvehiculo1287, marca1287, modelo1287, año1287, color1287, precio1287, kilometraje1287):
        self.idvehiculo1287=idvehiculo1287
        self.marca1287=marca1287
        self.modelo1287=modelo1287
        self.año1287=año1287
        self.color1287=color1287
        self.precio1287=precio1287
        self.kilometraje1287=kilometraje1287
       
    def mostrar_datos(self):
        print(f"Id del Vehiculo: {self.idvehiculo1287}, Marca: {self.marca1287}")
        print(f"Modelo: {self.modelo1287}, Año: {self.año1287}")
        print(f"Color: {self.color1287}, Precio: {self.precio1287}")
        print(f"Kilometraje: {self.kilometraje1287}")
        
    # CREACION DE LISTAS
    def agencia1287(self):
        agencias=["Ford", "Mercedes-Benz", "Chevrolet", "Dodge", "Kia", "Mitsubishi", "Mazda"]
        print(agencias)
        for ag in agencias:
            print(ag)
        
    # CREACION DE TUPLAS
    def cliente1287(self):
        clientes=("Roberto", "Sebastian", "Nicolas", "Dulce", "Ariel", "Frida", "Abril")
        print(clientes)
        for cl in clientes:
            print(cl)
    
    # CREACION DE CONJUNTOS 
    def empleado1287(self):
        empleados={"Luis", "Juan", "Gabriel", "Angel", "Pedro", "Adrian", "Carlos"}
        print(empleados)
        for emp in empleados:
            print(emp)
    
    # CREACION DE DICCIONARIOS
    def venta1287(self):
        ventas={
        "Ford": 51,
        "Mercedes-Benz": 48,
        "Chevrolet": 74,
        "Dodge": 59,
        "Kia": 71,
        "Mitsubishi": 63,
        "Mazda": 55        
    }
        
        print(ventas)
        for x, y in ventas.items():
            print(x, y)
        
    def altas_1287(self):
        print("La información se ha cargado correctamente.")
        
    def bajas_1287(self):
        print("La información se ha cargado correctamente.")
        
    # CREACION DEL OBJETO 
info=Vehiculos1287(128376283, "Dodge", "Charger", 2016, "Negro", "$279,000", "25,000 KM")

# UTILIZACION DE OBJETOS 
info.mostrar_datos()
print("")
print("Lista de agencias")
info.agencia1287()
print("")
print("Lista de clientes")
info.cliente1287()
print("")
print("Lista de empleados")
info.empleado1287()
print("")
print("Lista de ventas")
info.venta1287()
print("")
