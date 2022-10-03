from lib2to3.pgen2 import grammar
from this import s
from time import sleep
from unicodedata import name


class MyClass:
    """
    定义一个简单的类实例
    """
    i = 12345
    # 这里的i就是一种属性
    def f(self):
        return "hello world"
    # f是一种方法（函数）

# 实例化
x = MyClass()

# 访问实例中的属性和方法
print("类中的属性为i为：",x.i)
print("类中的方法f的输出为：",x.f())

# 定义people类
class people:
    # define basis attibute 
    name = ''
    age = 0

    # define private attribute 

    _weight = 0

    # build function
    def __init__(self,n,a,w) -> None:
        self.name = n
        self.age = a
        self._weight = w
    
    # build another function
    def myinformation(self):
        print("%s says : i am %d years old ,and my weight is %d kg"%(self.name, self.age, self._weight))

p = people('why', 20, 60)
p.myinformation()

# 类的继承
# 学生是属于people的一种

class student(people):
    grade = ''
    def __init__(self, n, a, w, g) -> None:
        super().__init__(n, a, w)# 
        self.grade = g
    
    def myinformation(self):
        print("%s says:i am %d years old and i am %d grade now"%(self.name, self.age, self.grade))
s = student('why', 20, 60, 15)
s.myinformation()
