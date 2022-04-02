import tkinter as tk 
# from tkinter import *
from tkinter import filedialog


window = tk.Tk()
window.title("Text Encryption")
window.geometry('500x700')

def browseFiles():
    new = ""
    filename = None
    # try:
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    
    # except:
    if (filename == None):
        return

    else:
        file = open(filename, "r")
        for x in file:
            new =new +  x
            print(new)


    # file.close()

    print(new)
    text.insert("1.0", new)
    # out_txt.insert("1.0", chars = gen)
    # return new
                																				
	
file_opn_btn = tk.Button(window,text = "Browse Files", command = browseFiles)
file_opn_btn.pack()


text = tk.Text()
text.pack()
window.mainloop()


