import tkinter as tk 
from tkinter.filedialog import asksaveasfile

window = tk.Tk()
window.geometry('200x200')
window.title("Python Guides")

inputtxt = tk.Text(window,height = 8, width=38, bg="#051405", fg = "white",insertbackground="white")
inputtxt.pack()
   
def savefile(): 
    Files = (('All Files', '*.*'),('Python Files', '*.py'),('Text Document', '*.txt'))

    path = asksaveasfile(filetypes = Files).name
        
    with open(path, 'w') as f:
        content = inputtxt.get('1.0', tk.END)
        f.write(content)
        f.close()
      
 


        

button = tk.Button(window, text = 'Save', command = savefile)
button.pack( pady = 20)

window.mainloop()