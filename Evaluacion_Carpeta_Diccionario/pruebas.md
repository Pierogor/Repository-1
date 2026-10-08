# Reporte de Sistema de Mantenimiento de Aeronaves

Este documento detalla el funcionamiento y la estructura lógica del reto de programación para el control de horas de vuelo y vida útil de componentes aeronáuticos.

## 1. Registrar un nuevo avión

En esta fase del programa (Opción 1 del menú), se da de alta un nuevo equipo en el sistema. El usuario debe ingresar parámetros clave como la **matrícula**, las **horas** de operación y el **modelo** de la aeronave. Al finalizar este proceso, la aeronave queda inicializada y lista para que se le asignen piezas de recambio.

![Insertar imagen aquí: Registro de un nuevo avión](C:\Users\B09S202est\Desktop\evaluacion carpeta\Registro de avion.png)

---

## 2. Partes del código y Estructura de Datos

El programa se ejecuta bajo un bucle principal `while True` que mantiene el menú activo, gestionando las operaciones mediante condicionales `if-elif`. 

**Estructura de almacenamiento:**
La persistencia de los datos durante la ejecución se maneja mediante una combinación de **listas y diccionarios anidados**:
* **Lista principal:** Existe una lista global llamada `Flota_aerea = []` que actúa como la base de datos principal.
* **Diccionarios de Aeronaves:** Cada avión que se registra se guarda como un diccionario dentro de la lista principal, almacenando sus atributos (`matricula`, `modelo`, `horas`).
* **Listas de Componentes:** Dentro del diccionario de cada aeronave, existe una clave `"componentes"` que contiene una lista vacía por defecto. Cuando se usa la Opción 2, esta lista se llena con nuevos diccionarios, donde cada uno representa una pieza específica, sus horas actuales y su límite operativo permitido.
* **Almacenamiento de horas de uso:**
Como se puede ver en la imagen,las horas de uso se le solicitan al usuario con un input que es este: horas_Uso_Actuales = float(input("ingrese la cantidad de horas de uso actuales"))

Posteriormente , se guarda en un diccionario llamado "nuevo_componente" en el que se les asocia una clave para guardarlos en un bloque de información general y no como datos aislados. 

![Insertar imagen aquí: Estructura de listas y diccionarios en el código](C:\Users\B09S202est\Desktop\evaluacion carpeta\Registro de horas de uso.png)

---

## 3. Reporte

La Opción 3 del sistema se encarga de realizar una auditoría de mantenimiento. El algoritmo utiliza bucles `for` anidados para iterar primero sobre la flota aérea y luego sobre los componentes de cada avión. El sistema compara las `horas de uso actuales` contra el `limite de horas permitidas`; si el componente se encuentra dentro de los parámetros, indica que está en condiciones de operación; de lo contrario, genera una alerta crítica.

![Insertar imagen aquí: Interfaz de reporte de estado operativo](C:\Users\B09S202est\Desktop\evaluacion carpeta\Reporte de mantenimiento.png)

![Insertar imagen aquí: Alerta de mantenimiento preventivo](C:\Users\B09S202est\Desktop\evaluacion carpeta\Consulta de mantenimiento con alerta.png)

---

## 4. Reiniciar horas de uso

Esta funcionalidad está integrada dentro del mismo módulo de reportes. Cuando una pieza alcanza o supera su límite de vida útil, el sistema arroja la alerta de cambio y pregunta interactivamente al usuario si desea registrar la sustitución del componente. Al confirmar con una `"s"`, el programa accede al diccionario de esa pieza específica y formatea el valor de `horas de uso actuales` de vuelta a `0.0`, habilitando la aeronave para continuar operando.

![Insertar imagen aquí: Confirmación de cambio de pieza y reinicio a 0.0](C:\Users\B09S202est\Desktop\evaluacion carpeta\Reinicio de horas de componente.png)

---

## 5. Autoevaluación

* **Nota:** 4.5
* **Justificación:** Cumplimos con los requisitos del repositorio , sin embargo debemos aclarar que el sistema de reinicio de horas de los componentes fue agregado el dia de la entrega por desconocimiento propio , por lo mismo en las imágenes se puede apreciar que solo en la ultima se puede ver este sistema dentro del código. El resto de requisitos fueron cumplidos y adjuntados en el repositorio a la hora establecida por el profe.

Piero Gomez : 000607647
Damian Barrera : 000492016  