class Paciente:
    def __init__(self):
        self.__nombre = '' 
        self.__cedula = 0 
        self.__genero = '' 
        self.__servicio = '' 
              
    # Metodos get    
    def verNombre(self):
        return self.__nombre 
    def verCedula(self):
        return self.__cedula 
    def verGenero(self):
        return self.__genero 
    def verServicio(self):
        return self.__servicio 
    # metodos set
    def asignarNombre(self,n):
        self.__nombre = n 
    def asignarCedula(self,c):
        self.__cedula = c 
    def asignarGenero(self,g):
        self.__genero = g 
    def asignarServicio(self,s):
        self.__servicio = s 
        
class Sistema:    
    def __init__(self):
        self.__lista_pacientes = [] 
        
    def verificarPacienteC(self,cedula):  
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                return True
        return False
    
    def verificarPacienteNA(self,nombre):  
        for p in self.__lista_pacientes:
            if nombre == p.verNombre().split(" ")[0]:
                return True
            elif nombre == p.verNombre().split(" ")[1]:
                return True
            elif nombre == p.verNombre().split:
                return True
        return False
        
    def ingresarPaciente(self,pac):
        self.__lista_pacientes.append(pac)
        return True
    
    def verDatosPacienteC(self, c):
        if self.verificarPacienteC(c) == False:
            return None
        for p in self.__lista_pacientes:
            if c == p.verCedula():
                return p
    def verDatosPacienteN(self, n):
        __listaN = []
        if self.verificarPacienteNA(n) == False:
            return None
        for p in self.__lista_pacientes:
            if n == p.verNombre().split(" ")[0]:
                __listaN.append(p)
        return __listaN
    def verDatosPacienteA(self, a):
        __listaA = []
        if self.verificarPacienteNA(a) == False:
            return None
        for p in self.__lista_pacientes:
            if a == p.verNombre().split(" ")[1]:
                __listaA.append(p)
        return __listaA
    def verDatosPacienteNA(self, na):
        __listNA = []
        if self.verificarPacienteNA(na) == False:
            return None
        for p in self.__lista_pacientes:
            if na == p.verNombre():
                __listNA.append(p)
        return __listNA
        
            
    def verNumeroPacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes") 

def main():
    sis = Sistema() 
    #probemos lo que llevamos programado
    while True:
        #TAREA HACER EL MENU
        opcion = int(input("\nIngrese \n0 para salir, \n1 para ingresar nuevo paciente, \n2 ver Paciente\n\t--> ")) 
        
        if opcion == 1:
            #ingreso pacientes
            print("A continuacion se solicitaran los datos ...") 
            #1. Se solicitan los datos
            cedula = int(input("Ingrese la cedula: ")) 
            if sis.verificarPacienteC(cedula):
                print("\n<< Ya existe un paciente con esa cedula >>".upper()) 
            else:    
                # 2. se crea un objeto Paciente
                pac = Paciente() 
                # como el paciente esta vacio debo ingresarle la informacion
                pac.asignarNombre(input("Ingrese el nombre: ")) 
                pac.asignarCedula(cedula) 
                pac.asignarGenero(input("Ingrese el genero: ")) 
                pac.asignarServicio(input("Ingrese servicio: ")) 
                #3. se almacena en la lista que esta dentro de la clase sistema
                r = sis.ingresarPaciente(pac)             
                if r:
                    print("Paciente ingresado") 
                else:
                    print("No ingresado") 
        elif opcion == 2:
            #1. solicito la cedula que quiero buscar
            des = int(input("""1.Buscar por cedula
                            \r2.Buscar por nombre
                            \r3.Buscar por apellido
                            \r4.Buscar por nombre y apellido
                            \r:"""))
            if des == 1:
                c = int(input("Ingrese la cedula a buscar: ")) 
                p = sis.verDatosPacienteC(c) 
                if p != None:
                    print("Nombre: " + p.verNombre())
                    print("Cedula: " + str(p.verCedula())) 
                    print("Genero: " + p.verGenero()) 
                    print("Servicio: " + p.verServicio()) 
                else:
                    print("No existe un paciente con esa cedula")
            elif des == 2:
                n = input("Ingrese el nombre a buscar, tenga en cuenta que se mostraran todos los pacientes con ese nombre: ")
                p = sis.verDatosPacienteN(n)
                if p!= None:
                    for i in p:
                        print("Nombre: " + i.verNombre()) 
                        print("Cedula: " + str(i.verCedula())) 
                        print("Genero: " + i.verGenero()) 
                        print("Servicio: " + i.verServicio())
                else:
                    print("No existe un paciente con ese nombre")
            elif des == 3:
                a = input("Ingrese el apellido a buscar, tenga en cuenta que se mostraran todos los pacientes con ese apellido: ")
                p = sis.verDatosPacienteA(a)
                if p!= None:
                    for i in p:
                        print("Nombre: " + i.verNombre()) 
                        print("Cedula: " + str(i.verCedula())) 
                        print("Genero: " + i.verGenero()) 
                        print("Servicio: " + i.verServicio())
                else:
                    print("No existe un paciente con ese nombre")
            elif des == 4:
                na = input("Ingrese el nombre y apellido a buscar, tenga en cuenta que se mostraran todos los pacientes con ese nombre y apellido: ")
                p = sis.verDatosPacienteNA(na)
                if p!= None:
                    for i in p:
                        print("Nombre: " + i.verNombre()) 
                        print("Cedula: " + str(i.verCedula())) 
                        print("Genero: " + i.verGenero()) 
                        print("Servicio: " + i.verServicio())
                else:
                    print("No existe un paciente con ese nombre y apellido")
            else:
                print("Elija una opcion valida, volviendo al menu principal")
        elif opcion !=0:
            continue 
        else:
            break 

#aca el python descubre cual es la funcion principal
if __name__ == "__main__":
    main() 