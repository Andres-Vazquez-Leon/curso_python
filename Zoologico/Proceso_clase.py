import csv
import json
class Proceso_clase:
    def __init__(self, Clase_id, Clase_tipo):
        self.Clase_id = Clase_id
        self.Clase_tipo = Clase_tipo

    def __str__(self):
        return f"Proceso_clase: id = {self.Clase_id}, tipo = {self.Clase_tipo}"
    def __repr__(self):
        return f"Proceso_clase(Clase_id = {self.Clase_id}, Clase_tipo = {self.Clase_tipo})" 
    
    

    """Crear achivo json y nombrarlo como clase animal"""
    
    def crear_json(self, data, file_path):
        print ("clase Proceso_clase, metodo crear_json")
        import json
        with open(file_path, mode='w') as file:
            json.dump(data, file, indent=4)  

"""cargar el archivo json en una lista string"""
def cargar_json(file_path):
    print ("clase Proceso_clase, metodo cargar_json")
    import json
    with open(file_path, mode='r') as file:
        data = json.load(file)
    return data

"""crear archivo json con datos de clases.csv y guardarlo como clase-animal.json"""
def crear_json_clase_animal(file_path, nombre_archivo_json):

    data = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    with open(nombre_archivo_json, mode='w') as file:
        json.dump(data, file, indent=4)

"""crea un diccionario con los animales de zoo.json y Clase_tipo de clase-animal.json que corresponda con la Clase_id de clase-animal.json"""
def crear_diccionario_zoo_clase_animal(file_path_zoo, file_path_clase_animal):
    print ("clase Proceso_clase, metodo crear_diccionario_zoo_clase_animal")
    with open(file_path_zoo, mode='r') as file:
        data_zoo = json.load(file)
    with open(file_path_clase_animal, mode='r') as file:
        data_clase_animal = json.load(file)
    diccionario = {}
    for animal in data_zoo:
        for clase in data_clase_animal:
            if animal["Clase_id"] == clase["Clase_id"]:
                diccionario[animal["Nombre"]] = clase["Clase_tipo"]
    return diccionario

    

if __name__ == "__main__":
    """llama al metodo imprimir_json para mostrar el contenido del archivo json creado con los datos de clases.csv"""
    """dar como parametro a crear_json_clase_animal el nombre del archivo csv y a imprimir_json el nombre del archivo json creado"""
    crear_json_clase_animal('clases.csv', 'clase-animal.json')
    data = cargar_json('clase-animal.json')
    crear_json_clase_animal('zoo.csv', 'zoo.json')
    data = cargar_json('zoo.json')
    print(json.dumps(data, indent=4))



