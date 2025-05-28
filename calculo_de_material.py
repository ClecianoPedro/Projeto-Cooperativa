qtd_pallets_cat_1 = int(input("Quantos pallets CAT-1: "))
qtd_pallets_cat_2 = int(input("Quantos pallets CAT-2: "))
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

print(f"Você precisa de {qtd_caixas} UND DE CAIXAS")
print(f"Você precisa de {qtd_cumbuca} CX DE CUMBUCAS")
print(f"Você precisa de {qtd_bolsao} UND DE BOLSÕES")
print(f"Você precisa de {qtd_cinta_cat_1} CX CINTA BELVALE")
print(f"Você precisa de {qtd_cinta_cat_2} CX CINTA QUATRO ESTAÇÕES")
print(f"Você precisa de {qtd_selo} ROLOS DE SELO")
print(f"Você precisa de {qtd_etq_p_caixa} ROLOS DE ETQ P/ CAIXA")
print(f"Você precisa de {qtd_generador} UND DE GENERADORES")
print(f"Você precisa de {qtd_cantoneira} UND DE CANTONEIRAS")