def solve(a,b):
    try:
        if isinstance(a,str) or isinstance(b,str):
            return "Enter integer"
        return a*b*10
    
    except :
        return "Enter Valid value"

