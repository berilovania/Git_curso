num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

soma = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
multiplicacao = num1 * num2
exponenciacao = num1 ** num2

print('A soma dos números é:', soma)
print('A subtração dos números é:', subtracao)
if divisao == 0:
    print('Divisão por zero não é permitida.')
else:
    print('A divisão dos números é:', divisao)
print('A multiplicação dos números é:', multiplicacao)
print('A exponenciação do primeiro número pelo segundo é:', exponenciacao)

print('Operações concluídas com sucesso!')