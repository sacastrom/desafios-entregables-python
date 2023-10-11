from mi_paquete.Cliente import Cliente, ClientePersonalizado

# Crear una instancia de ClientePersonalizado
cliente1 = ClientePersonalizado("Shirley", 31, "Pedro Rivera 3006", "shirley@gmail.com")

# Enviar un correo electrónico personalizado
mensaje_personalizado = "Gracias por registrarte en nuestra tienda en línea."
cliente1.enviar_mail_personalizado(mensaje_personalizado)

# cliente1 = Cliente("Juan", 30, "Calle Principal 123", "juan@example.com")
cliente2 = Cliente("Dayana", 31, "Uruguay 1143", "dayana@gmail.com")

# cliente1.enviar_mail("¡Hola {self.nombre} Gracias por registrarte en nuestra tienda en línea.")
cliente2.realizar_compra("Pantalón")