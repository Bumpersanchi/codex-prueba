def saludar(nombre):
    return f"Hola, {nombre}! Bienvenido a Codex."

if __name__ == "__main__":
    nombre = input("¿Cómo te llamas? ")
    print(saludar(nombre))
