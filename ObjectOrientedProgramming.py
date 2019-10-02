'''
class Error():
    pass

class ValueOfFirstNumberIsZero(Exception):
    pass

class ValueOfSecondNumberIsZero(Exception):
    pass


class RaiseError():

    def Add(self,first,second):
        try:
            result=0
            #result= first/0
            #result=first+b
            if second > 500:
                raise Exception('TooBigNumberError')

            if first==0:
                raise ValueOfFirstNumberIsZero

            if second==0:
                raise ValueOfSecondNumberIsZero

        except ZeroDivisionError:
            print('Error : ZeroDivisionError')  

        except NameError:
            print('Error : NameError') 

        except SyntaxError:
            print('Error : SyntaxError')

        except TypeError:
            print('Error : TypeError')  

        except ValueOfFirstNumberIsZero:
            print('Error :First Number cannot 0')     
        except ValueOfSecondNumberIsZero:
            print('Error :Second Number cannot 0 ')
        except Exception as err:
            print('Error : OtherKindOfError and that is {}'.format(err)) 

        else:
            print('This block (else) run when there is no any kind of error')
            #print('Your answer of the above operation is = ',result)   
            print('Your answer of the above operation is = {}'.format(result)) 

        finally:
            print('This block (finally) has to run in any condition')        


Obj=RaiseError()
first,second=list(map(int,input('Enter two number = ').split()))
Obj.Add(first,second)

'''

'''
class RaiseError:
    def __init__(self, inp1,inp2):
        
        self.inp1=inp1
        self.inp2=inp2
          
    def Add(inp1,inp2):
        return inp1+inp2

print(RaiseError.Add(5,6))

'''



class WorkOnString:
    pass

class WorkOnList(WorkOnString):
    def Maximum(First,Second):
        if First>Second:
            return First
        else:
            return Second  

    # This function is commentted
    def Multiply(self):
        return First*Second   
        
class Dummy:

    def Add(self,first,second):
        return first+second

def Main():  
    Obj=WorkOnList()
    print(WorkOnList.Maximum(9,8))  
    #Obj1=Dummy
    Obj1=Dummy()
    result=Obj1.Add(5,99)
    print(result)
    #Obj.Multiply()
    # print(Obj.Maximum(8,14))


def show():
    print('This is for testing purpose only')   

#print(Obj.Multiply())

if __name__ == "__main__":
    Main()
else:
    print('Else Part')  
   

   
'''
import math
class Areas:
    def AreaOfSqure(self):
        print(self.Side * self.Side)

    def AreaOfCircle(self):
        print(22 * self.Radius * self.Radius//7)  

    def AreaOfTriangle(self):
        print(math.sqrt(3)*self.SlantHeight* self.SlantHeight //4)      

class Dummy(Areas):
    def Show(self):
        print('This function is for testing purpose')

Obj=Dummy()
Obj1=Areas()
Obj.Side=5
Obj.Radius=14
Obj1.SlantHeight=8
Obj.AreaOfSqure()
Obj1.AreaOfTriangle()
#Obj1.AreaOfCircle()
Obj1.Show()
'''

'''
class Person:
     def __init__(self):
         print('This is your Person Class')

     def Function1(self):
         print('This is your Person Class Function')    

     def Function(self):
         print('This is common function and id of this function is Person ')    

class Employee(Person):
    def __init__(self):
        super().__init__()
        print('This is your Employee Class')

    def Function2(self):
        print('This is your Employee class Function')  

    def Function(self):
        super().Function() 
        print('This is common function and id of this function is Employee')  
        

class Workers(Employee):
    def __init__(self):
        super().__init__()
        print('This is your Workers Class')

    def Function3(self):
        print('This is your Workers Class Function')   

    def Function(self):
        super().Function()  
        print('This is common function and id of this function is Workers') 
         

    def Result(self):
        self.Function1()
        super().Function2()
        self.Function3()

    def Final(self):    
        self.Function()

Obj=Workers()
Obj.Result()
# Obj.Function() 
Obj.Final()
             
'''

'''
class Cube:

    def __init__(self,length,breadth,height):
        self.length=length
        self.breadth=breadth
        self.height=height

    def Volume(self):
        Vol=self.length*self.breadth*self.height
        print('Volume is',Vol)    
       
class Area(Cube):

    def __init__(self,length,breadth,height):
        Cube(length,breadth,height)
        self.length=length
        self.breadth=breadth
        self.height=height


    def Ara(self):
        Aras=self.length*self.breadth
        print('Area is',Aras)

class Perimeter(Area):

    def __init__(self,length,breadth,height):
        Area(length,breadth,height)
        self.length=length
        self.breadth=breadth
        self.height=height
       

    def Pera(self):
        Perimtr=2*(self.length*self.breadth+self.breadth*self.height)
        print('Perameter is',Perimtr)

    def Result(self):
        self.Pera()
        self.Ara()
        self.Volume()


Obj=Cube(1,4,5)
Obj.Volume()
'''