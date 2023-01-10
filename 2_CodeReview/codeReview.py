def foo1(items):
    result = []
    for i in range(len(items)):

        flag = False
        for j in range(len(result)):
            
            if items[i] == result[j]:
                flag = True
                break
        
        if not flag:
            result.append(items[i])

    return result

def foo2(items):
    result = []
    for i in range(len(items)):

        if not items[i] in result:
            result.append(items[i])

    return result

tmp = ["ahoj", "cau", "ahoj", "cau", "dobry den"]
print("Origin code result")
print(foo1(tmp))
print("My code result")
print(foo2(tmp))