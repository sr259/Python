from cs1graphics import *
from time import sleep


paper = Canvas(500,500, 'skyblue')
grass = Rectangle(500,200, Point(250,400))
grass.setFillColor('green')
paper.add(grass)
#Sprites and characters
#trees and mud
tree = Layer()
leaves = Polygon(Point(150,150),Point(75,350),Point(225,350))
leaves.setFillColor('darkGreen')
trunk = Rectangle(50,100, Point(150,350))
trunk.setFillColor('brown')
tree.add(trunk)
tree.add(leaves)
paper.add(tree)

tree2 = Layer()
hole = Circle(15,Point(-100,375))
hole.setFillColor('Transparent')
hole.setBorderColor('chocolate')
hole.setBorderWidth(3)
leaves2 = Circle(100, Point(-100,250))
leaves2.setFillColor('darkGreen')
trunk2 = Rectangle(75,100, Point(-100,370))
trunk2.setFillColor('brown')

tree2.add(trunk2)
tree2.add(hole)
tree2.add(leaves2)
paper.add(tree2)

mud = Rectangle(120, 80, Point(400,400))
mud.setFillColor('brown')
paper.add(mud)

#pig
pig = Layer()
body = Circle(50, Point(400,350))
body.setFillColor('pink')

foot1 = Rectangle(20, 25, Point(380,400))
foot1.setFillColor('pink')
foot2 = foot1.clone()
foot2.moveTo(415,400)

head = Circle(30, Point(400,325))
head.setFillColor('pink')

earleft = Polygon(Point(380,278),Point(395,300),Point(380,310))
earleft.setFillColor('pink')
earright = earleft.clone()
earright.flip()
earright.moveTo(420,280)

eyeleft = Circle(5, Point(390,317))
eyeleft.setFillColor('white')

eyeright = eyeleft.clone()
eyeright.moveTo(410,317)

nose = Circle(8, Point(400,330))
nose.setFillColor('pink')

nostril1 = Circle(1, Point(397,330))
nostril1.setFillColor('black')
nostril2 = nostril1.clone()
nostril2.moveTo(403,330)


####angry eyebrows
eyebrow1 = Path(Point(385,305),Point(395,315))
eyebrow2 = Path(Point(405,315),Point(415,305))
eyebrow1.setBorderWidth(3)
eyebrow2.setBorderWidth(3)


pig.add(body)
pig.add(foot1)
pig.add(foot2)
pig.add(head)
pig.add(earleft)
pig.add(earright)
pig.add(eyeleft)
pig.add(eyeright)
pig.add(nose)
pig.add(nostril1)
pig.add(nostril2)
pig.adjustReference(400,350)



#Bird
bird = Layer()

tail = Polygon(Point(115,210),Point(85,190),Point(85,230))
tail.setFillColor('purple')
tail.setBorderColor('purple')

torso = Circle(24, Point(120,210))
torso.setFillColor('purple')
torso.setBorderColor('purple')

birdhead = Circle(15, Point(150,210))
birdhead.setFillColor('purple')

beak = Polygon(Point(175,210),Point(160,205),Point(160,215))
beak.setFillColor('orange')

eye = Circle(4, Point(153,205))
eye.setFillColor('white')

eye2= Path(Point(149,205),Point(157,205))
eye2.setBorderWidth(2)

feet = Polygon(Point(120,234),Point(115,241),Point(125,241))
feet.setFillColor('orange')

wing = Polygon(Point(117.5,250),Point(105,210),Point(130,210))
wing.setFillColor('purple')

eyebrow = Path(Point(145,205),Point(158,193))
eyebrow.setBorderWidth(3)

bird.add(feet)
bird.add(tail)
bird.add(torso)
bird.add(birdhead)
bird.add(beak)
bird.add(eye)
bird.add(wing)
bird.adjustReference(120,210)
#Electrical Post
post = Layer()
base = Rectangle(30,375, Point(-100,250))
base.setFillColor('brown')

wireholder = Rectangle(35,35,Point(-100,110))
wireholder.setFillColor('grey')

