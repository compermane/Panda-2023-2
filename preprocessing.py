import csv
from typing import List

class Estudante:
    def __init__(self, notaMT, notaLP, notaCN, notaCH, notaRED, sexo, corRaca, tpEscola, faixaEtaria, q006) -> None:
        self._notaMT = notaMT if notaMT != "" else 0
        self._notaLP = notaLP if notaLP != "" else 0
        self._notaCN = notaCN if notaCN != "" else 0
        self._notaCH = notaCH if notaCH != "" else 0
        self._notaRED = notaRED if notaRED != "" else 0
        self._sexo = sexo

        if corRaca == "0":
            self._corRaca = "Nao declarado"
        elif corRaca == "1":
            self._corRaca = "Branca"
        elif corRaca == "2":
            self._corRaca = "Preta"
        elif corRaca == "3":
            self._corRaca = "Parda"
        elif corRaca == "4":
            self._corRaca = "Amarela"
        elif corRaca == "5":
            self._corRaca = "Indígena"
        else:
            self._corRaca = "Nao dispoe da informacao"

        if tpEscola == "1":
            self._tpEscola = "Nao respondeu"
        elif tpEscola == "2":
            self._tpEscola = "Publica"
        else:
            self._tpEscola = "Privada"

        if faixaEtaria == "1":
            self._faixaEtaria = "Menor de 17 anos"
        elif faixaEtaria == "2":
            self._faixaEtaria = "17 anos"
        elif faixaEtaria == "3":
            self._faixaEtaria = "18 anos"
        elif faixaEtaria == "4":
            self._faixaEtaria = "19 anos"
        elif faixaEtaria == "5":
            self._faixaEtaria = "20 anos"
        elif faixaEtaria == "6":
            self._faixaEtaria = "21 anos"
        elif faixaEtaria == "7":
            self._faixaEtaria = "22 anos"
        elif faixaEtaria == "8":
            self._faixaEtaria = "23 anos"
        elif faixaEtaria == "9":
            self._faixaEtaria = "24 anos"
        elif faixaEtaria == "10":
            self._faixaEtaria = "25 anos"
        elif faixaEtaria == "11":
            self._faixaEtaria = "Entre 26 e 30 anos"
        elif faixaEtaria == "12":
            self._faixaEtaria = "Entre 31 e 35 anos"
        elif faixaEtaria == "13":
            self._faixaEtaria = "Entre 36 e 40 anos"
        elif faixaEtaria == "14":
            self._faixaEtaria = "Entre 41 e 45 anos"
        elif faixaEtaria == "15":
            self._faixaEtaria = "Entre 46 e 50 anos"
        elif faixaEtaria == "16":
            self._faixaEtaria = "Entre 51 e 55 anos"
        elif faixaEtaria == "17":
            self._faixaEtaria = "Entre 56 e 60 anos"
        elif faixaEtaria == "18":
            self._faixaEtaria = "Entre 61 e 65 anos"
        elif faixaEtaria == "19":
            self._faixaEtaria = "Entre 66 e 70 anos"
        else:
            self._faixaEtaria = "Maior de 70 anos"

        if q006 == "A":
            self._q006 = "Nenhuma Renda"
        elif q006 == "B":
            self._q006 = "Até R$ 1.212,00"
        elif q006 == "C":
            self._q006 = "De R$ 1.212,01 até R$ 1.818,00."
        elif q006 == "D":
            self._q006 = "De R$ 1.818,01 até R$ 2.424,00."
        elif q006 == "E":
            self._q006 = "De R$ 2.424,01 até R$ 3.030,00."
        elif q006 == "F":
            self._q006 = "De R$ 3.030,01 até R$ 3.636,00."
        elif q006 == "G":
            self._q006 = "De R$ 3.636,01 até R$ 4.848,00."
        elif q006 == "H":
            self._q006 = "De R$ 4.848,01 até R$ 6.060,00."
        elif q006 == "I":
            self._q006 = "De R$ 6.060,01 até R$ 7.272,00."
        elif q006 == "J":
            self._q006 = "De R$ 7.272,01 até R$ 8.484,00."
        elif q006 == "K":
            self._q006 = "De R$ 8.484,01 até R$ 9.696,00."
        elif q006 == "L":
            self._q006 = "De R$ 9.696,01 até R$ 10.908,00."
        elif q006 == "M":
            self._q006 = "De R$ 10.908,01 até R$ 12.120,00."
        elif q006 == "N":
            self._q006 = "De R$ 12.120,01 até R$ 14.544,00."
        elif q006 == "O":
            self._q006 = "De R$ 14.544,01 até R$ 18.180,00."
        elif q006 == "P":
            self._q006 = "De R$ 18.180,01 até R$ 24.240,00."
        elif q006 == "Q":
            self._q006 = "Acima de R$ 24.240,00."
    @property
    def notaMT(self):
        return self._notaMT
    
    @property
    def notaLP(self):
        return self._notaLP

    @property
    def notaCN(self):
        return self._notaCN
    
    @property
    def notaCH(self):
        return self._notaCH
    
    @property
    def notaRED(self):
        return self._notaRED

    @property
    def sexo(self):
        return self._sexo

    @property
    def corRaca(self):
        return self._corRaca
    
    @property
    def tpEscola(self):
        return self._tpEscola

    @property
    def faixaEtaria(self):
        return self._faixaEtaria
    
    @property
    def q006(self):
        return self._q006
    
    def calculaMedia(self) -> float:
        sum = float(self.notaCH) + float(self.notaCN) + float(self.notaLP) + float(self.notaMT) + float(self.notaRED)
        return round((sum / 5), 2)
    
def readData() -> List[Estudante]:
    with open("MICRODADOS_ENEM_2022.csv", "r", encoding = "cp1252") as f:
        csv_reader = csv.DictReader(f, delimiter = ";")
        estudantes: List[Estudante] = []

        for row in csv_reader:
            estudantes.append(Estudante(row["NU_NOTA_MT"], row["NU_NOTA_LC"], row["NU_NOTA_CN"], row["NU_NOTA_CH"], row["NU_NOTA_REDACAO"], row["TP_SEXO"], row["TP_COR_RACA"], row["TP_ESCOLA"], row["TP_FAIXA_ETARIA"], row["Q006"]))
        f.close()

    return estudantes

def writeData(estudantes: List[Estudante]) -> None:
    with open("Microdados_do_enem.csv", "w", newline = '') as f:
        writer = csv.writer(f)
        header = ["NU_NOTA_MT", "NU_NOTA_LC", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_REDACAO", "MEDIA_SIMPLES", "TP_ESCOLA", "TP_SEXO", "TP_COR_RACA", "TP_FAIXA_ETARIA", "Q006"]

        writer.writerow(header)

        for est in estudantes:
            row = [est.notaMT, est.notaLP, est.notaCN, est.notaCH, est.notaRED, est.calculaMedia(), est.tpEscola, est.sexo, est.corRaca, est.faixaEtaria, est.q006]
            writer.writerow(row)

    f.close()

if __name__ == "__main__":
    estudantes: List[Estudante] = readData()
    writeData(estudantes)