'''Q5. Develop a Python program to show successful working of super() function '''
class Square: 
     def __init__(self, side): 
         self.side = side 
  
     def area(self): 
         return self.side * self.side 
class Cube(Square): 
	def area(self): 
		return super().area() * 6

	def volume(self): 
		return super().area() * self.side() 

print("Classes executed successfully!")