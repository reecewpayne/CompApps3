from Tkinter import*
import tkMessageBox
import physics

def Info():
    '''Information popup'''
    toplevel = Toplevel()
    toplevel.title("Info")
    photo = PhotoImage(file="Capture.gif")
    label1 = Label(toplevel, image = photo)
    label1.image = photo
    label1.pack()

def K():
    '''Knowledge popup'''
    toplevel1 = Toplevel()
    toplevel1.title("Knowledge")
    photo1 = PhotoImage(file="momentum.gif")
    label2 = Label(toplevel1, image = photo1,)
    label2.image = photo1
    label2.pack()

def Eq():
    '''Equations popup'''
    toplevel2 = Toplevel()
    toplevel2.title("Equations")
    photo2 = PhotoImage(file="elacol2.gif")
    label3 = Label(toplevel2, image = photo2,)
    label3.image = photo2
    label3.pack()


def start():
    flag = False
    data =[[40, Vel1.get(), Mass1.get(), 0.9],[440, Vel2.get(), Mass2.get(), 0.9]]
    sim = physics.space(data)
    if not flag:
        main_window.after(250, iterate, sim)

def iterate(sim):
    print('iterating')
    i = sim.next()
    print i
    can.move('ball_1', i[0], 0)
    can.move('ball_2', i[1], 0)


def stop():
    flag = True

flag = False
ball_1_x = 40
ball_2_x = 440

#Start TK
main_window = Tk()

#Create main canvas
can = Canvas(main_window,width=800, height=500)
can.pack()
    
#Draws box the size of the canvas as outline
can.create_rectangle(10,10,590,325, fill="#F5F5F5") #Animation box
can.create_rectangle(600,10,790,490, fill="#F5F5F5") #Information box

#Creates The balls on screen
ball_1 = can.create_oval(ball_1_x,100, ball_1_x+60, 160, fill="orange", tags='ball_1')
ball_2 = can.create_oval(ball_2_x,100, ball_2_x+60,160, fill="black", tags='ball_2')



# Button configurations settings
button1 = Button( text = "Info", anchor = W, command= Info)
button1.configure(relief= SOLID,width = 20,height=2, borderwidth=3, bg="#9AC7BF",activebackground = "#33B5E5") 
button1_window = can.create_window(770, 290, anchor=NE, window=button1)

button2 = Button( text = "Knowledge", anchor = W, command = K)
button2.configure(relief= SOLID,width = 20,height=2, borderwidth=3, bg="#9AC7BF", activebackground = "#33B5E5") 
button2_window = can.create_window(770, 340, anchor=NE, window=button2)

button3 = Button( text = "Equations", anchor = W, command= Eq)
button3.configure(relief= SOLID,width = 20,height =2, borderwidth=3, bg="#9AC7BF", activebackground = "#33B5E5") 
button3_window = can.create_window(770, 390, anchor=NE, window=button3)

#button4 = Button( text = "Explore", anchor = W)
#button4.configure(relief= SOLID,width = 20, height= 2, borderwidth=3, bg="#9AC7BF", activebackground = "#33B5E5") 
#button4_window = can.create_window(770, 440, anchor=NE, window=button4)

button_play = Button( text = ">")
button_play.configure(width = 5, bg="#9AC7BF", activebackground = "#33B5E5", command=start) 
button_play_window = can.create_window(560, 280, window=button_play)

button_pause = Button( text = "||")
button_pause.configure(width = 5, bg="#9AC7BF", activebackground = "#33B5E5", command=stop) 
button_pause_window = can.create_window(560, 310, window=button_pause)



# slider configurations settings
Mass1 = Scale(label= "Mass (Kg)", orient='horizontal',length= 130,from_=1, to=50)
Mass1_window = can.create_window(130, 380, window=Mass1)

Mass2 = Scale(orient='horizontal',length=130, from_=1, to=50)
Mass2_window = can.create_window(130, 440, window=Mass2)

Vel1 = Scale(label= "Velocity (m/s)",orient='horizontal',length= 130,from_=1, to=10)
Vel1_window = can.create_window(280, 380, window=Vel1)

Vel2 = Scale(orient='horizontal',length=130, from_=-1, to=-10)
Vel2_window = can.create_window(280, 440, window=Vel2)



# All Label configurations 
label1 = Label(text= "Ball 1")
label1_window = can.create_window(30, 395, window=label1)

label2 = Label(text= "Ball 2")
label2_window = can.create_window(30, 450, window=label2)

labelM1 = Label(text= "Momentum 1")
labelM1_window = can.create_window(450, 360, window=labelM1)

labelM2 = Label(text= "Momentum 2")
labelM2_window = can.create_window(450, 416, window=labelM2)

labelMT = Label(text= "Momentum Total")
labelMT_window = can.create_window(440, 472, window=labelMT)

Title = Label( bg="#F5F5F5", font=20, text= """The Law of Conservation
of Momentum""")
Title_window = can.create_window(695, 50, window=Title)

sub = Label( bg="#F5F5F5", font=10, text= """In a collision
between two objects,
the total momentum
is unchanged. Meaning
the velocities of both
objects change but does
not alter the total
momentum.""")
sub_window = can.create_window(695, 180, window=sub)



# boxes to display momentum readouts 
momentum1 = Text(height=2, width=10,relief= SOLID)
momentum_window= can.create_window(550,360, window=momentum1)

momentum2 = Text(height=2, width=10,relief= SOLID)
momentum_window= can.create_window(550,416, window=momentum2)

momentumT = Text(height=2, width=10,relief= SOLID)
momentum_window= can.create_window(550,472, window=momentumT)


main_window.mainloop()
