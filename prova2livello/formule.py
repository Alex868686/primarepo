def somma_due_numeri(a:float,b:float=8):
    """questa funzione somma due numeri float e restituisce il risultato"""
    somma = a + b
    #print(somma)
    return somma

def formula_quadrato(a:float,b:float):
    area_quadrato=a*b
    #print(area_quadrato)
    return area_quadrato

def volume_cubo(a:float):
    "questa funzione restituisce il valore del parallelepipedo"
    volume=a**2
    #print(volume)
    return volume

class Rettangolo:

    def __init__(self,a,b):
        self.base = a
        self.altezza = b

    def area_rettangolo(self):
        return self.base*self.altezza

    def perimetro_rettangolo(self):
        return self.base*2+self.altezza*2

    def volume_parallelep(self,x):
        return self.area_rettangolo()*x

class Statistics:

    def __init__(self,a,b,c):
        "in ingresso a è il massimo, b il minimo, c la std"
        self.massimo = a
        self.minimo = b
        self.std_dev = c

    def mediana(self):
        "restituisce la mediana del range"
        return (self.massimo - self.minimo) / 2
    
    def range(self):
        "restituisce il range"
        return self.massimo - self.minimo
    
    def coefficiente_variazione(self,x):
        "restituisce il coefficente variazione e in ingresso richiede la max std"
        return self.mediana()*x
    



