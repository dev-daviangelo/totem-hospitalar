class Impressora:

    def imprimir_ticket(self, paciente, tipo, servico, senha):

        print("\n------------------------------------------")
        print(" TICKET DE ATENDIMENTO")
        print("------------------------------------------")

        print("PACIENTE:", paciente.nome)
        print("TIPO:", tipo)
        print("SERVIÇO:", servico)
        print("SENHA:", senha)

        print("------------------------------------------")
        print("Aguarde ser chamado no painel central.")