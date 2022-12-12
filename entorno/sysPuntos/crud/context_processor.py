def total_carrito(request):
    total = 0
    contador = 0
    descuento = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
                contador += int(value["cantidad"])
    descuento = int(total * 0.93)
    porcentaje = int( total * 0.07 )           
    return {"total_carrito": total, "total_contador": contador, "descuento" : descuento, "porcentaje" : porcentaje}