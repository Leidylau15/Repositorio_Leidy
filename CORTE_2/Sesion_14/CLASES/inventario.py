def reducir_inventario(inv,nuevos):
    nuevos=crear_inventario(nuevos)
    for elemento in nuevos:
        if elemento not in inv:
            inv[elemento]=nuevos[elemento]
        else:
            if (inv[elemento]-nuevos[elemento])<0:
                inv[elemento]=0
            else:
                inv[elemento]-=nuevos[elemento]
    return inv