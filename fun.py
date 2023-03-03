def solve(a,b):
    try:
        if isinstance(a,str) or isinstance(b,str):
            return "Enter integer"
        print("Line added in 5")
        return a*b*10
    
    except :
        return "Enter Valid value"

