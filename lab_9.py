import turtle
import random 

size_x=800
size_y=500
turtle.setup(size_x,size_y)

turtle.penup()
START_LENGTH = 1
square_size=20
TIME_STEP = 100


countdown_list=[]
n=60
def countdown():
    global n
    if n == 0:
        print("blast off")
        return
    print(n)
    n=n-1
    countdown_list.append(n)
    turtle.ontimer(countdown,1000)
    



pos_list = []
stamp_list = []
trash_pos=[]
trash_stamps=[]

robot = turtle.clone()
screen = turtle.Screen()
image = "robot.gif"
screen.addshape(image)
robot.shape(image)



turtle.listen()
screen = turtle.Screen()
screen.setup(size_x,size_y)
screen.bgpic('ocen.gif')

turtle.hideturtle()


robot.direction = "Up"
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    robot.direction="Up"
    print("You pressed the up key!")
    
turtle.onkeypress(up, "Up")



def Down():
    robot.direction="Down"
    print("You pressed the Down key!")
    
turtle.onkeypress(Down, "Down")


def Right():
    robot.direction="Right" 
    print("You pressed the Right key!")
    
turtle.onkeypress(Right, "Right")


def Left():
    robot.direction="Left" 
    print("You pressed the Left key!")
    
turtle.onkeypress(Left, "Left")

turtle.listen()
turtle.register_shape("plasticbag1.gif")
trash = turtle.clone()
trash.shape("plasticbag1.gif")
trash_pos = []
trash_stamps = []



for this_trash_pos in trash_pos :
    trash.goto(this_trash_pos)
    f = trash.stamp()
    trash_stamps.append(f)

trash.hideturtle()

def make_trash():
    min_x=-int(size_x/2/square_size)+1
    max_x=int(size_x/2/square_size)-1
    min_y=-int(size_y/2/square_size)+1
    max_y=int(size_y/2/square_size)-1
    trash_x = random.randint(min_x,max_x)*square_size
    trash_y = random.randint(min_y,max_y)*square_size
    trash.goto(trash_x,trash_y)
    trash_pos.append((trash_x,trash_y))
    trash1 = trash.stamp()
    trash_stamps.append(trash1)


turtle.listen()
turtle.register_shape("plcup.gif")
trash2 = turtle.clone()
trash2.shape("plcup.gif")
trash2_pos = []
trash2_stamps = []




for this_trash2_pos in trash2_pos :
    trash2.goto(this_trash2_pos)
    f1 = trash2.stamp()
    trash2_stamps.append(f1)
    
trash2.hideturtle()

def make_trash2():
    min_x=-int(size_x/2/square_size)+1
    max_x=int(size_x/2/square_size)-1
    min_y=-int(size_y/2/square_size)+1
    max_y=int(size_y/2/square_size)-1
    trash2_x = random.randint(min_x,max_x)*square_size
    trash2_y = random.randint(min_y,max_y)*square_size
    trash2.goto(trash2_x,trash2_y)
    trash2_pos.append((trash2_x,trash2_y))
    trash3 = trash2.stamp()
    trash2_stamps.append(trash3)

turtle.listen()
turtle.register_shape("pl.gif")
trash4 = turtle.clone()
trash4.shape("pl.gif")
trash4_pos = [ ]
trash4_stamps = []



for this_trash4_pos in trash4_pos :
    trash4.goto(this_trash4_pos)
    f2 = trash4.stamp()
    trash4_stamps.append(f2)

trash4.hideturtle()

def make_trash4():
    min_x=-int(size_x/2/square_size)+1
    max_x=int(size_x/2/square_size)-1
    min_y=-int(size_y/2/square_size)+1
    max_y=int(size_y/2/square_size)-1
    trash4_x = random.randint(min_x,max_x)*square_size
    trash4_y = random.randint(min_y,max_y)*square_size
    trash4.goto(trash4_x,trash4_y)
    trash4_pos.append((trash4_x,trash4_y))
    trash5 = trash4.stamp()
    trash4_stamps.append(trash5)


for i in range(8):
    make_trash2()

for b in range(8):
    make_trash()

for l in range(8):
    make_trash4()


countdown()

