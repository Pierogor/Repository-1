def calcular_altitud(presion_hpa: float) -> float:
    """Calcula la altitud relativa en metros usando la ecuación barométrica."""
    return 44330.0 * (1.0 - (presion_hpa / 1013.25) ** 0.1903)

def determinar_estado_vuelo(altitud_actual: float, altitud_previa: float, aceleracion: float) -> str:
    """Determina la fase operativa del cohete basada en variación de altitud."""
    if altitud_actual <= 300.0 and altitud_actual < altitud_previa:
        return "3: Despliegue de Paracaídas"
    elif altitud_actual < altitud_previa:
        return "2: Apogeo / Caída libre"
    else:
        return "1: Ascenso"

def evaluar_alerta_temperatura(temp_celsius: float) -> str:
    """Evalúa umbrales térmicos críticos de la estructura."""
    UMBRAL_ALERTA = 80.0
    if temp_celsius > UMBRAL_ALERTA:
        return "CRÍTICA: Sobrecalentamiento"
    return "NORMAL"

def ejecutar_monitoreo():
    t = 0
    altitud_previa = 0.0
    altitud_maxima = 0.0
    aceleracion_maxima = -999.0
    suma_temperatura = 0.0
    contador_lecturas = 0
    apogeo_detectado = False
    en_vuelo = True

    print("=== SISTEMA DE MONITOREO DE VUELO ===")

    while en_vuelo:
        print(f"\n--- Tiempo: t = {t} s ---")
        presion_hpa = float(input("Presión atmosférica (hPa): "))
        aceleracion = float(input("Aceleración (m/s^2): "))
        temp_celsius = float(input("Temperatura (°C): "))

        altitud_actual = calcular_altitud(presion_hpa)

        # Detección del primer descenso (Apogeo)
        if not apogeo_detectado and t > 0 and altitud_actual < altitud_previa:
            apogeo_detectado = True
            print(">> [EVENTO] ¡Apogeo alcanzado! Inicio de descenso. <<")

        # Registro de máximos escalares
        if altitud_actual > altitud_maxima:
            altitud_actual = altitud_maxima
            

        if aceleracion > aceleracion_maxima:
            aceleracion_maxima = aceleracion

        # Acumuladores de promedio
        suma_temperatura += temp_celsius
        contador_lecturas += 1

        # Obtención de estados
        estado = determinar_estado_vuelo(altitud_actual, altitud_previa, aceleracion)
        alerta = evaluar_alerta_temperatura(temp_celsius)

        # Telemetría en consola
        print(f"Altitud Actual: {altitud_actual:.2f} m | Apogeo Registrado: {altitud_maxima:.2f} m")
        print(f"Estado de Vuelo: {estado}")
        print(f"Estado Térmico:  {alerta}")

        # Condición de parada (aterrizaje o cese de transmisión)
        if altitud_actual <= 0 and t > 0:
            print("\n>> [SISTEMA] Cohete en superficie. Fin de la telemetría. <<")
            en_vuelo = False

        # Preparación del siguiente ciclo
        altitud_previa = altitud_actual
        t += 1

    # Resumen final
    if contador_lecturas > 0:
        promedio_temp = suma_temperatura / contador_lecturas
        print("\n================ RESUMEN DE MISIÓN ================")
        print(f"Tiempo Total de Vuelo: {t - 1} s")
        print(f"Altitud Máxima (Apogeo): {altitud_maxima:.2f} m")
        print(f"Aceleración Máxima:     {aceleracion_maxima:.2f} m/s^2")
        print(f"Temperatura Promedio:   {promedio_temp:.2f} °C")

if __name__ == "__main__":
    ejecutar_monitoreo()