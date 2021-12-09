import math


def question1(x:str, y:str) -> str:
    res = "{}{}{}{}".format(x, y, y, x)
    return res


def question2(Sam_smile:bool, Tam_smile:bool) -> bool:
    if Sam_smile == True and Tam_smile == True:
        return True
    elif Sam_smile == False and Tam_smile == False:
        return True
    else:
        return False


def question3(input_str:str) -> str:
    if len(input_str) == 0:
        return ""
    if len(input_str) == 1:
        return input_str
    start = input_str[0]
    end = input_str[-1]
    res = "{}{}{}".format(end,input_str[1:-1],start)
    return res


def question4(x:int, y:int) -> bool:
    if x == 10 or y == 10:
        return True
    if x+y == 10:
        return True
    return False


def question5(x:str) -> str:
    if x.startswith("not"):
        return x
    else:
        res = "not{}".format(x)
        return res

print(question5("nota"))

question3("Hello")
question3("Hl")
question1("Welcome","ToCanada")

def leastMinutes( n) :
    if n == 1:
        return 1
    else:
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = i
            min = i
            for j in range(i):
                if math.ceil((i / 2 ** j)) + j < min:
                    # dp[i] = math.ceil((i / 2 ** j)) + j
                    min = math.ceil((float(i) / 2 ** j)) + j
                    dp[i] = min


        print(dp)

    return dp[n]


leastMinutes(7)