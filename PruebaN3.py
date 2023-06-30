import numpy as np

Nombre=[] #ValidarTexto
Apellido=[] #ValidarTexto
Rut=[] #ValidarNumero
Edad=[] #ValidarEdad
FechaNac=[] #ValidarNumero
Categoria=[] #ValidarCategoria
Celular=[] #ValidarCelular
Correo=[] #ValidarCorreo
Nombre2=[] #ValidarTexto
Apellido2=[] #ValidarTexto
Rut2=[] #ValidarNumero
Edad2=[] #ValidarEdad
FechaNac2=[] #ValidarNumero
Categoria2=[] #ValidarCategoria
Celular2=[] #ValidarCelular
Correo2=[] #ValidarCorreo
IdentificadorParejas=[] #ValidaTexto

def ValidarNumero(tipo,texto,vmin=None,vmax=None):
    while True:
        try:
            numero=tipo(input(texto))
            if vmin!=None and vmax!=None:
                if vmin<=numero<=vmax:
                    break 
                else:
                    print("No cumple con los rangos requeridos.")
            elif vmin!=None:
                if vmin<=numero:
                    break
                else:
                    print(f"El número debe se igual o mayor a {vmin}")
            elif vmax!=None:
                if vmax>=None:
                    break 
                else:
                    print(f"El número debe ser menor o igual a {vmax}")
            else:
                break
        except:
            print("Ingrese solo números!!")
    return numero

def ValidarTexto(texto):
    while True:
        nombre=input(texto)
        if nombre.isalpha():
            break
        else:
            print("Ingrese solamenete Letras")
    return nombre


def ValidarCelular(tipo,texto,vmin=None,vmax=None):
    while True:
        try:
            celular=tipo(input(texto))
            if vmin!=None and vmax!=None:
                if vmin<=len(str(texto))<=vmax:
                    break
                else:
                    print("No cumple los rangos necesarios")
            elif vmin!=None:
                if vmin<=len(str(texto)):
                    break
                else:
                    print(f"El número celular debe tener como minimo {vmin} digitos!!")
            elif vmax!=None:
                if vmax>=len(str(texto)):
                    break
                else:
                    print(f"El número celular debe tener como minimo {vmax} digitos!!")
            else:
                break
        except:
            print("Ingrese solamente números!!")
    return celular                    

def ValidarCorreo(texto,vmin=None,vmax=None):
    while True:
        try:
            correo=input(texto)
            if "@" in texto:
                if vmin!=None and vmax!=None:
                    if vmin<=len(correo)<=vmax:
                        break
                    else:
                        print("No cumple con los requerimientos necesarios el correo")
                elif vmin!=None:
                    if vmin<=len(correo):
                        break
                    else:
                        print(f"El correo debe tener minimo {vmin} digitos")
                elif vmax!=None:
                    if vmax>=len(correo):
                        break
                    else:
                        print(f"El correo debe tener máximo {vmax} digitos")
                else:
                    break
            else:    
                print("El correo debe tener @ !!")
        except:
            print("No cumple con los requqerimientos necesarios")
    return correo

def ValidarCategoria(texto): 
    while True:
        categoria=input(texto).lower()
        if categoria=="oro" or categoria=="plata" or categoria=="bronce":
            break
        else:
            print("Ingrese solamente opciones validas")
    return categoria

def BuscarJugador(texto):
    for i in range(len(texto)):
        print(f"Nombre: {Nombre[i]} \nCategoria: {Categoria[i]} \nFono: {Celular[i]} \nCorreo: {Correo[i]}")
    
def VerEquipos(texto):
    for i in range(len(texto)):
        print(f"1.- Nombre: {Nombre[i]} \n2.- Nombre: {Nombre2[i]}")


def menu():
    while True:
        print("-- Campeonato de Padel --")
        print("-"*30)
        print("1.- Inscripción de Jugadores")
        print("2.- Buscar Jugador")
        print("3.- Ver Equipos")
        print("4.- Salir")
        opc=ValidarNumero(int,"Seleccione una opción: ",1,4)
        if opc==1:
            print("Datos primer Jugador")
            nombre=ValidarTexto("Ingrese nombre su nombre: ")
            Nombre.append(nombre)
            apellido=ValidarTexto("Ingrese su apellido: ")
            Apellido.append(apellido)
            rut=ValidarNumero(int,"Ingrese su rut: ")
            Rut.append(rut)
            edad=ValidarNumero(int,"Ingrese su edad: ",1,80)
            Edad.append(edad)
            fechanac=ValidarNumero(int,"Ingrese su fecha de nacimiento: ")
            FechaNac.append(fechanac)
            categoria=ValidarCategoria("Seleccione la cetegoria [Oro/Plata/Bronce]: ")
            Categoria.append(categoria)
            celular=ValidarCelular(int,"Ingrese su número de celular: ",9)
            Celular.append(celular)
            correo=ValidarCorreo("Ingrese su correo: ",6)
            Correo.append(correo)
            print("-"*30)
            print("Datos segundo jugador")
            nombre=ValidarTexto("Ingrese nombre su nombre: ")
            Nombre2.append(nombre)
            apellido=ValidarTexto("Ingrese su apellido: ")
            Apellido2.append(apellido)
            rut=ValidarNumero(int,"Ingrese su rut [sin guion ni digito verificador]: ", 10000000,30000000)
            Rut2.append(rut)
            edad=ValidarNumero(int,"Ingrese su edad: ",1,80)
            Edad2.append(edad)
            fechanac=ValidarNumero(int,"Ingrese su fecha de nacimiento: ")
            FechaNac2.append(fechanac)
            categoria=ValidarCategoria("Seleccione la cetegoria [Oro/Plata/Bronce]: ")
            Categoria2.append(categoria)
            celular=ValidarCelular(int,"Ingrese su número de celular: ",9)
            Celular2.append(celular)
            correo=ValidarCorreo("Ingrese su correo: ",6)
            Correo2.append(correo)
            print("-"*30)
            identificadorparejas=ValidarTexto("Ingrese nombre al equipo [solo letras]: ")
            IdentificadorParejas.append(identificadorparejas)
            print("Datos ingresados correctamente")
        elif opc==2:
            BuscarJugador()
        elif opc==3:
            VerEquipos()
        elif opc==4:
            print("Saliendo del sistema...")
            break


menu()