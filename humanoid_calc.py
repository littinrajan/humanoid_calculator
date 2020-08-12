#author: littinrajan

def humanoid_calculator(text):
    print("===================== Started Humanoid Calculator =====================")
    OPERAND_DICT = {'add':'Addition','sum':'addition','+':'Addition','addition':'Addition',
                    'difference':'Substraction','substraction':'Substraction','-':'Substraction',
                    'product':'Multiplication','multiply':'Multiplication','*':'Multiplication',
                    'divide':'Division','division':'Division','/':'Division'}
    text = text.strip().lower()
    try:
        operands = [int(operand) for operand in text.split() if operand.isdigit()]
        print("\nOperands:",','.join([str(x) for x in operands]))
        try:
            operations = [OPERAND_DICT[operation] for operation in text.split() if (not(operation.isdigit()) and operation in OPERAND_DICT.keys())]
            print("\nOperations:",','.join(operations))
        except:
            return "\nOops..! No operations found.. Try again.."
    except:
        return "\nOops..! No operands found.. Try again.."
    
    if operands and operations:
    
        if operations[0]=='Addition':
            if len(operands)<2:
                return "\nOops..! Missing operands.. Try Again.."
            else:
                result = operands[0]+operands[1]
                return f"\nResult is {result}"

        if operations[0]=='Substraction':
            if len(operands)<2:
                return "\nOops..! Missing operands.. Try Again.."
            else:
                result = operands[0]-operands[1]
                return f"\nResult is {result}"
    
        if operations[0]=='Multiplication':
            if len(operands)<2:
                return "\nOops..! Missing operands.. Try Again.."
            else:
                result = operands[0]*operands[1]
                return f"\nResult is {result}"

        if operations[0]=='Division':
            if len(operands)<2:
                return "\nOops..! Missing operands.. Try Again.."
            else:
                result = operands[0]/operands[1]
                return f"\nResult is {result}"

    else:
        return "\nOops..! You have missed operands or operation.. Try Again.."


text = "I want to multiply 4 with 6"
output = humanoid_calculator(text)
print(output)