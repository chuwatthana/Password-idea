import random, string
character=string.ascii_uppercase
numbers=string.digits
symbols=string.punctuation

print("welcome to password generator !")
user_preference=input("กรุณาป้อนระดับของ password (easy)(medium)(hard)(impossible):")
user_length=int(input("ความยาวของ passwords ?"))

if user_preference=="easy":
    password=""
    for char in range(1,user_length+1):
        password+=random.choice(numbers)
    print("พาสเวิร์ดของคุณคือ"+password) 
    
       
elif user_preference=="medium":
    user_character=int(input("คุณต้องการตัวอักษรกี่ตัว"))
    if user_character<user_length:
     password=""
     for char in range(1,user_length-user_character+1):
        password+=random.choice(numbers)

     for char in range(1,user_character+1):
        password+=random.choice(character)   
     print("พาสเวิร์ดของคุณคือ"+password)
    else:
       print("Error !")

elif user_preference=="hard":
    user_character=int(input("คุณต้องการตัวอักษรกี่ตัว"))
    user_symbols=int(input("คุณต้องการตัวอักษรพิเศษกี่ตัว"))
    if user_character+user_symbols<user_length:
     password=""
     for char in range(1,user_length-user_character-user_symbols+1):
        password+=random.choice(numbers)

     for char in range(1,user_character+1):
        password+=random.choice(character)  
     for char in range(1,user_symbols+1):
        password+=random.choice(symbols)
     print("พาสเวิร์ดของคุณคือ"+password)
    
    else:
       print("Error")
    

elif user_preference=="impossible":
      user_character=int(input("คุณต้องการตัวอักษรกี่ตัว"))
      user_symbols=int(input("คุณต้องการตัวอักษรพิเศษกี่ตัว"))
      if user_character+user_symbols<user_length:
       password=[]
       for char in range(1,user_length-user_character-user_symbols+1):
        password+=random.choice(numbers)

       for char in range(1,user_character+1):
        password+=random.choice(character)  
    
       for char in range(1,user_symbols+1):
        password+=random.choice(symbols)
    
       random.shuffle(password)
       final_password=""
       for char in password :
          final_password+=char   
       print(f"พาสเวิร์ดของคุณคือ",final_password)
      else:
         print("Error")
if user_length<=0:
       print("สมองมีแค่นี่หรอ!")


print("จบโปรแกรม")

   
