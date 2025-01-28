class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)

c1=Complex(5,9)
c1.showNumber()

c2=Complex(8,6)
c2.showNumber()

c3=c1+c2
c3.showNumber()
