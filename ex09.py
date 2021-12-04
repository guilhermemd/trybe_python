def calculadora():
    soma = 0
    numeros = input('Digite vários número separados com espaço ')
    results = numeros.split(" ")
    for result in results:
        if not result.isdigit():
            print(f"Erro ao somar valores, {result} é um valor inválido")
        soma += int(result)
    print(f"A soma total é de {soma}")


calculadora()
