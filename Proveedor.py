class Proveedor:
    nombre:str; documento:int; num_celular:int
    direccion:str; correo:str

    def __init__(self, documento:int):
        self.nombre=""
        self.documento=documento
        self.num_celular=0
        self.dirrecion=""
        self.correo=""

    def pedir_datos(self) ->None:
        try:
            self.nombre=input("ingrese su nombre")
            self.documento=int(input(""))
        except: ValueError     
        