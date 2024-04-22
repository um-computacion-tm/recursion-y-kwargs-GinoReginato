def buscar_datos(*args, **kwargs):
    datos_encontrados = []
    
    if "database" in kwargs:
        database = kwargs["database"]
        for arg in args:
            found = False
            for key, data in database.items():
                if arg in data.values():
                    datos_encontrados.append(arg)
                    found = True
                    break 
            if not found:
                print(f"La palabra '{arg}' no está en la base de datos.")
    
    print("Datos encontrados en la base de datos:", datos_encontrados)
    return datos_encontrados


database = {
    "persona1": {
        "primer_nombre": "Juan",
        "segundo_nombre": "Pablo",
        "primer_apellido": "Carini",
        "segundo_apellido": "Perez"
    },
    
    "persona2": {
        "primer_nombre": "Gino",
        "segundo_nombre": "Piero",
        "primer_apellido": "Reginato",
        "segundo_apellido": "fugazzotto"
    }
}

buscar_datos("Gino", "Juan", "Ruiz", "Picasso", database=database)
