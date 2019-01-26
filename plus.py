def plus(k):
    if (k>0):
        result=k+plus(k-1)
        # print(result)
    else:
        result=0
    return result
# print("the example results:\n".title())
# plus(6)
print("the final example result:".title())
result=plus(6)
print(result)