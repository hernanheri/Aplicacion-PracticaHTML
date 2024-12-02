import tkinter as tk
from tkinter import messagebox

def validar_formulario():
    # Obtener valores de los campos
    nombre_completo = entry_nombre_completo.get().strip()
    email = entry_email.get().strip()
    fecha_nacimiento = entry_fecha_nacimiento.get().strip()
    password = entry_password.get().strip()
    confirm_password = entry_confirm_password.get().strip()

    # Validar campos vacíos
    if not nombre_completo or not email or not fecha_nacimiento or not password or not confirm_password:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    # Validar correo electrónico
    if "@" not in email or "." not in email:
        messagebox.showerror("Error", "Por favor, ingresa un correo electrónico válido.")
        return

    # Validar coincidencia de contraseñas
    if password != confirm_password:
        messagebox.showerror("Error", "Las contraseñas no coinciden.")
        return

    # Validar fecha de nacimiento (mayoría de edad)
    try:
        año, mes, día = map(int, fecha_nacimiento.split("-"))
        edad = 2024 - año  # Supongamos que estamos en 2024
        if edad < 18 or (edad == 18 and mes > 12):
            messagebox.showerror("Error", "Debes tener al menos 18 años.")
            return
    except ValueError:
        messagebox.showerror("Error", "Fecha de nacimiento inválida. Usa el formato AAAA-MM-DD.")
        return

    # Mostrar datos en una nueva ventana
    mostrar_datos(nombre_completo, email, fecha_nacimiento)

def mostrar_datos(nombre_completo, email, fecha_nacimiento):
    ventana_datos = tk.Toplevel()
    ventana_datos.title("Datos Registrados")

    # Mostrar los datos registrados
    tk.Label(ventana_datos, text="Datos Registrados", font=("Arial", 14)).pack(pady=10)
    tk.Label(ventana_datos, text=f"Nombre Completo: {nombre_completo}").pack(pady=5)
    tk.Label(ventana_datos, text=f"Correo Electrónico: {email}").pack(pady=5)
    tk.Label(ventana_datos, text=f"Fecha de Nacimiento: {fecha_nacimiento}").pack(pady=5)

    # Botón para cerrar la ventana
    tk.Button(ventana_datos, text="Cerrar", command=ventana_datos.destroy).pack(pady=10)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Registro de Usuario")

# Campos del formulario
tk.Label(ventana, text="Nombre Completo:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nombre_completo = tk.Entry(ventana, width=30)
entry_nombre_completo.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Correo Electrónico:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_email = tk.Entry(ventana, width=30)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(ventana, text="Fecha de Nacimiento (AAAA-MM-DD):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_fecha_nacimiento = tk.Entry(ventana, width=30)
entry_fecha_nacimiento.grid(row=2, column=1, padx=10, pady=5)

tk.Label(ventana, text="Contraseña:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_password = tk.Entry(ventana, width=30, show="*")
entry_password.grid(row=3, column=1, padx=10, pady=5)

tk.Label(ventana, text="Confirmar Contraseña:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_confirm_password = tk.Entry(ventana, width=30, show="*")
entry_confirm_password.grid(row=4, column=1, padx=10, pady=5)

# Botón de registro
tk.Button(ventana, text="Registrar", command=validar_formulario).grid(row=5, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
ventana.mainloop()
