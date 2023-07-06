def jogar():
    import random

    def mensagem_inicial():
        print('*************************************')
        print('***Seja bem vindo ao jogo da forca***')
        print('*************************************')

    def carregando_palavras():
        todas_as_palavras = []
        arquivo = open("palavras.txt", "r")

        for linha in arquivo:
            linha = linha.strip()
            todas_as_palavras.append(linha)

        arquivo.close()
        return todas_as_palavras

    def rodando_tentativas():
        grupo_de_palavras = carregando_palavras()
        escolhendo_palavra = grupo_de_palavras[random.randint(0, len(grupo_de_palavras))]
        palavra_secreta = escolhendo_palavra.upper()
        letras_acertadas = ["_" for letra in palavra_secreta]
        enforcou = False
        acertou = False
        erros = 0

        def desenha_forca(erros):
            print("  _______     ")
            print(" |/      |    ")

            if (erros == 1):
                print(" |      (_)   ")
                print(" |            ")
                print(" |            ")
                print(" |            ")

            if (erros == 2):
                print(" |      (_)   ")
                print(" |      \     ")
                print(" |            ")
                print(" |            ")

            if (erros == 3):
                print(" |      (_)   ")
                print(" |      \|    ")
                print(" |            ")
                print(" |            ")

            if (erros == 4):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |            ")
                print(" |            ")

            if (erros == 5):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |            ")

            if (erros == 6):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      /     ")

            if (erros == 7):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      / \   ")

            print(" |            ")
            print("_|___         ")
            print()

        chances = int(input('Com quantas chances quer começar?'))

        while (not acertou and not enforcou):
            tentativas = chances - erros
            print('Você possuí {} tentativas'.format(tentativas))

            chute = input("Qual letra deseja fazer um palpite? ")
            chute = chute.strip().upper()
            if (chute in  palavra_secreta):
                index = 0
                for letra in palavra_secreta:
                    if (chute == letra):
                        letras_acertadas [index] = letra
                    index += 1

            else:
                erros = erros + 1
                desenha_forca(erros)


            print(letras_acertadas)

            acertou = "_" not in letras_acertadas
            enforcou = erros == chances

            if (acertou):
                print("Parabéns, você ganhou!")
                print("       ___________      ")
                print("      '._==_==_=_.'     ")
                print("      .-\\:      /-.    ")
                print("     | (|:.     |) |    ")
                print("      '-|:.     |-'     ")
                print("        \\::.    /      ")
                print("         '::. .'        ")
                print("           ) (          ")
                print("         _.' '._        ")
                print("        '-------'       ")
                print('A palavra era:')
                print(palavra_secreta)

            if (enforcou):
                print("    _______________         ")
                print("   /               \       ")
                print("  /                 \      ")
                print("//                   \/\  ")
                print("\|   XXXX     XXXX   | /   ")
                print(" |   XXXX     XXXX   |/     ")
                print(" |   XXX       XXX   |      ")
                print(" |                   |      ")
                print(" \__      XXX      __/     ")
                print("   |\     XXX     /|       ")
                print("   | |           | |        ")
                print("   | I I I I I I I |        ")
                print("   |  I I I I I I  |        ")
                print("   \_             _/       ")
                print("     \_         _/         ")
                print("       \_______/           ")
                print("Puxa, você foi enforcado!")
                print("A palavra era {}".format(palavra_secreta))

    mensagem_inicial()
    carregando_palavras()
    rodando_tentativas()


    print('Fim de jogo.')


