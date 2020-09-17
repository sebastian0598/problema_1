def calcular_nota(self):
    if ((self.nota >= 3) and (self.nota <=5)):
        print(f"el alumno {self.nombre} aprobo")
    elif ((self.nota) < 3 and (self.nota >= 0)):
        print(f"el alumno {self.nombre} reprobo")
    else: 
        print(f"nota no valida")
            

def main():

    alumno1.calcular_nota()

    
if __name__== "__main__":
    main()