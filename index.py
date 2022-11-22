# o objetivo é fazer um jogo de embaralha palavra
from random import shuffle, choice

def main():
    palavra = 'LINDA'
    frases = ['Não foi dessa vez', 'Vamos lá, mais uma vez', 'Você consegue na próxima', 'Não desista ainda!']

    # embalhar a palavra
    def embalhar_palavra(palavra):
        palavra_embaralhada = list(palavra)
        shuffle(palavra_embaralhada)
        palavra_embaralhada = ' '.join(palavra_embaralhada)
        return palavra_embaralhada
    
    # mostrar as tentativas
    def tentativas(palavra, frases):
        x, y = 0, 4
        while x < 5:
            tentativa = input('\nDigite Aqui: ')
            if tentativa.lower() == palavra.lower():
                print('\n--- PARABÉNS VOCÊ CONSEGUIU ----')
                break
            else:
                if y > 1:
                    print('\nAinda faltam '+ str(y) +' tentativas\n\n' + choice(frases))
                else:
                    print('\nUltima tentativa\n\n' + choice(frases))
            x += 1
            y -= 1

    # mostrar para o usuario
    def jogo(palavra, frases):
        print('\nBem vindo ao meu jogo com python\n')
        print('Tente acertar a palavra embaralhada')
        print('\n---- ' + embalhar_palavra(palavra) + ' ----')
        tentativas(palavra, frases)
        jogar_novamente = input('\nQuer jogar novamente: [S/N] ')
        if jogar_novamente.lower() == 's':
            print('\n'+(40 * '-'))
            main()
        else:
            exit()

    jogo(palavra, frases)
main()