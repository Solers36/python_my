

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
            print("Wrong input type. Can't cast to  " + str(modifire))



