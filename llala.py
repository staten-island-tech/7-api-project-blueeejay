def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError: 
        print("Can't divide by Zero")
    else:
        print(result)
    