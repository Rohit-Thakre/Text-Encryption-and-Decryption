# Global variables 
dic_dcrpt = {'120': 'A', '130': 'B', '140': 'C', '150': 'D', '160': 'E', '170': 'y', '180': 'G', '190': 'H',
 '210': 'I', '230': 'J', '240': 'K', '250': 'L', '260': 'M', '270': 'N', '280': 'O', '290': 'P', '310': 'Q',
  '320': 'R', '340': 'S', '350': 'T', '360': 'U', '370': 'V', '380': 'W', '390': 'X', '930': 'Y', '410': 'Z',
   '420': 'a', '430': 'b', '450': 'c', '460': 'd', '470': 'e', '480': 'f', '490': 'g', '510': 'h', '520': 'i',
    '530': 'j', '540': 'k', '560': 'l', '570': 'm', '580': 'n', '590': 'o', '610': 'p', '620': 'q', '630': 'r', 
    '640': 's', '650': 't', '670': 'u', '680': 'v', '690': 'w', '710': 'x', '720': 'z', '730': '+', '740': '-', 
    '750': '/', '760': '*', '780': '=', '790': '%', '810': '&', '870': '@', 'bc0': '0', 'ab0': '1', 'cd0': '2', 
    'ef0': '3', 'gh0': '4', 'ig0': '5', 'kl0': '6', 'mn0': '7', 'op0': '8', 'qr0': '9'}

dic_encrypt = {'A': '120', 'B': '130', 'C': '140', 'D': '150', 'E': '160', 'F': '170', 'G':'180', 'H': '190',
 'I': '210', 'J': '230', 'K': '240', 'L': '250', 'M': '260', 'N': '270',  'O' : '280',  'P':'290',  'Q':'310',
  'R': '320', 'S': '340', 'T': '350', 'U': '360', 'V': '370',  'W':'380',  'X':'390',  'Y':'930', 'Z': '410', 
  'a': '420', 'b': '430', 'c': '450', 'd': '460', 'e': '470', 'f': '480', 'g': '490', 'h':'510',  'i':'520', 
  'j': '530', 'k': '540', 'l': '560', 'm': '570',  'n':'580', 'o': '590', 'p': '610', 'q': '620', 'r': '630', 
  's': '640',  't':'650', 'u': '670',  'v':'680', 'w': '690', 'x': '710', 'y': '170',  'z':'720',  '+':'730', 
  '-': '740',  '/':'750', '*': '760', '=': '780',  '%':'790', '&': '810',  '@':'870',  '0':'bc0', '1': 'ab0', 
  '2': 'cd0',  '3':'ef0', '4': 'gh0',  '5':'ig0', '6': 'kl0', '7': 'mn0',  '8':'op0', '9': 'qr0'}


def Input_Nor():
   Normal_txt = str(input("Enter Your Nomal text here: "))
   gen =""

   # func of text encryption
   for x in Normal_txt: 
      # print(x)
      if (x == ' '): 
         gen = gen + ' '

      for y in dic_encrypt:
         if(x == y): 
            gen = gen + dic_encrypt[y]

   # return gen
   print(gen)




def Input_Dec(): 
   Encrypted_txt = input("Enter Your Encrypted text here: ")

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
         # print(text)

   # return gen
   print(gen)

def main():
   import os
   os.system("cls")
   os.system("color a")

   print("1.Encypet text")
   print("2.Decrypt text")
   print("3.Exit")
   print("Please select one of your operation:\n ")

   while(True):
      option = int(input("please enter your option here : "))

      if(option == 1): 
         Input_Nor()

      elif(option == 2): 
         Input_Dec()
      elif (option == 3): 
         exit(1)
      else: 
         print("Invalid option !")




main()