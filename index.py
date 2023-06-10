class Rectangulo:
    def __init__(self, anchura, altura):
        self.anchura = anchura
        self.__altura = altura
    def area(self):
        return self.anchura * self.__altura
    def estableceAltura(self, altura):
        self.__altura = altura