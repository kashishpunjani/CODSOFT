#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kashi
#
# Created:     29-09-2023
# Copyright:   (c) kashi 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#................................to-do-list................................

from tkinter import *
import tkinter.messagebox
from tkinter import simpledialog





#to-do list-functions


def entertask():
    input_text = ''
    def add():
        input_text = entery_task.get(1.0 ,'end-1c')
        if input_text == '':
            tkinter.messagebox.showwarning(title='warning' , message='please add some text')
        else:
            listbox_task.insert(END , input_text)
            root1.destroy()
    root1 = Tk()
    root1.title('add task')
    entery_task = Text(root1 , width= 50 , height= 4)
    entery_task.pack()
    button_temp = Button(root1 , text='add text' , command= add )
    button_temp.pack()

    root1.mainloop() #sb run karega jo function m hoga  using mainloop


#delete the one task which select using cursor
def deletetask():
    #selects the slected item and then deletes it
    selected=listbox_task.curselection()
    listbox_task.delete(selected[0])

#Executes this to mark completed
def markcompleted():
    marked=listbox_task.curselection()
    temp=marked[0]
    #store the text of selected item in a string
    temp_marked=listbox_task.get(marked)
    #update it
    temp_marked=temp_marked+" ✔"
    #delete it then insert it
    listbox_task.delete(temp)
    listbox_task.insert(temp,temp_marked)


# clear all the task
def clearbutton():
    listbox_task.delete(0,'end')

#close the app
def closeapp():
    window.destroy()

# insert the add task and it will update it..........
def update():
    selected_task = listbox_task.curselection()
    if selected_task:
        new_task = simpledialog.askstring('update ' ,'enter the updated task')
        if new_task:
            listbox_task.delete(selected_task)
            listbox_task.insert(selected_task, new_task)



#creating the initial window
# layout of application --------------------------------------------------------------->
tasks = []
window=Tk()  # use to create main application
window.title('To-Do-list')

#window.configure(background='black')
# it is optional to use this window.co....... because if open the window in full screen it will by default show the white screen but using this it will show black or any background so it's not mandatory to use this

#Frame predefine h ek contaniner which contain other widget in main window  and can have 3d border or y ek argument hota h jo main window m h
#Frame widget to hold the listbox and the scrollbar
frame_task = Frame(window)
frame_task.pack()


# listbox is predefine it store all the task that we given in the to-do-list
# agar hum height or weidth ni dege to default dega y window k size k according
listbox_task = Listbox(frame_task,bg = 'black' , fg = 'white' , height = 20 , width = 50 , font = 'Algerian')
listbox_task.pack(side = tkinter.LEFT)

scrol_bar_task = Scrollbar(frame_task)
scrol_bar_task.pack(side=tkinter.RIGHT , fill=tkinter.Y)

listbox_task.config(yscrollcommand= scrol_bar_task.set)
scrol_bar_task.config(command =listbox_task.yview)
# it configure it on the verticle axis given by command  listbox_task.yview



#button------->
entery_button = Button(window , text= 'add task' , width= 50 , bg= 'navyblue' , fg='white' , font = 'Algerian' , command= entertask)
entery_button.pack(pady=3)

delete_button = Button(window , text= 'delete task' , width= 50 ,bg= 'navyblue' , fg='white' ,font = 'Algerian',command = deletetask)
delete_button.pack(pady=3)

mark_button = Button(window , text= 'mark as completed' , width = 50 , bg= 'navyblue' ,fg='white' ,font = 'Algerian', command = markcompleted )
mark_button.pack(pady=3)

update_button = Button(text='update the list' , width=50 , background='navyblue' , fg= 'white', font = 'Algerian', command = update)
update_button.pack(pady=3)

clearall_button = Button(text= 'clear all list' , width= 50 , bg='navyblue' , fg='white' , font = 'Algerian', command = clearbutton )
clearall_button.pack(pady=3)

#bg = background color , fg = color of text , pady = button k uper or niche ke bich bich m difference just like padding
# we create a function entertask , delete task , mask as complete to call these function we use command

closeapp_button = Button(text='Exit' , width=50 , background='navyblue' , fg= 'white', font = 'Algerian', command = closeapp)
closeapp_button.pack(pady=3)
# font = ('Algerian',23)




window.mainloop()
# jo hum iske andar note krege vo sb run karega or display krega


