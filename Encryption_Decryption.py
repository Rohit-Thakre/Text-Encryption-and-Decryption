import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import datetime
# Global variables 
dic_dcrpt = {'A12+0': 'A', '1*3a0': 'B', '#140': 'C', '1%5$0': 'D', 'A160': 'E', 'B&1(70': 'F', '+1/8%0': 'G', 
'1@9!0': 'H', '2f1%0': 'I', '23540': 'J', '2~!4*0': 'K', ')2=50': 'L', '#2@6!0': 'M', '$(2)7$0': 'N', '2&8@g0': 'O', 
'2&9ad0': 'P', '3r$1&0': 'Q', 'r3f2r0': 'R', '3(4+s0': 'S', 't3s5j80': 'T', '%*3d60': 'U', '3$7dfed0': 'V', 
'3K8O0': 'W', '3*V9d0': 'X', '9(+)3-0': 'Y', '@4#10': 'Z', '4rt20': 'a', '430': 'b', '450': 'c', '460': 'd', 
'470': 'e', '480': 'f', '490': 'g', '510': 'h', '520': 'i', '5j3s&0': 'j', '#515de4&0': 'k', '5&de=60': 'l', 
'&5d7g0': 'm', '5^8dk0': 'n', '5*a9%0': 'o', '6vs1code0': 'p', 'r-oh6i2T0': 'q', '6%3=gf0': 'r', '6$4ge0': 's', 
'6*gr5T0': 't', '6U$<70': 'u', '64$8@%0': 'v', '-l6r9T0': 'w', '&aH7d10': 'x', '1Y7z90': 'y', '7rthei-(2(0': 'z',
 ')7)3+0': '+', '740': '-', '750': '/', '760': '*', '780': '=', '790': '%', '810': '&', '870': '@', 'bc0': '0', 
 'ab0': '1', 'c5d0': '2', 'e3f0': '3', 'gdegh0': '4', 'qigelo0': '5', 'st&dkl0': '6', 'm%ndn0': '7', 'ehop0': '8', 
 'qltr0': '9',  "ti8d0":'"', "the$0": "'" , "(0" : ")", ")0": "(", "dfrt870": "}", "577rt0" : "{", "713eo_t0": "_","45ri_5t0": '/', "rohit0": "\\",
 "dspd_ex0" : "$", "pravin0": "^"}

 
dic_encrypt = {'A': 'A12+0', 'B': '1*3a0', 'C': '#140', 'D': '1%5$0', 'E': 'A160', 'F': 'B&1(70', 'G':'+1/8%0', 'H': '1@9!0',
 'I': '2f1%0', 'J': '23540', 'K': '2~!4*0', 'L': ')2=50', 'M': '#2@6!0', 'N': '$(2)7$0',  'O' : '2&8@g0',  'P':'2&9ad0',  'Q':'3r$1&0',
  'R': 'r3f2r0', 'S': '3(4+s0', 'T': 't3s5j80', 'U': '%*3d60', 'V': '3$7dfed0',  'W':'3K8O0',  'X':'3*V9d0',  'Y':'9(+)3-0', 'Z': '@4#10', 
  'a': '4rt20', 'b': '430', 'c': '450', 'd': '460', 'e': '470', 'f': '480', 'g': '490', 'h':'510',  'i':'520', 
  'j': '5j3s&0', 'k': '#515de4&0', 'l': '5&de=60', 'm': '&5d7g0',  'n':'5^8dk0', 'o': '5*a9%0', 'p': '6vs1code0', 'q': 'r-oh6i2T0', 'r': '6%3=gf0', 
  's': '6$4ge0',  't':'6*gr5T0', 'u': '6U$<70',  'v':'64$8@%0', 'w': '-l6r9T0', 'x': '&aH7d10', 'y': '1Y7z90',  'z':'7rthei-(2(0',  '+':')7)3+0', 
  '-': '740',  '/':'750', '*': '760', '=': '780',  '%':'790', '&': '810',  '@':'870',  '0':'bc0', '1': 'ab0', 
  '2': 'c5d0',  '3':'e3f0', '4': 'gdegh0',  '5':'qigelo0', '6': 'st&dkl0', '7': 'm%ndn0',  '8':'ehop0', '9': 'qltr0', '"': "ti8d0",
  "'":"the$0", ")": "(0", "(":")0",  "}":"dfrt870", "{" : "577rt0","_":"713eo_t0", '/': "45ri_5t0", "\\": "rohit0" , "$": "dspd_ex0", "^" : "pravin0" }



