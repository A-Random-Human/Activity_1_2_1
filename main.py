# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
font_setup = ("Arial", 20, "bold")
spotColor = "LightCoral"
spotShape = "circle"
spotSize = 15
score = 0

#-----initialize turtle-----
spot = trtl.Turtle(spotShape)
spot.shape(spotShape)
spot.turtlesize(spotSize)
spot.fillcolor(spotColor)
spot.pencolor("pink")
spot.penup()

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(60,120)

timer = 10
counter_interval = 500   
timer_up = False
counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-200,120)

wn = trtl.Screen()
trtl.screensize(400, 300, "YellowGreen")
#-----game functions--------
def change_position():
  new_xpos = rand.randint(-200,200)
  new_ypos = rand.randint(-150,135)
  spot.goto(new_xpos, new_ypos)

def spot_clicked(x,y):
  global timer_up
  if timer_up == False:
    global timer
    timer +=1
    update_score()
    change_size()
    change_position()
  else:
    spot.shape("turtle")
    spot.fillcolor("FireBrick")
    trtl.bgcolor ("Yellow")
    
def change_size():
  global spotSize
  spotSize -=1
  spot.turtlesize(spotSize)

def update_score():
  global score
  score += 1
  score_writer.clear()
  score_writer.write("Score: " + str(score), font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

spot.onclick(spot_clicked)

#-----events----------------
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
