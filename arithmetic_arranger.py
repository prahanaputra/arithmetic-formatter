def arithmetic_arranger(problems, calc = False):
    split_problems = [item.split() for item in problems]
    top = []
    mid = []
    math = []
    bottom = []

    for problem in split_problems:
        top.append(problem[0])
        math.append(problem[1])
        mid.append(problem[2])
    
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for h in math:
        if h == "+" or h == "-":
            continue
        else:
            return "Error: Operator must be '+' or '-'."
            
        
    for o,p in zip(top, mid):
        try:
            int(o)
            int(p)
        except:
            return "Error: Numbers must only contain digits."
            

    for n,m in zip(top, mid):
        if len(n) > 4 or len(m) > 4:
            return "Error: Numbers cannot be more than four digits."


    for f,g,i in zip(top, mid, math):
        if i == "+":
            bottom.append(str(int(f) + int(g)))
        else:
            bottom.append(str(int(f) - int(g)))

    arithmetic_arranger = ""
    
    for index, a in enumerate(split_problems):
        x = max(len(a[0]),len(a[2])) + 1
        arithmetic_arranger += " " + " " * (x-len(a[0])) + a[0]
        if index < (len(split_problems) - 1):
            arithmetic_arranger += "    "
    
    arithmetic_arranger += "\n"

    for index, a in enumerate(split_problems):
        x = max(len(a[0]),len(a[2])) + 1
        arithmetic_arranger += a[1] + " " * (x-len(a[2])) + a[2]
        if index < (len(split_problems) - 1):
            arithmetic_arranger += "    "
    
    arithmetic_arranger += "\n"

    for index, a in enumerate(split_problems):
        x = max(len(a[0]),len(a[2])) + 1
        arithmetic_arranger += "-" * (x+1)
        if index < (len(split_problems) - 1):
            arithmetic_arranger += "    "
    
    if calc == True:
        arithmetic_arranger += "\n"
        for index, (a, b) in enumerate(zip(split_problems, bottom)):
            x = max(len(a[0]),len(a[2])) + 2
            arithmetic_arranger += " " * (x-len(b)) + b
            if index < (len(split_problems) - 1):
                arithmetic_arranger += "    "
            
    return arithmetic_arranger