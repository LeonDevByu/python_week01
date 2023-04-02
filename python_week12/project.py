listaasistente = []


class asistenciaclases(object):
    def __init__(self, codigo, nombre, apellido1, apellido2, perfil, curso, asiste):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.perfil = perfil
        self.curso = curso
        self.asiste = asiste
        self.total = asiste

        self.detalle = []

    def registros(self):
        print("CODIGO: {}| NOMBRE:{} {} {} | PERFIL: {} | CURSO: {} |N° DE ASISTENCIA: {}".format(self.codigo,
                                                                                                   self.nombre,
                                                                                                  self.apellido1,
                                                                                                  self.apellido2,
                                                                                                   self.perfil,
                                                                                                   self.curso,
                                                                                                   self.asiste))

    def asistencia(self, asiste):
        sald = self.total
        self.asiste = asiste
        self.total = sald + 1
        self.detalle = []
        print("ASISTENCIA REGISTRADA\n")

    def incluirtransaccion(self, asiste):
        return "N° DE ASISTENCIAS: {}\n TOTAL:{}".format(self.asiste, self.total)

def registropersonal():
    print("REGISTRO DE PERSONAL")
    codigo = int(input("\nDIGITE EL NUMERO DE DOCUMENTO, ESTE SERA SU CODIGO\n"))
    nombre = str(input("\nNOMBRE\n"))
    apellido1 = str(input("\nPRIMER APELLIDO\n"))
    apellido2 = str(input("\nSEGUNDO APELLIDO\n"))
    perfil = str(input("\nESCRIBA E, PERFIL: ESTUDIANTE, PROFESOR O ADMINISTRATIVO\n"))
    curso = str(input("\nCURSO O MATERIA EN LETRA\n"))
    asiste = 1

    v = asistenciaclases(codigo,nombre,apellido1,apellido2,perfil,curso,asiste)
    listaasistente.append(v)
    print("REGISTRO EXITOSO\n")


def listadopersonal():
    print("LISTA DE PERSONAL")
    for v in listaasistente:
        v.registros()


def buscapersonal():
    print("BUSCA PERSONAL")
    codigo = int(input("\nCODIGO\n"))
    for v in listaasistente:
        if codigo == v.codigo:
            v.registros()


def controlasistencia():
    print("Iniciando transaccion")
    codigo = int(input("\nCODIGO\n"))
    for v in listaasistente:
        if codigo == v.codigo:
            asiste = 0
            v.asistencia(asiste)
            v.registros()
            recepcionmensaje = v.incluirtransaccion(asiste)
            v.detalle.append(recepcionmensaje)


def historial():
    print("ASISTENCIA")
    codigo = int(input("\n CODIGO\n"))
    for v in listaasistente:
        if codigo == v.codigo:
            for recepcionmensaje in v.detalle:
                print("DIA ANTERIOR:{}".format(recepcionmensaje))


def salir():
    print("\nGRACIAS POR USAR NUESTRO SERVICIO\n")
    exit()


def main():
    while True:
        print("\nBIEVENIDO AL COLEGIO EMVV\n")
        opciones = int(input("\n QUE OPERACION DESEA REALIZAR?"
                             "\nOPRIME 1 PARA REGISTRAR NUEVO PERSONAL"
                             "\nOPRIME 2 PARA CONSULTAS"
                             "\nOPRIME 3 PARA CONTROL DE ASISITENCIA"
                             "\nOPRIME 4 PARA VER LISTA DE PERSONAL"
                             "\nOPRIME 5 PARA VER ULTIMA ASISTENCIA"
                             "\nOPRIME 6 PARA SALIR\n"))

        if opciones == 1:
            registropersonal()
        if opciones == 2:
            buscapersonal()
        if opciones == 3:
            controlasistencia()
        if opciones == 4:
            listadopersonal()
        if opciones == 5:
            historial()
        if opciones == 6:
            salir()


if __name__ == "__main__":
    main()
