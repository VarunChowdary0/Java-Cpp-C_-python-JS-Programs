# Infix to Postfix

class PostfixConvertor:
    def __init__(self):
        self.stack = []  # operends
        self.queue = []   # operators
        self.OperatorPrecidency =  {
            '+':1,
            '-':1,
            '*':2,
            '/':2,
            '^':3
        }
    def CheckOperatorPrecidencyAndHandle(self,operator):
        if(len(self.queue)==0 or self.queue[-1] == '('):
            self.queue.append(operator)
        else:
            last_operator_in_queue = self.queue[-1]
            last_operator_value = self.OperatorPrecidency[last_operator_in_queue]
            current_operator = operator
            current_operator_value = self.OperatorPrecidency[current_operator]
            # print(f"tocken - {operator} and value:{current_operator_value} , last operator { last_operator_in_queue} : { last_operator_value}")
            if(current_operator_value > last_operator_value):
                # print("Higher Priority: ",operator)
                self.queue.append(operator)
            else:
                self.pushTostack(self.queue.pop())
                self.queue.append(operator)
                # print(f"Lesser Priority {last_operator_in_queue} removed from queue and added { operator } operator to stack ")
        
    def checkForClosingBracket(self,bracket):
        if bracket == ')':
            # print("Closing Bracket must pop queue untill open bracket and append to stack")
            self.PopInQueueUntillOpenBracket()
        else : 
            self.queue.append(bracket)
            # print("Not a closing Bracket Do nothing")
    def pushTostack(self,token):
        self.stack.append(token)
        
    def PopInQueueUntillOpenBracket(self):
        if(len(self.queue)!=0):
            current = self.queue.pop()
            while current != '(':
                self.pushTostack(current)
                if(len(self.queue)!=0):
                    current = self.queue.pop()
                else:
                    break
    def pushToQueue(self,token):
        if token in ['(' , ')']:
            self.checkForClosingBracket(token)
        else:
            self.CheckOperatorPrecidencyAndHandle(token)
    def ReturnThePostFix(self):
        if len(self.queue) != 0 :
            for i in range(len(self.queue)):
                self.pushTostack(self.queue.pop())
        return " ".join(self.stack)

Infix = list(input("Enter Infix (seprate each character with a space): ").split(" "))
Convertor = PostfixConvertor()
for token in  Infix:
    if token in ['+','-','*','/','(',')']:
        Convertor.pushToQueue(token)
    else:
        Convertor.pushTostack(token) 
print(Convertor.ReturnThePostFix())