frame = tk.Tk()
frame.title("Text Encryption")
frame.geometry('500x730')
bg = "#202020"
frame.config(bg=bg)



def Input_Nor():

    Normal_txt = inputtxt.get(1.0, "end-1c")
    gen =""

    current_time = datetime.datetime.now()
    file = open( "histry.txt",  "a")
    file.writelines("\n" + Normal_txt + "\t \t " + str(current_time))
    
   # func of text encryption
    for x in Normal_txt: 
      # print(x)
        if (x == ' '): 
            gen = gen + ' '

        for y in dic_encrypt:
            if(x == y): 
                gen = gen + dic_encrypt[y]

    out_txt.delete("1.0", "end")
    out_txt.insert("1.0", chars = gen)



def Input_Dec():
    Encrypted_txt = inputtxt.get(1.0, "end-1c")

   # func of text decryption
    gen=""
    text = ""
    for x in Encrypted_txt:
        if(x == "0"): 
            text = text + x
            for y in dic_dcrpt: 
                if(y == text ): 
                    gen = gen + dic_dcrpt[y]
                    text = ""

        elif (x == ' '): 
            gen = gen + ' '

        else: 
         text = text + x 

    out_txt.delete("1.0", "end")
    out_txt.insert("1.0", chars = gen)


def Reset(): 
    inputtxt.delete("1.0", "end")
    out_txt.delete("1.0", "end")

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
            # print(new)
    
    inputtxt.delete("1.0", "end")
    inputtxt.insert("1.0", chars = new)



def savefile(): 
    Files = (('All Files', '*.*'),('Python Files', '*.py'),('Text Document', '*.txt'))

    path = asksaveasfile(filetypes = Files).name
        
    with open(path, 'w') as f:
        content = out_txt.get('1.0', tk.END)
        f.write(content)
        f.close()
      
btn_font = ('Helvetica 10 bold italic')
Font_tuple = ("Comic Sans MS", 15, "bold")
bt_color="white"
bt_bg="#003322"

# TextBox Creation
inputtxt = tk.Text(frame,height = 8, width=38, bg="#262626", fg = "white",insertbackground="white")
out_txt = tk.Text(frame,height = 8, width=38,bg= "#262626", fg = "white",insertbackground="white")
# pack  
inputtxt.place(x = 18, y = 50)
inputtxt.config(font = Font_tuple)
out_txt.place(x = 18, y = 410)
out_txt.config(font = Font_tuple)

# Button 
EncyptButton = tk.Button(frame,text = "Encrypt",command = Input_Nor, height= 2, width= 15,fg=bt_color,bg="#1aff1a", font= btn_font)
EncyptButton.place(x=25, y=325)

DecryptButton = tk.Button(frame,text = "Decrypt",command = Input_Dec,height= 2, width= 15,fg=bt_color,bg="#3399ff", font=btn_font)
DecryptButton.place(x=193, y=325)

ResetButton = tk.Button(frame,text = "Reset",command = Reset,height= 2, width= 15,fg=bt_color,bg="red", font=btn_font)
ResetButton.place(x=350, y=325)

browse = tk.Button(frame,text = "Open",command = browseFiles,height= 2, width= 15,fg=bt_color,bg="#ff4000", font=btn_font)
browse.place(x=190, y=675)

save = tk.Button(frame,text = "Save",command = savefile,height= 2, width= 15,fg=bt_color,bg="#004d99", font=btn_font)
save.place(x=350, y=675)

  

# Label Creation
lbl = tk.Label(frame, text = "Text Encryption and Decryption",font=Font_tuple, bg= bg,fg = "#1aff1a")
lbl.pack()



# os.system("cls")
frame.mainloop()