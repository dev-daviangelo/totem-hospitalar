class Classificador:

    def classificar(self, paciente):

        if paciente.idade >= 60 or paciente.pcd.upper() == "S":
            return "PRIORITÁRIO"

        return "Geral"