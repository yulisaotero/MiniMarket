class Producto:
    nombre_producto:str ; codigo_producto:int ; categoria:int ; precio_sin_iva:float ; costo_adquisicion:float ; porcentaje_iva:float ; stock:int ; proveedor_asociado:str
 
    def __init__(self, nombre:str, costo: float, codigo:int, precio:float, categoria:int, iva:float, proveedor:str):
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
        categoria=int(input("Ingrese el número de la categoría a la que pertenece el producto: \n1) Alimentos \n2) Bebidas \n3) Productos de aseo \n4) Papeleria \n5) Bienes de uso frecuente"))
        nombre=input("Ingrese el nombre del producto: ")
        codigo=int(input("Ingrese el codigo del producto: "))
        costo=float(input("Ingrese el costo de adquisición del producto: "))
        precio=float(input("Ingrese el precio del producto: "))
        iva=float(input("Ingrese el porcentaje dde IVA asociado al producto: "))
        self.stock=int(input("Ingrese la cantidad de producto ingresado: "))
        proveedor:input("Ingrese el nombre del proveedor asociado al producto: ")        
