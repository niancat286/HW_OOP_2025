AVAILABLE_FIGURES_2D = ['Triangle', 'Rectangle', 'Trapeze',
                        'Parallelogram', 'Circle']

AVAILABLE_FIGURES_3D = ['Ball', 'TriangularPyramid', 'QuadrangularPyramid',
                        'RectangularParallelepiped', 'Cone', 'TriangularPrism']

class Figure:
    def __init__(self):
        pass

    def dimension(self):    #повертає вимірність фігури
        return None

    def perimetr(self):     #повертає периметр фігури для дво-вимірних фігур
        return None

    def square(self):   #повертає площу фігури для дво-вимірних фігур
        return None

    def squareSurface(self):    #повертає площу бічної фігури для три-вимірних фігур
        return None

    def squareBase(self):   #повертає площу основи фігури для три-вимірних фігур
        return None

    def height(self): #повертає висоту фігури для три-вимірних фігур
        return None

    def volume(self):   #що обчислює міру фігури (для плоскої фігури – площу, для об’ємної – відповідно об’єм)
        return None

