from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root=Tk()
root.title("Error Handling")
root.geometry("400x400")
root.configure(background="yellow")

img=ImageTk.PhotoImage(Image.open("images.jpg"),master=root)

entry_type=Entry(root)
entry_type.place(relx=0.5,rely=0.2,anchor=CENTER)

label_image=Label(root,image=img)
label_image.place(relx=0.5,rely=0.6,anchor=CENTER)

def Check():
    try:
        get_value=int(entry_type.get())
        messagebox.showinfo("MESSAGE","Credit Card Accepted")
    except:
        messagebox.showinfo("ALERT","Credit Card Not Accepted, Please Enter A Valid Pincode")
        
    
    
        
    

btn=Button(root,bg="orange",fg="white",text="Check Credit Card",command=Check)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)
root.mainloop()

