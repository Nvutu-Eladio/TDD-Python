from calculadora import soma

try:
    print(soma(15, '15'))
except AssertionError as e:
    print(f'Conta Inválida: {e}')

print('Conta', soma(25, 25))

# import calculadora

# result = calculadora.soma(10,11)
# print(result)
