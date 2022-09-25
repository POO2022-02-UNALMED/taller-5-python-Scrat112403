class Zoologico:
    def __init__(self,nombre, ubicacion):
        self._nombre: nombre
        self._ubicacion: ubicacion
        self._zonas: []
    
    def agregarzonas(self, zona):
        self._zonas.append(zona)
    
    def cantidadTotalAnimales(self):
        return sum([i.cantidadAnimales() for i in self._zonas])
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre= nombre
    
    
    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, ubi):
        self._ubicacion= ubi
    
    def getZonas(self):
        return self._zonas
    
    def setZonas(self, zona):
        self._zonas= zona

