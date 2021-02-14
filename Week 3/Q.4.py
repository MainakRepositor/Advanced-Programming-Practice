'''4. Develop an python code to call the function fly which exist in both the class parrot and
penguin, how will you achieve using common interface flying test.'''
class Parrot:
    def fly(self):
        print("Parrot can fly")
    
        
class Penguin:
    def fly(self):
        print("Penguin can’t fly")
    

def flying_test(bird):
    bird.fly()

blu = Parrot()
peggy = Penguin()

flying_test(blu)
flying_test(peggy)
