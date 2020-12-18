"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

table = dict()

def sum_diff(q):
    q = list(q)
    add = dict()
    minus = dict()
    answers = dict()

    for num in q:
        result = f(num)
        answers[num] = result
    
    print(answers)
    for i in range(len(q)):
        for j in range(len(q)):
            addition_result = f(q[i]) + f(q[j])
            add_key = (q[i],q[j])
            add[add_key] = addition_result
            # print(add_key,add[add_key],"add table")


            sub_result = f(q[i]) - f(q[j])
            sub_key = (q[i],q[j])
            minus[sub_key] = sub_result
            # print(sub_key,minus[sub_key],"minus table")

    for key in add:
        for key2 in minus:
            if add[key] is minus[key2]:
                print(f"f({key[0]}) + f({key[1]}) = f({key2[0]}) - f({key2[1]})" ,end = "    ")
                print(f"{answers[key[0]]} + {answers[key[1]]} = {answers[key2[0]]} - {answers[key2[1]]}    "   , end = "  " )
                print(f"==== {add[key]}")
                
                
                   
sum_diff(q)
