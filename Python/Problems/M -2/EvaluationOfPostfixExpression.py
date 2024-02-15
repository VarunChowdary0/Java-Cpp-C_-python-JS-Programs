# Evaluate the Postfix
class Evaluate:
    def __init__(self):
        self.stack = []
    def isPostfixValid(self,Postfix):
        operators = 0
        nums = 0
        for token in Postfix:
            if token in  ['+','-','*','/']:
                operators+=1
            elif (token[0])  in ['0','1','2','3','4','5','6','7','8','9']:
                nums+=1
            else :
                return False
        if(nums == operators+1):
            return True
        return False
    def pushTostack(self,token):
        self.stack.append(token)
        return
    def getLastTwoNums(self):
        lastOne = self.stack.pop()
        lastButOne = self.stack.pop()
        return lastButOne , lastOne
    def Evaluate(self,operation):
        a , b = self.getLastTwoNums()
        if(operation == '+'):
            res = a + b
        elif(operation=='-'):
            res = a - b
        elif(operation=='*'):
            res = a * b
        elif(operation=="/"):
            res = a / b
        self.pushTostack(res)
    def getResult(self):
        return int(self.stack.pop())

Postfix = list(input("Enter postfix (seprate each character with a space): ").split(" "))
evaluator = Evaluate()
if evaluator.isPostfixValid(Postfix):
    for token in  Postfix:
        if token in ['+','-','*','/']:
            evaluator.Evaluate(token)
        else:
            evaluator.pushTostack(int(token)) 
    print(evaluator.getResult())
else : 
    print("Invalid Postfix")