wire = Path(Point(-100,110),Point(-1000,110))

post.add(wire)
post.add(base)
post.add(wireholder)
paper.add(post)

#Animation

#Pig Moving In
delay = .20
pig.moveTo(500,350)
paper.add(pig)

x=0
while x!=5:
    x =x +1
    pig.rotate(-10)
    pig.move(-10,0)
    sleep(delay)
    pig.rotate(10)
    pig.move(-10,0)
    sleep(delay)

#Bird Moving In
bird.moveTo(-120,-210)
paper.add(bird)
wing.adjustReference(0,-30)
x=0
delay = .1
while x !=60:
    x =x +1
    bird.move(4,7)
    wing.rotate(180)
    sleep(delay)

#bird makes pig angry
text1 =Layer()
meanText = Text("Gosh Pig, you sure are fat and lazy.",12)
meanText2 = Text("All you do is sit in the mud and sleep.",12)
meanText2.move(0,30)
text1.add(meanText)
text1.add(meanText2)
text1.moveTo(300,100)
paper.add(text1)
sleep(5)
paper.remove(text1)

#pig remark
pig.add(eyebrow1)
pig.add(eyebrow2)
text2 = Text("Hey, say that to my face you bird!!!",12)
text2.moveTo(350,270)
paper.add(text2)
sleep(4)
paper.remove(text2)


#bird fear
text3 = Text("AHHHHHHH!!!!")
text3.moveTo(300,100)
bird.add(eyebrow)
paper.add(text3)
x=0
while x!=5:
    x =x +1
    pig.rotate(-10)
    pig.move(-10,0)
    sleep(delay)
    pig.rotate(10)
    pig.move(-10,0)
    wing.rotate(180)
    sleep(delay)
#bird flys away
bird.flip()
x=0
while x!=22:
    x =x +1
    pig.move(10,0)
    mud.move(10,0)
    tree.move(10,0)
    sleep(delay)
    pig.move(10,0)
    mud.move(10,0)
    tree.move(10,0)
    wing.rotate(180)
x=0

while x!=25:
    x=x+1
    tree2.move(10,0)
    sleep(.1)
    wing.rotate(180)
paper.remove(text3)
bird.remove(eyebrow)
bird.flip()
text4 = Text("Oh wait, why am I scared? He cant get me when I'm up here!!",12)
text4.moveTo(300,100)
paper.add(text4)
bird.remove(eye)
bird.add(eye2)
sleep(5)
paper.remove(text4)
bird.remove(eye2)
bird.add(eye)  

#bird goes to rest on the wire
text5 = Text("All that flying got me really tired, I'm going to rest for a bit.", 12)
text5.moveTo(300,100)
paper.add(text5)
sleep(5)
paper.remove(text5)
bird.flip()
x=0
while x!=45:
    x=x+1
    tree2.move(10,0)
    sleep(.1)
    wing.rotate(180)
x = 0
while x!=35:
    x=x+1
    post.move(10,0)
    sleep(.1)
    wing.rotate(180)
x= 0
while x!= 13:
    x=x+1
    bird.move(0,-10)
    sleep(.1)
    wing.rotate(180)
bird.flip()
bird.remove(eye)
bird.add(eye2)
sleep(4)

#PIG COMES BACKKKK
text6 = Text("COME HERE BIRD!!!",12)
text6.moveTo(400,200)
paper.add(text6)
sleep(2)
bird.remove(eye2)
bird.add(eye)
bird.add(eyebrow)
paper.add(text3)
pig.moveTo(550,420)
bird.flip()
x = 0
while x!=45:
    x =x +1
    pig.rotate(-10)
    pig.move(-10,0)
    sleep(delay)
    pig.rotate(10)
    pig.move(-10,0)
    wing.rotate(180)
    bird.move(-10,3)
    sleep(delay)
paper.remove(text3)
paper.remove(text6)

#The End
end =Text("THE END", 20)
end.moveTo(400,200)
paper.add(end)





