#coding:utf-8

class ClassA(object):
    string = '这时一个字符串。'

    def instancefunc(self):
        print ('这是一个实例方法。')
        print(self)

    @classmethod
    def classfun(cls):
        print('这是一个类方法。')
        print(cls)

    @staticmethod
    def staticfun():
        print('这是一个静态方法。')

test = ClassA()
test.instancefunc()
test.classfun()
test.staticfun()

print (test.string)

ClassA.instancefunc(test)
ClassA.instancefunc(ClassA)
ClassA.classfun()
ClassA.staticfun()
