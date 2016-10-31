def splt(n): # split the number into basic elements i - 2**i
    n=int(n)
    rst=[]
    while n!=0:
        i = 0
        while True:
            if n<2**i:
                break
            i=i+1
        rst=rst+[i-1]
        n=n-2**(i-1)
    return rst

def convert(list): #return replacement solution
    basecase = {7: 'xxx', 6: 'xx.', 5: 'x.x', 4: 'x..', 3: '.xx', 2: '.x.', 1: '..x', 0: '...'}
    rst = {}
    l = [0] * 8
    if list==[]:
        for x in range(0,8):
            rst[basecase[x]]='.'
        return rst
    for i in range(0,8):  # l is a list of 1,0
        if i in list:   # TODO: combination
            rst[basecase[s]]='x'
        else: 
            rst[basecase[s]] = '.'
    return rst

def cellular_automaton(string, n, gen):
    solution=convert(splt(n))  ### find how to input list
    l=len(string)
    m=0
    while m<gen:
        string2 = string + string +string
        p = 0
        while p<l:
            q=string2[p:p+3]
            if p<l-1:  # try: use % function to avoid if
                for i in solution:
                    if i==q:
                        string=string[0:p+1]+solution[i]+string[p+2:]
            else:
                for i in solution:
                    if i==q:
                        string=solution[i]+string[1:]
            p=p+1
        m=m+1
    return string


# There was an error defining your procedure for the inputs `...x....`, `0`, `1`.

# print (cellular_automaton('...x....', 0, 1))

# print(cellular_automaton('xx.xxxxx', 125, 1))
#>>> .xxx....

# print (cellular_automaton('.x.x.x.x.', 17, 2))
# # >>> xxxxxxx..
# print (cellular_automaton('.x.x.x.x.', 249, 3))
# #>>> .x..x.x.x
# print (cellular_automaton('...x....', 125, 1))
# #>>> xx.xxxxx
# print (cellular_automaton('...x....', 125, 2))
# # >>> .xxx....
# print (cellular_automaton('...x....', 125, 3))
# #>>> .x.xxxxx
# print (cellular_automaton('...x....', 125, 4))
# #>>> xxxx...x
# print (cellular_automaton('...x....', 125, 5))
# #>>> ...xxx.x
# print (cellular_automaton('...x....', 125, 6))
# #>>> xx.x.xxx
# print (cellular_automaton('...x....', 125, 7))
# #>>> .xxxxx..
# print (cellular_automaton('...x....', 125, 8))
# #>>> .x...xxx
# print (cellular_automaton('...x....', 125, 9))
# #>>> xxxx.x.x
# print (cellular_automaton('...x....', 125, 10))
# # >>> ...xxxxx
