import math

Temperatura = []
Humedad = []
Presión = []
Velocidad = []
Direccion = []

with open("datos.txt", "r") as archivo:
    for linea in archivo:
        if "Temperatura" in linea:
            Temperatura.append(float(linea.split(":")[1].strip()))

        if "Humedad" in linea:
            Humedad.append(float(linea.split(":")[1].strip()))

        if "Presion" in linea:
            Presión.append(float(linea.split(":")[1].strip()))

        if "Viento" in linea:
            Viento = linea.split(":")
            Valor = Viento[1].split(",")
            Velo = float(Valor[0].strip())

            Velocidad.append(Velo)
            Direccion.append(Valor[1].strip())

with open('Direccion.txt', 'r') as file:
    reemplazos = {}
    for line in file:
        clave, valor = line.strip().split(':')
        reemplazos[clave] = float(valor)

Direccion_grados = [reemplazos.get(item, item) for item in Direccion]


class Procesamiento:
    def Promedio(self, lista):
        prom = 0
        for valor in lista:
            prom += valor
        prom = prom / len(lista)
        return round(prom)

    def Predominacion(self, lista):
        x_sum = 0
        y_sum = 0

        for direccion in lista:
            radianes = math.radians(direccion)
            x_sum += math.cos(radianes)
            y_sum += math.sin(radianes)

        angulo_rad = math.atan2(y_sum, x_sum)
        angulo_grados = math.degrees(angulo_rad)

        if angulo_grados < 0:
            angulo_grados += 360

        return round(angulo_grados)


Proceso = Procesamiento()

print("La Temperatura promedio es aproximadamente de: {}".format(Proceso.Promedio(Temperatura)))
print("La Humedad promedio es aproximadamente de: {}".format(Proceso.Promedio(Humedad)))
print("La Presion promedio es aproximadamente de: {}".format(Proceso.Promedio(Presión)))
print("La Velocidad promedio es aproximadamente de: {}".format(Proceso.Promedio(Velocidad)))
print("La dirección predominante del viento es aproximadamente {}°".format(Proceso.Predominacion(Direccion_grados)))
