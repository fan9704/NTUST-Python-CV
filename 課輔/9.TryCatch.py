try:
    s = input("Enter two numbers, separated by a comma: ")
    raw_input = s.split(",")
    if len(raw_input) != 2:
        raise ValueError("Input must contain one comma")
    a = int(raw_input[0])
    b = int(raw_input[1])
    print("Result is", a / b)
except ZeroDivisionError:
    print("Division by zero!")
except ValueError as e:
    if "comma" in str(e):
        print("A comma may be missing in the input")
    else:
        print("Something wrong in the input")
except:
    print("Something wrong in the input")
else:
    print("No exceptions")
finally:
    print("The finally clause is executed")
