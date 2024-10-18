class Questao:
    def __init__(self, id, pergunta, resposta_correta):
        self.id = id
        self.pergunta = pergunta
        self.resposta_correta= resposta_correta

    def  verificar_resposta(self, resposta_usuario):
        return resposta_usuario.strip().lower() == self.resposta_correta.lower()


