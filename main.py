from tkinter import *
root = Tk()
root.title('To Do List')
# hihiadsfkasdjfkdjsfkajkadsjfk
def createNewNote():
    newpage = Tk()
    newpage.title('new note')

    newnote = Entry(newpage)
    newnote.grid(row=0, column=1)
    newnote.pack()
    def insidecreateNewNote():
        toDoList = open('ToDoList.txt', 'a')
        toDoList.write(newnote.get() + '\n')
        toDoList.close()
        newpage.destroy()
        global todo
        todo.destroy()
        toDoList = open('ToDoList.txt', 'r')
        todo = Label(root, text=toDoList.read())
        todo.pack()
        toDoList.close()

    savebutton = Button(newpage, text='save', width=25, command=insidecreateNewNote)
    savebutton.pack()



button = Button(root, text='Create new note', width=25, command=createNewNote)
button.pack()

toDoList = open('ToDoList.txt', 'r')

todo = Label(root, text=toDoList.read())
todo.pack()
toDoList.close()

root.mainloop()
