import jogo_advinhacao
import forca

print('************************************');
print('**********Seja bem vindo*************')
print('************************************');
print('')
print('Ditite (1) para jogar o jogo de advinhação ou (2) para jogar  o jogo da forca.')
jogo = int(input('Qual jogo você deseja jogar? '))
if(jogo == 1):
    jogo_advinhacao.jogar();
elif(jogo == 2):
    forca.jogar();
else:
    print('Você não digitou um jogo valido');

