AVAILABLE_FIGURES_2D = ['Triangle', 'Rectangle', 'Trapeze',
                        'Parallelogram', 'Circle']

AVAILABLE_FIGURES_3D = ['Ball', 'TriangularPyramid', 'QuadrangularPyramid',
                        'RectangularParallelepiped', 'Cone', 'TriangularPrism']

class Figure:
    def __init__(self, ):
        pass

    def dimention(self):    #повертає вимірність фігури
        pass

    def perimetr(self):     #повертає периметр фігури для дво-вимірних фігур
        pass

    def square(self):   #повертає площу фігури для дво-вимірних фігур
        pass

    def squareSurface(self):    #повертає площу бічної фігури для три-вимірних фігур
        pass

    def squareBase(self):   #повертає площу основи фігури для три-вимірних фігур
        pass

    def height(self): #повертає висоту фігури для три-вимірних фігур
        pass

    def volume(self):   #що обчислює міру фігури (для плоскої фігури – площу, для об’ємної – відповідно об’єм)
        pass