def suma_numeros():
    def suma_iterativa(n):
        suma = 0
        while n > 9:
            suma += n % 10
            n //= 10
        suma += n
        return suma

    def suma_recursiva(n):
        if n <= 9:
            return n
        else:
            return suma_recursiva(n // 10) + n % 10

    n = int(input("Ingresa un número para la suma recursiva e iterativa: "))
    suma_total_iterativa = 0
    suma_total_recursiva = 0

    print("Ingresa los números que deseas sumar:")
    for i in range(n):
        numero = int(input(f"Número -->: "))
        suma_total_iterativa += suma_iterativa(numero)
        suma_total_recursiva += suma_recursiva(numero)

    print("Suma Total Iterativa:", suma_total_iterativa)
    print("Suma Total Recursiva:", suma_total_recursiva)

suma_numeros()