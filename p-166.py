from tkinter import *
from tkinter import ttk
root= Tk()
root.geometry("1000x600")
root.title("Working On Canvas Using Functions")

#create a canvas define width, height, bg color and border
canvas=Canvas(root, width = 500, height=400, bg = "darkblue", highlightbackground="red")
canvas.pack()

label=Label(root,text="   Choose Color : ")
label.place(relx=0.6,rely=0.9, anchor= CENTER)
 

#Add colors in the below list
fillcolour=["yellow", "brown", "red"]
colour_dropdown = ttk.Combobox(root,state="readonly" ,values = fillcolour, width = 10)
colour_dropdown.place(relx=0.8, rely=0.9, anchor= CENTER)

#add coordinates in the below list exaple: 10, 50, 100...
coordinates_values= [50,100,150,200,250,300,350,400,450,500]


startx=Label(root,text="startx")
startx.place(relx=0.1, rely=0.85, anchor= CENTER)
d1 = ttk.Combobox(root,state="readonly" ,values = coordinates_values, width = 10)
d1.place(relx=0.2, rely=0.85, anchor= CENTER)
    
#add code for starty label and dropdown for choosing coordinates
starty=Label(root,text="starty")
starty.place(relx=0.3, rely=0.85, anchor= CENTER)
d2 = ttk.Combobox(root,state="readonly" ,values = coordinates_values, width = 10)
d2.place(relx=0.4, rely=0.85, anchor= CENTER)





endx=Label(root,text="endx")
endx.place(relx=0.5, rely=0.85, anchor= CENTER)
d3 = ttk.Combobox(root,state="readonly" , values = coordinates_values, width = 10) 
d3.place(relx=0.6, rely=0.85, anchor= CENTER)

#add code for endy label and drop down for choosing coordinates
endy=Label(root,text="endy")
endy.place(relx=0.7, rely=0.85, anchor= CENTER)
d4 = ttk.Combobox(root,state="readonly" , values = coordinates_values, width = 10) 
d4.place(relx=0.8, rely=0.85, anchor= CENTER)


root.mainloop()