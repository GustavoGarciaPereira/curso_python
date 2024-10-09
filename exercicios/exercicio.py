import os
class Caneta:
    def __init__(self,cor):
        self.cor = cor
        self.tampada = True
        self.carga = 100
   
    def destampar(self):
        if self.tampada:
            self.tampada = False
            print("A caneta foi destampada")
           
        else:
            print("A caneta já está desatampada")
   
    def escrever(self):
        if  not self.tampada and self.carga >0:
            self.carga -= 50
            print("Escrevendo")
        else:
            print("A caneta está tampada não posso escrever!")


    def get_garga(self):
        print(f"{self.carga}")
   
    def limpar_tela(self):
        os.system("cls")
   
    def __str__(self):
        return f"Cor {self.cor}  - Tampada {self.tampada} - Carga {self.carga}"


       
       
       
caneta_azul = Caneta("Azul")


caneta_preta = Caneta("Preta")
# # print(caneta.cor)
# # print(caneta.tampada)
# # caneta.destampar()
# # caneta.destampar()
# # print(caneta.tampada)


caneta_azul.limpar_tela()
caneta_azul.get_garga()
caneta_azul.destampar()
caneta_azul.escrever()
caneta_azul.get_garga()
caneta_azul.escrever()
caneta_azul.get_garga()
caneta_azul.escrever()
caneta_azul.get_garga()




print(caneta_azul)
caneta_azul.limpar_tela()