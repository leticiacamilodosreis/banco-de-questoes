from database import Database
from questao import Questao

def main():
    db = Database()
    questoes = [Questao(*q)for q in db.buscar_questao()]

    for questao in questoes:
        acertou = False
        while not acertou:
            resposta = input(f"{questao.pergunta}")
            if questao.verificar_resposta(resposta):
                print("correto! próxima questão")
                acertou = True
            else:
                print('errado!! tente novamente :(')

    print('parabens, vc concluiu todas as questões')
    db.fechar_conexao()

if __name__ == "__main__":
    main()

print('oiii')