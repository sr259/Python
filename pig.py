from cs1graphics import *

class Pig(Layer):
    def __init__(self, scale, px, py, color):
        """
        The pigs original size is going to be around 100 pixels wide and about 125 tall. The scale
        parameter will allow you to choose how large or small you want your pig to
        be in corelation of the size of the original pig. Px and Py are the initial points
        you want the pig to be on the Canvas. The color is what color you want the pig.
        """
        super().__init__()
        self._scale = scale
        self._px = px
        self._py = py
        self._color = color
        self._emotionless = True
        #Making the pig
        #body
        self._body = Circle(50 * self._scale, Point(self._px,self._py))
        self._body.setFillColor(self._color)
        #feet
        self._foot1 = Rectangle(20 *self._scale, 25 * self._scale, Point(self._px - ( 20*self._scale), self._py + (50* self._scale)))
        self._foot1.setFillColor(self._color)
        self._foot2 = self._foot1.clone()
        self._foot2.moveTo(self._px + (15 * self._scale), self._py +(50 * self._scale))
        # Head
        self._head = Circle(30 * self._scale, Point(self._px, self._py - (25 * self._scale)))
        self._head.setFillColor(self._color)
        # Ears
        self._earleft = Polygon(Point(self._px - (20 * self._scale), self._py - (72 * self._scale)), Point(self._px - (5 * self._scale), self._py - (50 * self._scale)), Point(self._px - (20 * self._scale), self._py - (40 * self._scale)))
        self._earleft.setFillColor(self._color)
        self._earright = self._earleft.clone()
        self._earright.flip()
        self._earright.moveTo(self._px + (20 * self._scale), self._py - ( 70 * self._scale))
        #eyes
        self._eyeleft = Circle(5*self._scale, Point(self._px -( 10 * self._scale), self._py - (33 * self._scale)))
        self._eyeleft.setFillColor('white')
        self._eyeright =self._eyeleft.clone()
        self._eyeright.moveTo(self._px + (10 * self._scale), self._py - (33 * self._scale))
        #nose
        self._nose = Circle(8 * self._scale, Point(self._px, self._py - (20 * self._scale)))
        self._nose.setFillColor(self._color)
        self._nostril1 = Circle(1 * self._scale, Point(self._px - (3 * self._scale), self._py -(20* self._scale)))
        self._nostril1.setFillColor('black')
        self._nostril2 = self._nostril1.clone()
        self._nostril2.moveTo(self._px + (3 * self._scale), self._py - (20 * self._scale))

        #adding the parts together
        self.add(self._body)
        self.add(self._foot1)
        self.add(self._foot2)
        self.add(self._head)
        self.add(self._earleft)
        self.add(self._earright)
        self.add(self._eyeleft)
        self.add(self._eyeright)
        self.add(self._nose)
        self.add(self._nostril1)
        self.add(self._nostril2)
        self.adjustReference(self._px, self._py)

    def angry(self):
        """
        This just makes the pig look angry by adding eyebrows.
        """
        if self._emotionless == False:
            self.remove(self._eyebrow1)
            self.remove(self._eyebrow2)
        self._eyebrow1 = Path(Point(self._px - (15* self._scale), self._py - (45 * self._scale)), Point(self._px - (5 * self._scale), self._py - (35 * self._scale)))
        self._eyebrow2 = Path(Point(self._px + (5 * self._scale), self._py - (35 * self._scale)), Point(self._px + (15 * self._scale), self._py - (45 *self._scale)))
        self._eyebrow1.setBorderWidth(3 * self._scale)
        self._eyebrow2.setBorderWidth(3 * self._scale)
        self.add(self._eyebrow1)
        self.add(self._eyebrow2)
        self._emotionless = False
    def unamused(self):
        """
        Makes the pig look unamused by changing the style of the eyebrows.
        """
        if self._emotionless == False:
            self.remove(self._eyebrow1)
            self.remove(self._eyebrow2)
        self._eyebrow1 = Path(Point(self._px - (15* self._scale), self._py - (45 * self._scale)), Point(self._px - (5 * self._scale), self._py - (45 * self._scale)))
        self._eyebrow2 = Path(Point(self._px + (5 * self._scale), self._py - (45 * self._scale)), Point(self._px + (15 * self._scale), self._py - (45 *self._scale)))
        self._eyebrow1.setBorderWidth(3 * self._scale)
        self._eyebrow2.setBorderWidth(3 * self._scale)
        self.add(self._eyebrow1)
        self.add(self._eyebrow2)
        self._emotionless = False
    def surprised(self):
        """
        Makes the pig look surprised by chnging the style of the eyebrows.
        """
        if self._emotionless == False:
            self.remove(self._eyebrow1)
            self.remove(self._eyebrow2)
        self._eyebrow1 = Path(Point(self._px - (18* self._scale), self._py - (35 * self._scale)), Point(self._px - (5 * self._scale), self._py - (45 * self._scale)))
        self._eyebrow2 = Path(Point(self._px + (5 * self._scale), self._py - (45 * self._scale)), Point(self._px + (18 * self._scale), self._py - (35 *self._scale)))
        self._eyebrow1.setBorderWidth(3 * self._scale)
        self._eyebrow2.setBorderWidth(3 * self._scale)
        self.add(self._eyebrow1)
        self.add(self._eyebrow2)
        self._emotionless = False
    def blank(self):
        """
        Makes the pig expressionless.
        """
        if self._emotionless == False:
            self.remove(self._eyebrow1)
            self.remove(self._eyebrow2)
        self._emotionless = True
    def eyeColor(self, color):
        """
        Change the color of the pig's eyes by putting a color as the parameter.
        """
        self._eyeright.setFillColor(color)
        self._eyeleft.setFillColor(color)

        
        
        

if __name__ == '__main__':
    paper = Canvas(1000,1000, 'white')
    pig1 = Pig(1,100,100,'blue')
    pig2 = Pig(.2,750,750,'purple')
    pig3 = Pig(3, 700,200, 'red')
    pig4 = Pig(5, 300,750, 'pink')
    pig1.angry()
    pig4.surprised()
    pig3.unamused()
    pig1.eyeColor('red')
    pig3.eyeColor('green')
    paper.add(pig1)
    paper.add(pig2)
    paper.add(pig3)
    paper.add(pig4)
   

    
