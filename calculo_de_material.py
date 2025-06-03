def menu():
    print("------------------ MENU --------------------")
    print("                                      ")
    print("1- Calcular por QTD de Pallets")
    print("2- Calcular por QTD de Caixas")
    print("3- Sair")
    print("--------------------------------------------")
    opcao = input("Digite a opção desejada: ")
    return opcao
    
while True:
    opcao = menu()
    while opcao != "1" and opcao != "2" and opcao != "3":
        print("Opção inválida!")
        opcao = menu()
    if opcao == "1":
        qtd_pallets_cat_1 = float(input("QTD Pallets CAT-1: "))
        qtd_pallets_cat_2 = float(input("QTD Pallets CAT-2: "))
        qtd_pallets = qtd_pallets_cat_1 + qtd_pallets_cat_2
        qtd_caixas = qtd_pallets * 110
        qtd_cumbuca = (qtd_caixas * 10) / 1000
        qtd_bolsao = qtd_caixas
        qtd_cinta_cat_1 = ((qtd_pallets_cat_1 * 110) * 10) / 2350
        qtd_cinta_cat_2 = ((qtd_pallets_cat_2 * 110) * 10) / 2350
        qtd_selo = (qtd_caixas * 2) / 2000
        qtd_etq_p_caixa = qtd_caixas / 1000
        qtd_generador = qtd_caixas / 2
        qtd_cantoneira = qtd_pallets * 4
        print(f"Para {qtd_pallets_cat_1+qtd_pallets_cat_2} PALLETS VOCÊ PRECISA DE:")
        print(f"{qtd_caixas} UND DE CAIXAS")
        print(f"{qtd_cumbuca} CX DE CUMBUCAS")
        print(f"{qtd_bolsao} UND DE BOLSÕES")
        print(f"{qtd_cinta_cat_1} CX CINTA BELVALE")
        print(f"{qtd_cinta_cat_2} CX CINTA QUATRO ESTAÇÕES")
        print(f"{qtd_selo} ROLOS DE SELO")
        print(f"{qtd_etq_p_caixa} ROLOS DE ETQ P/ CAIXA")
        print(f"{qtd_generador} UND DE GENERADORES")
        print(f"{qtd_cantoneira} UND DE CANTONEIRAS")
        break
    elif opcao == "2":
        qtd_caixas = float(input("QTD de Caixas: "))
        qtd_cumbuca = (qtd_caixas * 10) / 1000
        qtd_bolsao = qtd_caixas
        qtd_selo = (qtd_caixas * 2) / 2000
        qtd_etq_p_caixa = qtd_caixas / 1000
        qtd_generador = qtd_caixas / 2
        qtd_cantoneira = (qtd_caixas / 110) * 4
        print(f"Para {qtd_caixas} CAIXAS PRECISA DE:")
        print(f"Você precisa de {qtd_cumbuca} CX DE CUMBUCAS")
        print(f"Você precisa de {qtd_bolsao} UND DE BOLSÕES")
        print(f"Você precisa de {qtd_selo} ROLOS DE SELO")
        print(f"Você precisa de {qtd_etq_p_caixa} ROLOS DE ETQ P/ CAIXA")
        print(f"Você precisa de {qtd_generador} UND DE GENERADORES")
        print(f"Você precisa de {qtd_cantoneira} UND DE CANTONEIRAS")
        break        
    elif opcao == "3":
        print("Encerrando Programa...")
        break
