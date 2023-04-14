#variável para medir a quantidade de lixo descartado
pesoLixo = float(input("Digite o peso em quilogramas do lixo descartado(limite = 8KG):"))
pontos = 0
#condição para calcular a quantidade de pontos
if pesoLixo <= 8:
    pontos = pesoLixo * 1000
    print(f"Você ganhou {pontos} pontos!")
else:
    pontos = 8000
    print("Você depositou mais de 8kg, portanto os quilos que você depositou a mais não serão substituidos por pontos.")
    print("Você ganhou 8000 pontos!")

#verifica se o usuário já tem pode resgatar algum prêmio e então pergunta se ele está interessado em resgatar algum
if pontos >= 1500:
    decisao = input("Você já possui pontos o suficiente para resgatar alguns prêmios, deseja ver os prêmios disponíveis?")
    decisao = decisao.lower()
    if decisao == "sim":
        print("Ótimo!, aqui estão as opções:") 
        #condições pra mostrar ao usuário somente os prêmios que ele pode resgatar
        if pontos <= 1500:
            print("1-Passegem transporte público/1500p")
        if pontos > 1500 and pontos <= 1700:
            print("1-Passagem transporte público/1500p")
            print("2-Desconto de 30% em eventos culturais/1700")
        else:
            print("1-Passagem transporte público/1500p")
            print("2-Desconto de 30% em eventos culturais/1700p")  
            print("3-Desconto de 70% em eventos culturais/3200p")
        #usuário escolhe o seu prêmio    
        prem = input("Qual prêmio você deseja escolher?(1, 2 ou 3):")
        if prem == "1":
            res = input("Pegar Passagem por 1500 pontos?")
        elif prem == "2":
            res = input("Pegar desconto de 30% por 1700 pontos?")
        elif prem == "3":
            res = input("Pegar desconto de 70% por 3200?")
        else:
            print("Por favor escolha somente entre 1 a 3")
        #verifica se o usuário quer ou não resgatar o prêmio
        res = res.lower()
        if res == "sim":
            print("Prêmio resgatado com sucesso!") 
        elif res == "não" or res == "nao":  
            print("Certo")
    elif decisao == "não" or decisao == "nao":
        print("Certo, até a próxima")
    else:
        print("Responda com sim ou não, por favor")
else:
    print("Você ainda não possui pontos o suficiente para resgatar algum prêmio, continue reciclando para acumular mais pontos")