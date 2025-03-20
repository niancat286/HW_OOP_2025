from Figure import Figure

class Figure2D(Figure):
    def perimetr(self):     #повертає периметр фігури для дво-вимірних фігур
        pass

    def square(self):   #повертає площу фігури для дво-вимірних фігур
        pass

    def squareSurface(self):    #повертає площу бічної фігури для три-вимірних фігур
        return None

    def squareBase(self):   #повертає площу основи фігури для три-вимірних фігур
        return None

    def height(self): #повертає висоту фігури для три-вимірних фігур
        return None

    def volume(self):   #що обчислює міру фігури (для плоскої фігури – площу, для об’ємної – відповідно об’єм)
        pass