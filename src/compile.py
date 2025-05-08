modules = ["utils", "palindrome", "party", "file_chooser"]

if __name__ == "__main__":
    for module in modules:
        __import__(module)

    print("Todos los modulos se importaron correctamente")
