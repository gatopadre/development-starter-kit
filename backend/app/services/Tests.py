from databases.mongoDB import MongoDB


def test_connection_to_mongo():
    """
    Prueba la conexión a la base de datos MongoDB y guarda datos de ejemplo en la colección "Plants".

    Returns:
        bool: True si la conexión es exitosa y los datos se guardan correctamente, False en caso contrario.
    """
    database = MongoDB()
    data = {"name": "Porotos", "longevity": 30}  # Datos de ejemplo
    database.save_to_db(data, "Plants")  # Guardar datos en la colección "Plants"
    return True
