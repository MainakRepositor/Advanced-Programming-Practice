# defining private variables
class Privacy:
    def __init__(self, val):
        self.__val = 900;   
        print("Private data member =",self.__val,"\n")
value = Privacy(800);
print("Value not changable\n")
value.__val;
