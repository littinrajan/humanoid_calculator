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


text = "I want to multiply  with"
output = humanoid_calculator(text)
print(output)