def move_robot():
    my_pos = robot.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if robot.direction == "Up":
        robot.goto(x_pos, y_pos + square_size)
        print("You moved up!")
    elif robot.direction=="Down":
        robot.goto(x_pos, y_pos - square_size)
    
    if robot.direction == "Right":
        robot.goto(x_pos + square_size,y_pos)
        print("You moved up!")
    elif robot.direction=="Left":
        robot.goto(x_pos - square_size,y_pos)
  
    new_pos = robot.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
    if new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    if new_y_pos >= UP_EDGE:
        print("You hit the up edge! Game over!")
        quit()
    if new_y_pos <= DOWN_EDGE:
        print("You hit the down edge! Game over!")
        quit()
        
    if robot.pos() in trash_pos:
        trash_index=trash_pos.index(robot.pos()) 
        trash.clearstamp(trash_stamps[trash_index]) 
        trash_pos.pop(trash_index) 
        trash_stamps.pop(trash_index) 
        print("You catch trash !")
    #if len(trash_stamps) <= 6 :
     #   make_trash()
        
    if robot.pos() in trash2_pos:
        trash2_index=trash2_pos.index(robot.pos()) 
        trash2.clearstamp(trash2_stamps[trash2_index]) 
        trash2_pos.pop(trash2_index) 
        trash2_stamps.pop(trash2_index) 
        print("You catch trash !")
##    if len(trash2_stamps) <= 6 :
##        make_trash2()

        
    if robot.pos() in trash4_pos:
        trash4_index=trash4_pos.index(robot.pos()) 
        trash4.clearstamp(trash4_stamps[trash4_index]) 
        trash4_pos.pop(trash4_index) 
        trash4_stamps.pop(trash4_index) 
        print("You catch trash !")
##    if len(trash4_stamps) <= 6 :
##        make_trash4()

    if trash_pos == [] and trash2_pos == [] and trash4_pos == []:
        print("YOU WON!!!!!!!")
        quit()
    turtle.ontimer(move_robot,TIME_STEP)
    
#----------------------------------------------------------------------------------------------------------------
fish1 = turtle.clone()
screen = turtle.Screen()
image = "fish.gif"
screen.addshape(image)
fish1.shape(image)

fish2=turtle.clone()
screen = turtle.Screen()
image = "fish.gif"
screen.addshape(image)
fish2.shape(image)
fish2.penup()
turtle.penup()

pos_list1 = []
pos_list2 = []
stamp_list1 = []
stamp_list2 = []


turtle.hideturtle()
turtle.penup()
fish1.penup()
fish1.goto(-200,0)
fish2.goto(0,-200)

def new_stamp1():
    
    fish1_pos = fish1.pos()
   
    pos_list1.append(fish1_pos) 
        
    r=fish1.stamp()
         
    stamp_list1.append(r)
def new_stamp_f():
  
    fish2_pos = fish2.pos()

    pos_list2.append(fish2_pos) 
          
    r=fish2.stamp()
         
    stamp_list2.append(r)
    
    

for b in range(START_LENGTH) :
    x_pos1=fish1.pos()[0]
    y_pos1=fish1.pos()[1] 
    
    x_pos1+=square_size

    fish1.goto(x_pos1,y_pos1)
    
   
    
    new_stamp1()
    

for b in range(START_LENGTH) :
    x_pos2=fish2.pos()[0]
    y_pos2=fish2.pos()[1] 
    
    x_pos2+=square_size

    fish2.goto(x_pos2,y_pos2)

    
    new_stamp_f()
    
def remove_last_stamp1(): 

    old_stamp1 = stamp_list1.pop(0) 
    fish1.clearstamp(old_stamp1)
    pos_list1.pop(0) 



fish1.direction='Up'


def remove_last_stamp_f(): 

    old_stamp2 = stamp_list2.pop(0) 
    fish2.clearstamp(old_stamp2) 
    pos_list2.pop(0)



fish2.direction='Left'





def up1():
    fish1.direction="Up"

def down1():
    fish1.direction="Down"


def left1():
    fish1.direction="Left"


def right1():
    fish1.direction="Right"


def up_f():
    fish2.direction="Up"

def down_f():
    fish2.direction="Down"


def left_f():
    fish2.direction="Left"


def right_f():
    fish2.direction="Right"





