def foo(list, result) :
     if (len(list) == 0):
       return result
     else:
       dd = list[0]
       del list[0]
       value = dd + dd
       if (value < 0):
         return foo(list, result)
       else:
         return foo(list, result)[value]

arr = []
list = [-1,1,-2,2,-3,3]
ans = foo(list, arr)

print(ans)