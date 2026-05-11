class Producto:
    '''
    30/04/2026

    AUTORES:
    Yulisa Otero
    Sebastian Murillo

    Esta clase se encarga de contener la información de la entidad "Producto"
    pidiendo y almacenando los atributos de cada producto.
    '''

    nombre_producto:str ; codigo_producto:int ; categoria_producto:int ; precio_sin_iva:float ; costo_adquisicion:float ; porcentaje_iva:float ; stock:int ; proveedor_asociado:str

    def __init__(self, nombre:str="", costo:float=0.0, codigo:int=0, precio:float=0.0, categoria:int=0, iva:float=0.0, proveedor:str="No Aplica"):
        '''
        30/04/2026

        AUTORES:
        Yulisa Otero
        Sebastian Murillo

        Este es el método constructor de la clase; sirve para inicializar los atributos.

        PARAM:
        Nombre, costo, codigo, precio, categoria, iva, proveedor.

        RETURN:
        No aplica.
        '''

        ALIMENTOS=1 ; BEBIDAS=2 ; PRODUCTOS_ASEO=3; PAPELERIA=4; BIENES_USO_FRECUENTE=5
        self.nombre_producto=nombre
        self.codigo_producto=codigo
        self.precio_sin_iva=precio
        self.categoria_producto=categoria
        self.costo_adquisicion=costo
        self.porcentaje_iva=iva
        self.stock=0
        self.proveedor_asociado=proveedor

    def pedir_datos(self):
        '''
        30/04/2026

        AUTORES:
        Yulisa Otero
        Sebastian Murillo

        Este método es para que la clase pida los datos del producto  y así almacenarlos.

        PARAM:
        No aplica.

        RETURN:
        No aplica.
        '''

        opc=0
        while opc!=1:
            try:
                self.categoria_producto=int(input("Ingrese el número de la categoría a la que pertenece el producto: \n1) Alimentos \n2) Bebidas \n3) Productos de aseo \n4) Papeleria \n5) Bienes de uso frecuente \n\n"))
                if self.categoria_producto>0 and self.categoria_producto<6:
                  self.nombre_producto=input("Ingrese el nombre del producto: ")
                  if self.nombre_producto!="":
                    self.codigo_producto=int(input("Ingrese el codigo del producto: "))
                    if self.codigo_producto<=99999 and self.codigo_producto>0:
                      self.costo_adquisicion=float(input("Ingrese el costo de adquisición del producto: "))
                      if self.costo_adquisicion>0:
                        self.precio_sin_iva=float(input("Ingrese el precio del producto: "))
                        if self.precio_sin_iva>self.costo_adquisicion:
                          self.porcentaje_iva=float(input("Ingrese el porcentaje de IVA asociado al producto (entre 0 y 100): "))
                          if self.porcentaje_iva>=0 and self.porcentaje_iva<=100:
                            self.porcentaje_iva/=100
                            self.stock=int(input("Ingrese la cantidad de producto ingresado: "))
                            if self.stock>0:
                                self.proveedor_asociado=input("Ingrese el proveedor asociado al producto")
                                if self.proveedor_asociado!="":
                                    opc+=1
                                else:
                                    print("El nombre del proveedor inválido")
                            else:
                              print("La cantidad ingresada no es válida")
                          else:
                            print("El porcentaje de IVA ingresado no es válido")
                        else:
                          print("El precio ingresado no es válido")
                      else:
                        print("El costo ingresado no es válido")
                    else:
                      print("El código ingresado no es válido")
                  else:
                    print("El nombre ingresado no es válido")
                else:
                  print("La categoría ingresada no es válida")
            except ValueError:
                print("Introduzca un valor válido")        
