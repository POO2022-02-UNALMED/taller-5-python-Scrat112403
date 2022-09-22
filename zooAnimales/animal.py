from gestion.zona import Zona

class Animal:
    _totalAnimales=0
    def __init__(self, nombre, edad, habitat, genero, zona=None):
        self._nombre: nombre
        self._edad: edad
        self._habitat: habitat
        self._genero: genero
        self._zona:zona
        Animal._totalAnimales +=1
    
    def movimiento():
        return "desplazarse"
    
    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.mamifero import Mamifero
        return "Mamiferos: "+ Mamifero.cantidadMamiferos()
        return "Aves: "+
        return "Reptiles: "+
        return "Peces: "+
        return "Anfibios: "+
    
    def toString(self):
        if self._zona != None:
            return "Mi nombre es "+self._nombre +"tengo una edad de "+ self._edad + "habito en " + self._habitat + "y mi genero es " + self._genero + "la zona en la que me ubico es "+ self._zona + "en el " + self._zoo
        else:
            return "Mi nombre es "+self._nombre +"tengo una edad de "+ self._edad + "habito en " + self._habitat + "y mi genero es " + self._genero