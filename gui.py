from Tkinter import*

main_window = Tk()

can = Canvas(main_window,width=700, height=500)
can.pack()

can.create_rectangle(100,10,600,350, fill="blue")

can.create_oval(200,150,150,200, fill="orange")
can.create_oval(400,100,350,50, fill="black")

button1 = Button( text = "Info", anchor = W)
button1.configure(width = 10,height=5, activebackground = "#33B5E5")
button1_window = can.create_window(10, 10, anchor=NW, window=button1)

button2 = Button( text = "Knowledge", anchor = W)
button2.configure(width = 10,height=10, activebackground = "#33B5E5")
button2_window = can.create_window(10, 110, anchor=NW, window=button2)

button3 = Button( text = "Equations", anchor = W)
button3.configure(width = 10,height =5, activebackground = "#33B5E5")
button3_window = can.create_window(690, 10, anchor=NE, window=button3)

button4 = Button( text = "Explore", anchor = W)
button4.configure(width = 10, height= 10, activebackground = "#33B5E5")
button4_window = can.create_window(690, 110, anchor=NE, window=button4)

button_play = Button( text = ">")
button_play.configure(width = 5, activebackground = "#33B5E5")
button_play_window = can.create_window(350, 390, window=button_play)

button_pause = Button( text = "||")
button_pause.configure(width = 5, activebackground = "#33B5E5")
button_pause_window = can.create_window(350, 430, window=button_pause)

slider1 = Scale(orient='horizontal',length= 200,from_=1, to=500)
slider1_window = can.create_window(200, 380, window=slider1)

slider2 = Scale(orient='horizontal',length=200, from_=1, to=500)
slider2_window = can.create_window(500, 380, window=slider2)

label1 =Label(text= "Ball 1 Mass (kg)")
label1_window = can.create_window(200, 410, window=label1)

label2 =Label(text= " Ball 1 Velocity (m/s)")
label2_window = can.create_window(500, 410, window=label2)

slider3 = Scale(orient='horizontal',length= 200,from_=1, to=500)
slider3_window = can.create_window(200, 440, window=slider3)

slider4 = Scale(orient='horizontal',length=200, from_=1, to=500)
slider4_window = can.create_window(500, 440, window=slider4)

label3 =Label(text= "Ball 2 Mass (kg)")
label3_window = can.create_window(200, 470, window=label3)

label4 =Label(text= " Ball 2 Velocity (m/s)")
label4_window = can.create_window(500, 470, window=label4)

main_window.mainloop()
