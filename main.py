from models.paciente import Paciente
from models.menu import Menu
from models.classificador import Classificador
from models.gerador_senha import GeradorSenha
from models.triagem import Triagem
from models.impressora import Impressora


print("==========================================")
print(" HOSPITAL VIVER BEM - AUTOATENDIMENTO")
print("==========================================")

print("\n[CADASTRO DE PACIENTE]")

nome = input("Nome: ")
idade = int(input("Idade: "))
pcd = input("Possui deficiência? (S/N): ")

paciente = Paciente(nome, idade, pcd)

menu = Menu()
opcao = menu.mostrar_menu()

triagem = Triagem()

if triagem.verificar_emergencia(opcao):

    print("\n------------------------------------------")
    print(" ALERTA DE EMERGÊNCIA")
    print("------------------------------------------")

    print("PACIENTE:", paciente.nome)
    print("STATUS: RISCO IMEDIATO")

    print(">>> ATENÇÃO: Encaminhe-se IMEDIATAMENTE")
    print(" ao balcão de triagem médica.")
    print(" Não é necessário aguardar senha.")

else:

    classificador = Classificador()
    tipo = classificador.classificar(paciente)

    gerador = GeradorSenha()
    senha = gerador.gerar(tipo)

    servicos = {
        "1": "Consulta",
        "2": "Exame"
    }

    servico = servicos.get(opcao)

    impressora = Impressora()
    impressora.imprimir_ticket(paciente, tipo, servico, senha)