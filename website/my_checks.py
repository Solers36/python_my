

def awesome_input(message, posible_values, modifire):
    print(message)
    
    while True:
        if posible_values != None:
            print("posible values:", posible_values)
        try:
            result = input()
            if modifire != None:
                result = modifire(result)
            if posible_values == None:
                return result

            if posible_values.__contains__(result):
                return result
            else:
                print("imposible value!\n")
        except ValueError:
            print("Wrong input type. Can't cast to  "+ str(modifire))

def string_to_int(param):
    return int(param)

# print(awesome_input("input some", None, None))
# print(awesome_input("input None", ["None"], None))
# print(awesome_input("input Some", ["Some"], str))
# print(awesome_input("input Some or Other", ["Some", "Other"], str))
# print(awesome_input("input 1,2,3 or4", [1,2,3,4], int))
# print(awesome_input("input 3.45 only", [3.45], float))
i = awesome_input("input int", [1,2,3,4,6,8,234131], string_to_int)
print(i)


