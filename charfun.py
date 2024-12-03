"""
charfun.py
Programa que determina si una cadena proporcionada por el usuario es palíndroma. 
Para ello se preguntará por teclado al usuario tantas veces como quiera hasta que escriba la palabra salir.
Ultima Modificación. 04/12/2024

Autor. Gregorio Coronado Morón
CoAutor. Alejandro López Calderón
Dependencias. Unicodedata
"""
import unicodedata

def esPalindromo(cadena):
    """
    Función que verifica si una cadena es palíndroma y devuelve un Booleano
    """
    # Elimina espacios del principio y final, y lo convierte en minúsculas
    cadena = cadena.strip().lower()
    
    # Comprueba si la cadena está vacía o tiene un solo carácter
    if len(cadena) <= 1:
        return False
    
    # Elimina acentos y caracteres especiales
    cadena_limpia = ''.join(char for char in unicodedata.normalize('NFKD', cadena) if char.isalnum())

    # Compara la cadena con su reverso
    return cadena_limpia == cadena_limpia[::-1]

def main():
    """
    Función que solicita al usuario cadenas de texto y comprueba si son palíndromas, 
    hasta que el usuario escriba 'salir'.
    Alejandro López Calderón
    """
    salir = False

    while not salir:
        frase = input("Introduce una frase (o escribe 'salir' para terminar): ").strip()

        # Finaliza el programa si el usuario escribe "salir"
        if frase.lower() == "salir":
            salir = True
            print("Programa finalizado.")
        elif not frase:
            # Comprueba si la cadena está vacía o solo contiene espacios
            print("La cadena está vacía o solo contiene espacios. Inténtalo de nuevo.")
        else:
        # Comprueba si es palíndromo llamando a la función 'esPalindromo'
            if esPalindromo(frase):
                print("La frase es palíndroma.")
            else:
                print("La frase no es palíndroma.")
                
if __name__ == "__main__":
    main()
