def main():
    try:
        f()
        print("2.After the function call")
    except IndexError:
        print("2.Index out of bound")
    except:
        print("2.Exception in main")

def f():
    try:
        s = "abc"
        print(s[5])  # 錯誤：IndexError
    except ZeroDivisionError:
        print("1.Divided by zero")
    except IndexError:
        print("1.Index out of bound")

main()
