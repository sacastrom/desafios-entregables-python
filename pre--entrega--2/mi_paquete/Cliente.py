class Cliente:
    def __init__(self, nombre, edad, direccion, email):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.email = email

    def enviar_mail(self, mensaje):
        
        print(f"Enviando correo a {self.email}: {mensaje}")

    def realizar_compra(self, producto):
        
        print(f"{self.nombre} ha realizado la compra del producto {producto}")

    def __str__(self):
        return self.nombre


class ClientePersonalizado(Cliente):
    def enviar_mail_personalizado(self, mensaje_personalizado):
        mensaje = "¡Hola {}! {}".format(self.nombre, mensaje_personalizado)
        self.enviar_mail(mensaje)