
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt( word=text,move=shift):
    cipher_text=""
    num=0
    for letter in word:
      num=alphabet.index(letter)+shift
      if num>(len(alphabet)-1):
          num= (num- len(alphabet)) 
      cipher_text+=alphabet[num]
    print(f"Your encoded message is {cipher_text}")

#TODO-2: Create a function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text,shift):
    text = input("Type your message:\n").lower()
    cipher_text=""
    num=0
    for letter in text:
      num=alphabet.index(letter) - shift
      if num<0:
          num= (num+ len(alphabet)) 
      cipher_text+=alphabet[num]
    print(f"Your decoded message is {cipher_text}")
   
def execution():
    if direction=="encode":
     encrypt()
 
    want_decode=input("if You want to decode the meassage enter Y or N: \n").lower()
    if want_decode=="y":
      decrypt(text,shift)
    else:
      print("good bye")

execution()
user=input("you want try again Y or N : \n").lower()   
while user=="y":
  direction = input("Type 'encode' to encrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  execution()