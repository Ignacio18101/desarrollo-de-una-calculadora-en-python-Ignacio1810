def sumar(a, b):
    # aqui se realiza la suma de dos numeros
    x = (a + b)
    return int (x)

def restar(a, b):
    # aqui se realiza la resta de dos numeros
    x = (a - b)
    return int(x)

def multiplicar(a, b):
    # aqui se realiza la multiplicacion de dos numeros
    x = (a * b)
    return int(x)

def dividir(a, b):
    if (b != 0):        
        return a / b
    else:
        return "Error: No se puede dividir por cero"

def main():
    num1 = float(input("Ingrese el primer número:s "))
    num2 = float(input("Ingrese el segundo número: "))

    print("Suma:", sumar(num1, num2))
    print("Resta:", restar(num1, num2))
    print("Multiplicación:", multiplicar(num1, num2))
    print("División:", dividir(num1, num2))

if __name__ == "__main__":
    main()
