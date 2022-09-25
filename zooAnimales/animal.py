from gestion.zona import Zona

class Animal:
    _totalAnimales=0
    def __init__(self, nombre, edad, habitat, genero, zona=None):
        self._nombre= nombre
        self._edad= edad
        self._habitat= habitat
        self._genero= genero
        self._zona= zona
        Animal._totalAnimales +=1
    
    def movimiento():
        return "desplazarse"
    
    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.mamifero import Mamifero
        return "Mamiferos: "+ Mamifero.cantidadMamiferos()
        from zooAnimales.ave import Ave
        return "Aves: "+ Ave.cantidadAves()
        from zooAnimales.reptil import Reptil
        return "Reptiles: "+ Reptil.cantidadReptiles()
        from zooAnimales.pez import Pez
        return "Peces: "+ Pez.cantidadPeces()
        from zooAnimales.anfibio import Anfibio
        return "Anfibios: "+ Anfibio.cantidadAnfibios()
    
    def toString(self):
        if self._zona != None:
            return "Mi nombre es "+self._nombre +"tengo una edad de "+ self._edad + "habito en " + self._habitat + "y mi genero es " + self._genero + "la zona en la que me ubico es "+ self._zona + "en el " + self._zoo
        else:
            return "Mi nombre es "+self._nombre +"tengo una edad de "+ self._edad + "habito en " + self._habitat + "y mi genero es " + self._genero
    
    def setNombre(self, nombre):
        self._nombre= nombre

    def getNombre(self):
        return self._nombre 
    
    def setEdad(self, edad):
        self._edad= edad

    def getEdad(self):
        return self._edad
    
    def setHabitat(self, habitat):
        self._habitat= habitat

    def getHabitat(self):
        return self._habitat 
    
    def setGenero(self, genero):
        self._genero= genero

    def getGenero(self):
        return self._genero
    
    def setZona(self, zona):
        self._zona[0]= zona

    def getZona(self):
        return self._zona[0] 
    
    