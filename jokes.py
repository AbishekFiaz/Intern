import tkinter as tk
import pyjokes

root=tk.Tk()
root.title("JOKES GAME")
root.geometry("300x300")
root.configure(bg="black")

def joke():
    global joke
    joke=pyjokes.get_joke()
    T.insert(tk.END,joke)

def clear():
    T.delete("1.0","end")

T=tk.Text(root)
T.place(x=5,y=5,height=100,width=290)
b1=tk.Button(root,text="Jokes",bg="red",fg="white",command=joke)
b1.place(x=20,y=120,height=40,width=60)
b2=tk.Button(root,text="Clear",bg="red",fg="white",command=clear)
b2.place(x=100,y=120,height=40,width=60)

root.mainloop()