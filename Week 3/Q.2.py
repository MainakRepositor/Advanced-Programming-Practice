'''2.Develop an python code for the following scenario, Class D is an derived class which has
the properties class B via class B1 and class B2, create an object to call the member functions
of B, B1 and B2 also sketch the what type of inheritance it belongs to.'''
class B:
    def Hello(self):
        return 'Hello'


class B1(B):  
    def Python(self):  
        return 'Python'
class B2(B):  
    def How(self):  
        return 'How are you?'
class D(B1,B2):  
    def Divide(self):  
        return 'Today'
d = D()  
print("D is a subclass of B2?",issubclass(D,B2))  
print("B1 is a subclass of B2?",issubclass(B1,B2))  
print("B1 is a subclass of B?",issubclass(B1,B))
print("So, D is a subclass of B?",issubclass(D,B))