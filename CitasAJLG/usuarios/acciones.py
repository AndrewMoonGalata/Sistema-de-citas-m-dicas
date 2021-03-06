import usuarios.usuario as modelo
import consultorios.acciones as consultorio
import consultorios.consultorio as conscon
import doctores.acciones as doctor
import doctores.doctor as doct
import citas.acciones as cita

class Acciones:

    def registro(self):
        print("Se procedera a realizar tu registro en el sistema...")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente!!")

    def login(self):
        print("Identificate en el sistema...")

        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario('', '', email, password).identificar()

        if usuario[0] >= 1:
            print(f"\nBienvenido de nuevo {usuario[1][1]}! Te has registrado el {usuario[1][5]}\n")
            self.proximasAcciones(usuario)
        else:
            print("\nEmail o password incorrectos!!")
    
    def proximasAcciones(self, usuario):
        print(""" Acciones disponibles:

        1. Añadir un consultorio ---- [registrarConsultorio]
        2. Ver consultorio ------ [mostrarConsultorio]
        3. Eliminar consultorio ----- [eliminarConsultorio]
        4. Añadir doctor --------- [registrarDoctor]
        5. Ver doctores registrados ----------- [mostrarDoctor]
        6. Eliminar doctor ---------- [eliminarDoctor]
        7. Añadir cita ----------- [registrarCita]
        8. Ver cita ------------- [mostrarCita]
        9. Eliminar cita ------------ [eliminarCita]
        0. Salir -------------------- [salir]
        
        """)

        accion = input("¿Que desea hacer?: ")
        consult = consultorio.Acciones()
        doctr = doctor.Acciones()
        citas = cita.Acciones()

        if accion == "registrarConsultorio":
            consult.crear(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "mostrarConsultorio":
            consult.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "eliminarConsultorio":
            consult.eliminar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "registrarDoctor":
            if len(conscon.Consultorio().listar()) == 0:
                print("Necesitas crear un consultorio primero")
                self.proximasAcciones(usuario)
            else:
                doctr.crear(usuario)
                self.proximasAcciones(usuario)
        
        elif accion == "mostrarDoctor":
            doctr.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "eliminarDoctor":
            doctr.eliminar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "registrarCita":
            if len(doct.Doctor().listar()) == 0:
                print("Necesitas crear un consultorio primero")
                self.proximasAcciones(usuario)
            else:
                citas.crear(usuario)
                self.proximasAcciones(usuario)
        
        elif accion == "mostrarCita":
            citas.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "eliminarCita":
            citas.eliminar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "salir":
            exit()