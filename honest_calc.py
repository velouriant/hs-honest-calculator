msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


def is_one_digit(v):
    if v.is_integer() and -10 < v < 10:
        return True
    else:
        return False

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if v1 == 1 or v2 == 1:
        if v3 == "*":
            msg = msg + msg_7
    if v1 == 0 or v2 == 0:
        if v3 in ["*", "+", "-"]:
            msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)

running = True
memory = 0

while running:
    print(msg_0)
    calc = input()

    x, oper, y = calc.split()

    if x == "M":
        x = memory
    if y == "M":
        y = memory

    try:
        x = float(x)
        y = float(y)
    except (TypeError, ValueError):
        print(msg_1)
        continue

    if oper not in ["+", "-", "*", "/"]:
        print(msg_2)
        continue
    else:
        check(x, y, oper)
        if oper == "+":
            result = x + y
        elif oper == "-":
            result = x - y
        elif oper == "*":
            result = x * y
        elif y == 0:
            print(msg_3)
            continue
        else:
            result = x / y

    print(result)

    store_loop = True
    while store_loop:
        print(msg_4)
        store_ans = input()

        if store_ans == "y":
            if is_one_digit(result):
                print (msg_10)
                first_try = input()
                if first_try == "y":
                    print (msg_11)
                    second_try = input()
                    if second_try == "y":
                        print(msg_12)
                        third_try = input()
                        if third_try == "y":
                            memory = result
                            store_loop = False
                        else:
                            store_loop = False
                    else:
                        store_loop = False
                else:
                    store_loop = False
            else:
                memory = result
                store_loop = False
        if store_ans == "n":
            store_loop = False

    cont_loop = True
    while cont_loop:
        print(msg_5)
        cont_ans = input()

        if cont_ans == "y":
            cont_loop = False
        if cont_ans == "n":
            cont_loop = False
            running = False
