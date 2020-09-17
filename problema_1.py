import os 
class alumno():
    os.system('cls')
    print("ingresar nombre y nota de un alumno y decir si aprobo o no ")
    print("")
    nombre = input("digite el nombre del alumno: ")
    nota = float(input("digite la nota del alumno: "))
    print ("")

    def calcular_nota(self):
        if ((self.nota >= 3) and (self.nota <=5)):
            print(f"el alumno {self.nombre} aprobo")
        elif ((self.nota) < 3 and (self.nota >= 0)):
            print(f"el alumno {self.nombre} reprobo")
        else: 
            print(f"nota no valida")

def main():
    alumno1 = alumno()
    alumno1.calcular_nota()

    

if __name__ == "__main__":
    main()