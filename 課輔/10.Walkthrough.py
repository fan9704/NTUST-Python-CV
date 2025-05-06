def main():
    try:
        f()
        print("After the function call")
    except IndexError:
        print("Index out of bound")
    except:
        print("Exception in main")

def f():
    try:
        s = "abc"
        print(s[5])  # 錯誤：IndexError
    except ZeroDivisionError:
        print("Divided by zero")
    except IndexError:
        print("Index out of bound")

main()
