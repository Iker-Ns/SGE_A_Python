from Coche import Coche
from Colibrí import Colibrí

#3 instàncies de Cotxe
mustang = Coche("Ford", "Mustang GT", 2023, "Rojo", 250)
fiat = Coche("Fiat", "Punto", 2019, "Blanco", 180)
agera = Coche("Koenigsegg", "Agera RS", 2018, "Rojo", 447)

#3 instàncies de Colibrí.
colibri1 = Colibrí(2, "Verde", 50, 3.5, "Macho")
colibri2 = Colibrí(1, "Rojo", 50, 3.1, "Macho")
colibri3 = Colibrí(3, "Azul", 50, 3.2, "Hembra")

#Mostrar 3 getters de Cotxe
print(f"El {agera.get_modelo()} fue construido por {agera.get_marca()} en el año {agera.get_año_fabricacion()}.")

#Mostrar 4 getters de Colibrí 
print(f"El colibrí 1 tiene {colibri1.get_edad()} años, un pelaje de color {colibri1.get_color_del_pelaje()}, puede alcanzar una velocidad máxima de {colibri1.get_velocidad_maxima()} Km/H y pesa {colibri1.get_peso()} Kg.")

#Modificar 2 atributs de Cotxe a través dels setters
agera.set_color("Negro")
agera.set_velocidad_maxima(180)

#Mostrar els 2 atributs modificats a través dels getters
print(f"El {agera.get_modelo()} puede alcanzar una velocidad de {agera.get_velocidad_maxima()} Km/H y este es de color {agera.get_color()}.")

#Modificar 2 atributs de Colibrí a través dels setters
colibri1.set_color_del_pelaje("Azul")
colibri1.set_edad(4)

#Mostrar els 2 atributs modificats a través dels get
print(f"El colibrí 1 tiene {colibri1.get_edad()} años y un pelaje de color {colibri1.get_color_del_pelaje()}.")