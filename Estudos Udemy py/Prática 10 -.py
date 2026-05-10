

imposto = 0.3

def calcular_imposto(valor):
    resultado = valor*imposto
    return resultado

print(calcular_imposto(5000))

calcular_imposto2 = lambda valor: valor*imposto

print(calcular_imposto2(5000))

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(4))