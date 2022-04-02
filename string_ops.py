def is_palindrome(s):
    s= s.casefold()
    lst=[]
    [lst.append(i)for i in s]
    lst.reverse() 
    ra= "".join(lst)
    if s == ra:
        return print(True)
    else:
        return print(False)


def solve(a,b):
    a_len = len(a) -1
    b_len = len(b)
    astrc_len = b_len - a_len
    substirng = ''
    astrc_loc = a.find('*')
    
    if a.find('*') == -1:
        if a==b:
            return print(True)
        else:
            return print(False)
    
    for i in range(b_len):
        if b[i] != a[i]:
            if a[i] == '*':
                substirng = b[i:i+astrc_len] #b[4:7] b[start:end]
                break
            else:
                return print(False)
    
    a = a.replace('*',substirng)
    if a==b:
        return print(True)
    else:
        return print(False)



def find(substring,string,occurrence):
    start = 0
    count = 0
    for i in range(len(string)):
        x = string.find(substring,start)
        start = x+1
        count+=1
        if count == occurrence:
            return print(x)
        if x == -1:
            return print(-1)



def f(s):
    t = ''
    for i in s:
        t+=i
        k = s.count(t)
        if t*k == s:
            return print(t,k)