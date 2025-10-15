from Ingrediente import Ingrediente

class Stock:
    def __init__(self):
        self.lista_ingredientes = []

    def agregar_ingrediente(self, ingrediente):
        # Si el ingrediente ya existe, suma la cantidad
        for ing in self.lista_ingredientes:
            if ing.nombre == ingrediente.nombre and ing.unidad == ingrediente.unidad:
                ing.cantidad = float(ing.cantidad) + float(ingrediente.cantidad)
                return
        # Si no existe, lo agrega
        self.lista_ingredientes.append(ingrediente)

    def mostrar_stock(self):
        # Devuelve una lista de strings con los ingredientes
        return [str(ing) for ing in self.lista_ingredientes]

    def eliminar_ingrediente(self, nombre_ingrediente):
        self.lista_ingredientes = [
            ing for ing in self.lista_ingredientes if ing.nombre != nombre_ingrediente
        ]

    def verificar_stock(self):
        return len(self.lista_ingredientes) > 0

    def actualizar_stock(self, nombre_ingrediente, nueva_cantidad):
        for ing in self.lista_ingredientes:
            if ing.nombre == nombre_ingrediente:
                ing.cantidad = nueva_cantidad
                return True
        return False

    def obtener_elementos_menu(self):
        return self.lista_ingredientes

