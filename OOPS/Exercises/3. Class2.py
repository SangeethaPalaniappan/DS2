# 3. Write a Python program to create a calculator class.
# Include methods for basic arithmetic operations
class calculator:
    def add(self, *arguments):
        sums = 0
        for i in arguments:
            sums += i     
        return sums
    def sub(self, *arguments):
        subs = 0
        for i in arguments:
            subs =  i - subs   
        return subs
    def mul(self, *arguments):
        mult = 1
        for i in arguments:
            mult *= i
        return mult    
    def div(self, *arguments):
        divi = 1
        for x in arguments:
            if x != 0:
                divi = x // divi
            else:
                return "Not definied"    
        return divi    
obj = calculator()
a = calculator.add(obj, 3,3,2,64,79,86)
s = calculator.sub(obj, 10, 23, 40, 80)
m = calculator.mul(obj, 20, 3, 2, 0)
d = calculator.div(obj, 5, 10, 0, 40)
print(a)
print(s)
print(m)
print(d)    