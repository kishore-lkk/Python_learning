from itertools import permutations
import itertools
results = []
numbers = [1, 3, 4, 6]
operator = ["+", "-", "*", "/"]
flag = True

def function_1(p,o):
    try:
        operation = f"(({p[0]}{o[0]}{p[1]}){o[1]}{p[2]}){o[2]}{p[3]}"
        result = eval(operation)
        return result
    except Exception:
        return 0

def function_2(p,o):
    try:
        operation = f"({p[0]}{o[0]}({p[1]}{o[1]}{p[2]})){o[2]}{p[3]}"
        result = eval(operation)
        return result        
    except Exception:
        return 0
            
def function_3(p,o):
    try:
        operation = f"{p[0]}{o[0]}(({p[1]}{o[1]}{p[2]}){o[2]}{p[3]})"
        result = eval(operation)
        return result
    except Exception:
        return 0
            
def function_4(p,o):
    try:
        operation = f"{p[0]}{o[0]}({p[1]}{o[1]}({p[2]}{o[2]}{p[3]}))"
        result = eval(operation)
        return result
    except Exception:
        return 0
     
try:
    for p in permutations(numbers):
        for o in list(itertools.product(operator,repeat=3)):
            result_1 = function_1(p,o)
            result_2 = function_2(p,o)
            result_3 = function_3(p,o)
            result_4 = function_4(p,o)
            print(result_1, result_2, result_3, result_4)
            if result_1 == 24:
                print(f"found - combination : {p} operation : {o} and the function used is ((a.b).C).d")
                flag = False
                break
            elif result_2 == 24:
                print(f"found - combination : {p} operation : {o} and the function used is (a.(b.C).d")
                flag = False
                break
            elif result_3 ==24:
                print(f"found - combination : {p} operation : {o} and the function used is a.((b.C).d)")
                flag = False
                break
            elif result_4 ==24:
                print(f"found - combination : {p} operation : {o} and the function used is a.(b.(C.d))")
                flag = False
                break
        if flag:
            pass
        else:
            break
except Exception as e:
    print(str(e), p, o)
