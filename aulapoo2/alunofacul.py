from aluno import Aluno

class AlunoFacul(Aluno):
    def __init__(self, nome, n1, n2, n3):
        super().__init__(nome, n1, n2)
        self.__n3 = n3
        self.__media = 0.0
        self.__status = "Matriculado"

    def calcMedia(self):

        n1 = self.getN1()
        n2 = self.getN2()
        self.__media = (n1+n2+self.__n3)/3

        if(self.__media >=6):
            self.__status = "Aprovado"
        elif (4 <= self.__media < 6):
            self.__status = "Em Exame"
        else:
            self.__status = "Reprovado"

    def getMedia(self):
        return self.__media
    
    def getStatus(self):
        return self.__status
    
    