def move1():
   
    my_pos1 = fish1.pos()
    x_pos1 = my_pos1[0]
    y_pos1 = my_pos1[1]
    
  
    if fish1.direction == "Up":
        fish1.goto(x_pos1, y_pos1 + square_size)
   
    elif fish1.direction=="Down":
        fish1.goto(x_pos1, y_pos1 - square_size)

    elif fish1.direction=="Left":
        fish1.goto(x_pos1-square_size, y_pos1)

    elif fish1.direction=="Right":
        fish1.goto(x_pos1+square_size, y_pos1)
   
    remove_last_stamp1()
    new_stamp1()

 
    new_pos1 = fish1.pos()
    new_x_pos1 = new_pos1[0]
    new_y_pos1 = new_pos1[1]

    

    if new_x_pos1 >= RIGHT_EDGE:
         fish1.direction="Left"

    if new_y_pos1<=DOWN_EDGE:
        fish1.direction="Up"

    if new_x_pos1<=LEFT_EDGE:
        fish1.direction="Right"

    if new_y_pos1>=UP_EDGE:
        fish1.direction="Down"

    if new_pos1 == robot.pos():
        quit()

    turtle.ontimer(move1,TIME_STEP)
"""
    if len(trash_stamps)<=6:
        make_trash()
"""


move1()




def move_f():
   
    my_pos2 = fish2.pos()
    x_pos2 = my_pos2[0]
    y_pos2= my_pos2[1]

    if fish2.direction == "Up":
        fish2.goto(x_pos2, y_pos2 + square_size)
   
    elif fish2.direction=="Down":
        fish2.goto(x_pos2, y_pos2 - square_size)

    elif fish2.direction=="Left":
        fish2.goto(x_pos2-square_size, y_pos2)

    elif fish2.direction=="Right":
        fish2.goto(x_pos2+square_size, y_pos2)
    

    
    remove_last_stamp_f()
   
    new_stamp_f()

   
    new_pos2 = fish2.pos()
    new_x_pos2 = new_pos2[0]
    new_y_pos2 = new_pos2[1]
 

   
    if new_x_pos2 >= RIGHT_EDGE:
         fish2.direction="Left"

    if new_y_pos2<=DOWN_EDGE:
        fish2.direction="Up"

    if new_x_pos2<=LEFT_EDGE:
        fish2.direction="Right"

    if new_y_pos2>=UP_EDGE:
        fish2.direction="Down"

    if new_pos2 == robot.pos():
        quit()

    turtle.ontimer(move_f,TIME_STEP)
"""
    if len(trash_stamps)<=6:
        make_trash()
"""


move_f()

#--------------------------------------------------------------------------------
fish3 = turtle.clone()
screen = turtle.Screen()
image = "fish.gif"
screen.addshape(image)
fish3.shape(image)


pos_list3 = []
stamp_list3 = []

turtle.hideturtle()
turtle.penup()
fish3.penup()
fish3.goto(200,0)

def new_stamp3():
   
    fish3_pos = fish3.pos()
   
    pos_list3.append(fish3_pos) 
        
    r=fish3.stamp()
         
    stamp_list3.append(r)


    
    """x_pos3=fish3.pos()[0]
    y_pos3=fish3.pos()[1] 
    
    x_pos3+=square_size

    fish3.goto(x_pos3,y_pos3)
    
"""   

new_stamp3()


def remove_last_stamp3(): #BTW i know its a long name, i couldn't find any better

    old_stamp3 = stamp_list3.pop(0) # get the ID of the last piece of body
    fish3.clearstamp(old_stamp3) # erase this last piece of body from the screen
    pos_list3.pop(0) # remove last piece of the body position from the pos list


#make the turtle direction to be up
fish3.direction='Up'



#define the keys
def up3():
    fish3.direction="Up"

def down3():
    fish3.direction="Down"


def left3():
    fish3.direction="Left"
    print("test")


def right3():
    fish3.direction="Right"





#and finally, the move function
def move3():
    #get the pos and save it so that i will be able to change it
    my_pos3 = fish3.pos()
    x_pos3 = my_pos3[0]
    y_pos3 = my_pos3[1]
    
    #if pos is up/down/left/right i want to change the y pos by using
    #square size (20)
    if fish3.direction == "Up":
        fish3.goto(x_pos3, y_pos3 + square_size)
  
   
    elif fish3.direction=="Down":
        fish3.goto(x_pos3, y_pos3 - square_size)
       

    elif fish3.direction=="Left":
        fish3.goto(x_pos3-square_size, y_pos3)
      
    elif fish3.direction=="Right":
        fish3.goto(x_pos3+square_size, y_pos3)
        


    #makes the fish3 move automatically
    

    #remove the last stamp of the fish3 to make it "move"
    #TBH functions are not too bad
    remove_last_stamp3()
    #after i remove the last stamp i make the next stamp. thanks functions :P
    new_stamp3()



   
    new_pos3 = fish3.pos()
    new_x_pos3 = new_pos3[0]
    new_y_pos3 = new_pos3[1]
  

    
   
    if new_x_pos3 >= RIGHT_EDGE:
         fish3.direction="Left"

    if new_y_pos3<=DOWN_EDGE:
        fish3.direction="Up"

    if new_x_pos3<=LEFT_EDGE:
        fish3.direction="Right"

    if new_y_pos3>=UP_EDGE:
        fish3.direction="Down"

    if new_pos3 == robot.pos():
        quit()


    turtle.ontimer(move3,TIME_STEP)

