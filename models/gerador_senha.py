class GeradorSenha:

    contador_geral = 1
    contador_prioritario = 1

    def gerar(self, tipo):

        if tipo == "PRIORITÁRIO":
            senha = f"P-{GeradorSenha.contador_prioritario:03}"
            GeradorSenha.contador_prioritario += 1

        else:
            senha = f"G-{GeradorSenha.contador_geral:03}"
            GeradorSenha.contador_geral += 1

        return senha