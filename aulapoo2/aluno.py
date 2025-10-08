class Aluno:
<<<<<<< HEAD
    def __init__(self, nome, n1, n2):
=======
    def __init__(self, nome, n1,n2):
>>>>>>> 814b015 (Exercício 2 conceitos de Herança)
        self.__nome = nome
        self.__n1 = n1
        self.__n2 = n2
        self.__media = 0.0
        self.__status = "Matriculado"
<<<<<<< HEAD
    
    def calcMedia(self):
        self.__media = (self.__n1 + self.__n2) / 2

        if self.__media >= 6:
            self.__status = "Aprovado"
        elif 4 < self.__media < 6:
            self.__status = "Em Exame"
        else:
            self.__status = "Reprovado"

    # Getters
    def getNome(self):
        return self.__nome

    def getMedia(self):
        return self.__media
    def getStatus(self):
        return self.__status
=======

    def calcMedia(self):
        self.__media = (self.__n1+self.__n2)/2
        if self.__media >= 5:
            self.__status = "Aprovado"
        else:
            self.__status = "Reprovado"

    def getNome(self):
        return self.__nome
    
    def getN1(self):
        return self.__n1
    
    def getN2(self):
        return self.__n2
    
    def getMedia(self):
        return self.__media 
    
    def getStatus(self):
        return self.__status
    
    def setNotas(self, n1, n2):
        self.__n1 = n1
        self.__n2 = n2
>>>>>>> 814b015 (Exercício 2 conceitos de Herança)
