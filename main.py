import hanoi

def menu () -> int:
    bienvenida  = """
    Bievenido a Torres de Hanoi,
    en este programa se muestran las 
    diferentes soluciones que existen 
    para este juego.
    1. Hanoi Iterativo
    2. Hanoi Recursivo
    3. Hanoi Iterativo-Recursivo
    """
    print (bienvenida)
    opt= int (input ("Ingrese el tipo de solución que desea ver: "))
    return opt

if __name__ == "__main__":
    tipo = menu ()
    hanoi.hanoi_Juego(tipo)