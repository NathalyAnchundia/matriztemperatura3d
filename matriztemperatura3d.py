temperatudef calcular_promedio_semanal(temperaturas):
    promedios = []
    for ciudad_temperaturas in temperaturas:
        promedios_ciudad = []
        for semana_temperaturas in ciudad_temperaturas:
            promedio_semana = sum(semana_temperaturas) / len(semana_temperaturas)
            promedios_ciudad.append(promedio_semana)
        promedios.append(promedios_ciudad)
    return promedios

# Crear matriz 3D con temperaturas de ejemplo
temperaturas = [
    [  # Ciudad 1
        [25, 26, 24, 23, 22, 21, 20],  # Semana 1
        [24, 23, 25, 26, 27, 28, 22],  # Semana 2
        [23, 22, 24, 25, 26, 27, 28],  # Semana 3
    ],
    [  # Ciudad 2
        [22, 23, 24, 25, 26, 27, 28],  # Semana 1
        [23, 24, 25, 26, 27, 28, 29],  # Semana 2
        [24, 25, 26, 27, 28, 29, 30],  # Semana 3
    ],
    # Puedes agregar más ciudades y semanas según sea necesario
]

# calcular promedio de temperaturas por semana para cada ciudad
promedios_semanales = calcular_promedio_semanal(temperaturas)

# Mostrar promedios de temperaturas por ciudad y semana
for i, ciudad_temperaturas in enumerate(promedios_semanales):
    print(f"Promedios de temperaturas para la Ciudad {i+1}:")
    for j, promedio_semana in enumerate(ciudad_temperaturas):
        print(f"Semana {j+1}: {promedio_semana}°C")
    print()ra=