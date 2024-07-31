#print (7)
#print (7 + 3)
#print ("7+3")
#number = 7
#word = "7"
#print (type (number))
#print (type (word))
#clear
#float
#number_2 = 7.1
#print (type(number_2))
#print (number_2)
#print (type (number + number_2))
#print (number+number)
#True
#False
#print (type(True))
#print (type (False))
#print (7 + 7.5)
#conversion = int("7")
#print (type (conversion))
#print (type (word))
#"obi" == 'obi' 
#print ("obi" == 'obi')
#print ("ada" == 'obi')
#num = 5
#num_2 = 5
#print (num == num_2)
#print (num is num_2)
#name = input("what is your?")
#print (name)
#name = input ('What is your name? ')
#print(name)

#def greeting(name, age, greeting):
 ##   return f"{greeting} {name}, you are {age} years old"

#print((greeting,{"ugoo", age=30, greeting="hi"}))

class House:
    def __init__ (self, roof, door, window, paint, bulgulary_proof):
        self.roof = roof
        self.door = door
        self.window = window
        self.paint = paint
        self.bulgulary_proof = bulgulary_proof
    
    def roofing(self):
        return "aluminium sheet"
    
    def door_material(self):
        return "bullet proof"
    
bungalow = House ("black", "metal", "alumaco", "cream", "armour")    

print (bungalow.door_material())