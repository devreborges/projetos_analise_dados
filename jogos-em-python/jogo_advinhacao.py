def jogar():
    import random as rd

    print('************************************');
    print('Seja bem vindo ao jogo de advinhação');
    print('************************************');

    print('Nesse jogo você deve adivinhar em qual número estarei pensando, tudo bem?');
    print('');
    print('A pontuação inicial de toda partida é igual a 1000.');
    print('A cada erro, será subtraído da pontuação incial, um valor igual ao módulo da diferença entre o número que eu pensei e o seu chute.');

    dificuldade = int(input('Selecione a dificuldade que deseja: (1)Fácil, (2) Normal, (3)Difícil- '));


    pontos = 1000
    tentativas = 0

    if (dificuldade == 1):
        tentativas = 20;
    elif (dificuldade == 2):
        tentativas = 15;
    else:
        if (dificuldade == 3):
            tentativas = 10;
        else:
            print('Você digitou um número inválido para dificuldade, uma pena.')

    numero_secreto = rd.randint(1, 100);

    while (tentativas > 0):
        print('Eu estou pesando em um número de 1 ate 100.');
        print(f'você possui {tentativas} tentativas');
        print('');
        chute = int(input('Em qual número estou pensando? '));

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Parabéns você acertou, e fez {} pontos".format(pontos));
            break
        else:
            if (maior):
                print('Que pena, você chutou um número maior do que o número que eu estava pensando.');
            elif (menor):
                print('Que pena, você chutou um número menor do que o número que eu estava pensando.');
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = abs(pontos - pontos_perdidos);
        tentativas = tentativas - 1

    print('');
    print(f'Eu estava pensando no número {numero_secreto}');
    print('Fim do jogo.');
