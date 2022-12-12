class Listado:
    
    def __init__(self, request):
        self.request = request
        self.session = request.session
        lista = self.session.get("lista")
        if not lista:
            self.session["lista"] = {}
            self.lista = self.session["lista"]
        else:
            self.lista = lista
        
            
    def agregar(self, productos, venta_id, detalle_pedido):
        
        #id = str(venta_id)
        #pro = productos.object.get(id = detalle.id_producto)
        
        detalle = detalle_pedido.objects.filter(id_pedido = venta_id)
        for dv in detalle:
            
            id = str(dv.id)
            print("dentro de vs") 
            if id not in self.lista.keys():
                pro = productos.objects.get(id = dv.id_producto_id)
                self.lista[id]={
                    "id_venta" : venta_id, 
                    "pro_id" : dv.id_producto_id,
                    "nombre_producto": pro.nom_producto,
                    "cantidad": dv.cantidad,
                    "precio": dv.precio,
                    #"opcion": "historial",
                }
                
                self.guardar()
        return print(detalle)
        

    def guardar(self):
        self.session["lista"] = self.lista
        self.session.modified = True  
        return print("guardando session")
        
        
    def limpiar(self, detalle, venta_id):
        detalle_venta = detalle.objects.filter(id_pedido = venta_id)
        for dv in detalle_venta:
            id = str(dv.id)
            if id in self.lista.keys():
                del self.session["lista"][id]
                self.session.modified = True 
        #self.session["lista"] = {}
        #self.session.modified = True  