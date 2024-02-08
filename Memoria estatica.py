
import tkinter as tk
def obtener_calificacion():
    ventana = tk.Tk()
    ventana.withdraw()
    calificacion = tk.simpledialog.askinteger("Calificación", "Introduce la calificación: ")
    return calificacion
def main():
    calificaciones = []
    for i in range(5):
        calificacion = obtener_calificacion()
        calificaciones.append(calificacion)
    for i, calificacion in enumerate(calificaciones, start=1):
        print(f"Calificación {i}: {calificacion}")
if __name__ == "__main__":
    main()
