print('Alterado no celular')
while True:
    print('LOJA DO BRAZ!')
    text = f"""
    1.Comprar item
    2.Ver estoque
    3.Sair da loja
    """
    print(text)

    escolha = int(input('Escolha uma das opções á cima:'))

    if escolha == 1:
        text2 = f"""
        R$12,00 >>> camisa
        R$20,00 >>> sapato
        R$50,00 >>> bolsa de coro
        """
        print(text2)
        item = input('o que vc vai querer comprar:')
        n1 = int(input('Quantos vc vai querer:'))

        if item == "camisa":
            r = (n1 * 12)
            print(f'Vai dar R${r} Senhor!')
        elif item == "sapato":
            r = (n1 * 20)
            print(f'Vai dar R${r} senhor!')
        elif item == "bolsa de coro":
            r = (n1 * 50)
            print(f'Vai dar R${r} senhor!')
        else:
            print('Só tem esses itens á cima por enquanto senhor!')
    elif escolha == 2:
        text3 = f"""
        7 camisas
        9 sapatos
        10 bolsa de coro
        """
        print(text3)
        escolha2 = input('Deseja ver o que quer comprar: sim ou nao')

        if escolha2 == "sim":
            print('Aqui está!')

            text2 = f"""
                   R$12,00 >>> camisa
                   R$20,00 >>> sapato
                   R$50,00 >>> bolsa de coro
                   """
            print(text2)
            item = input('o que vc vai querer comprar:')
            n1 = int(input('Quantos vc vai querer:'))

            if item == "camisa":
                    r = (n1 * 12)
                    print(f'Vai dar R${r} Senhor!')
            elif item == "sapato":
                    r = (n1 * 20)
                    print(f'Vai dar R${r} senhor!')
            elif item == "bolsa de coro":
                r = (n1 * 50)
                    print(f'Vai dar R${r} senhor!')
                else:
                    print('por enquanto a gente só temos esses itens senhor!')

