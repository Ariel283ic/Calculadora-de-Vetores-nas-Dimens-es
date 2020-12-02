'''
Instructions
Create a simple addition or subtraction function that does the following:

Method myMath()
This method will take 3 parameters and will return a tuple. The parameters are in the following order:

Operator: expects + or - in method
Number, first number entered
Number, second number entered

The method has the following rules
Returns a Tuple with the word "Addition" if "+" is entered OR "Subtraction" if "-" with the solution math problem as a string value

'''
class MATH():
    def myMath(self, param1, param2, param3):
        if param2 == "+":
            self.result = float(param1)+float(param3)
            self.operator = "Addition"
        else:
            self.result = float(param1)-float(param3)
            self.operator = "Subtraction"
        return (self.operator, str(self.result))

me = MATH()
print(me.myMath(10, '+', 20))