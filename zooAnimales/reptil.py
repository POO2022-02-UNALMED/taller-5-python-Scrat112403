from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado: []
    iguanas=0
    serpientes=0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas: colorEscamas
        self._largoCola: largoCola
        Reptil._listado.append(self)
    
    def movimiento(self):
        return "arrastrarse"
    
    @classmethod
    def cantidadReptiles(cls):
        return len(Reptil._listado)
    
    @classmethod
    def crearIguana(cls, nombre, edad, habitat, genero):
        Reptil.iguanas+=1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, habitat, genero):
        Reptil.serpientes+=1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)
    
    def getListado(cls):
        return Reptil._listado
    
    def setListado(cls, listado):
        Reptil._listado= listado

    
    