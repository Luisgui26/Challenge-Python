#while criado para fazer com que o programa se repita até o usuário digitar  0

while True:
    #variável para medir a quantidade de lixo descartado
    pesoLixo = float(input("Digite o peso em quilogramas do lixo descartado (limite = 8KG), ou digite 0 para sair:"))
    #condição para calcular a quantidade de pontos
    if pesoLixo == 0:
        print("Programa encerrado.")
        break

    pontos = 0
    #verifica se o usuário já tem pode resgatar algum prêmio e então pergunta se ele está interessado em resgatar algum
    if pesoLixo <= 8:
        pontos = pesoLixo * 1000
        print(f"Você ganhou {pontos} pontos!")
    else:
        pontos = 8000
        print("Você depositou mais de 8kg, os quilos extras não geram pontos.")
        print("Você ganhou 8000 pontos!")

    if pontos >= 1500:
        decisao = input("Você já possui pontos suficientes para resgatar prêmios. Deseja ver as opções disponíveis? ").lower()

        if decisao == "sim":
            print("Ótimo! Aqui estão as opções:")
            #condições pra mostrar ao usuário somente os prêmios que ele pode resgatar
            if pontos <= 1500:
                print("1-Passagem transporte público/1500p")

            if 1500 < pontos <= 1700:
                print("1-Passagem transporte público/1500p")
                print("2-Desconto de 30% em eventos culturais/1700p")

            if pontos > 1700:
                print("1-Passagem transporte público/1500p")
                print("2-Desconto de 30% em eventos culturais/1700p")
                print("3-Desconto de 70% em eventos culturais/3200p")
            #while criado para fazer com av pergunta sobre qual prêmio escolher se repita, até o usuário digitar um valor válido
            while True:
                prem = input("Qual prêmio você deseja escolher? (1, 2 ou 3):")

                if prem in ["1", "2", "3"]:
                    break
                else:
                    print("Por favor escolha somente entre 1 a 3")

            if prem == "1":
                res = input("Pegar Passagem por 1500 pontos?")
            elif prem == "2":
                res = input("Pegar desconto de 30% por 1700 pontos?")
            elif prem == "3":
                res = input("Pegar desconto de 70% por 3200 pontos?")

            res = res.lower()
            #verifica se o usuário quer ou não resgatar o prêmio
            if res == "sim":
                print("Prêmio resgatado com sucesso!")
            elif res == "não" or res == "nao":
                print("Certo")
            else:
                print("Responda com sim ou não, por favor")

        elif decisao == "não" or decisao == "nao":
            print("Certo, até a próxima")
        else:
            print("Responda com sim ou não, por favor")

    else:
        print("Você ainda não possui pontos suficientes para resgatar prêmios. Continue reciclando para acumular mais pontos")