move3()

 #--------------------------------------------------------------------
fish4 = turtle.clone()
fish4.shape(image)

#lists for use in move function
pos_list4 = []
stamp_list4 = []
#i want to see the fish4 stamps, not the turtle itself
turtle.hideturtle()
turtle.penup()
fish4.penup()
fish4.goto(0,100)
#function that makes new stamp for the fish4
def new_stamp4():
    #i wanna get the current pos of the fish4
    fish4_pos = fish4.pos()
    #and then make it appear in the pos list
    pos_list4.append(fish4_pos) 
    #find and save the stamp ID so i can remove it
    #later on when the fish4 moves        
    r=fish4.stamp()
         
    stamp_list4.append(r)


    
#a for loop that draws the fish4 at the beginning of the game
#it counts the number of pieces of the fish4 which is 1
for b in range(START_LENGTH) :
    x_pos4=fish4.pos()[0]
    y_pos4=fish4.pos()[1] 
    #add the size of the square (20) to x pos
    x_pos4+=square_size

    fish4.goto(x_pos4,y_pos4)
    #Move snake to new (x,y)
   
    #draw the next place of the fish4
    new_stamp4()


def remove_last_stamp4(): #BTW i know its a long name, i couldn't find any better

    old_stamp4 = stamp_list4.pop(0) # get the ID of the last piece of body
    fish4.clearstamp(old_stamp4) # erase this last piece of body from the screen
    pos_list4.pop(0) # remove last piece of the body position from the pos list


#make the turtle direction to be up
fish4.direction='Right'



#define the keys
def up4():
    fish4.direction="Up"

def down4():
    fish4.direction="Down"


def left4():
    fish4.direction="Left"


def right4():
    fish4.direction="Right"




#and finally, the move function
def move4():
    #get the pos and save it so that i will be able to change it
    my_pos4 = fish4.pos()
    x_pos4 = my_pos4[0]
    y_pos4 = my_pos4[1]
    
    #if pos is up/down/left/right i want to change the y pos by using
    #square size (20)
    if fish4.direction == "Up":
        fish4.goto(x_pos4, y_pos4 + square_size)
   
    elif fish4.direction=="Down":
        fish4.goto(x_pos4, y_pos4 - square_size)

    elif fish4.direction=="Left":
        fish4.goto(x_pos4-square_size, y_pos4)

    elif fish4.direction=="Right":
        fish4.goto(x_pos4+square_size, y_pos4)

    #makes the fish4 move automatically


    #remove the last stamp of the fish4 to make it "move"
    #TBH functions are not too bad
    remove_last_stamp4()
    #after i remove the last stamp i make the next stamp. thanks functions :P
    new_stamp4()

   #where is my fish4's new position???
    new_pos4 = fish4.pos()
    new_x_pos4 = new_pos4[0]
    new_y_pos4 = new_pos4[1]
    #ok now i know where it is

    
    #like in the snake, i want the game to stop once the fish4 hits the
    #edges of the screen
    if new_x_pos4 >= RIGHT_EDGE:
         fish4.direction="Left"

    if new_y_pos4<=DOWN_EDGE:
        fish4.direction="Up"

    if new_x_pos4<=LEFT_EDGE:
        fish4.direction="Right"

    if new_y_pos4>=UP_EDGE:
        fish4.direction="Down"

    if new_pos4 == robot.pos():
        print('O no! You kill fish! Game over!')
        quit()

    elif countdown_list[-1]==0:
        print("time out,you lost!")
        quit()

    turtle.ontimer(move4,TIME_STEP)


#now use the move!
move4()



move_robot()



turtle.mainloop() 
