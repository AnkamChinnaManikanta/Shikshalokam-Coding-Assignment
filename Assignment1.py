def check(s):
	return (ord(s[0]) == ord(s[len(s) - 1]));

def sub(s,x):
    result=[]
    n = len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            if len(s[i:j])>1:
                if check(s[i:j]):
                    result.append(s[i:j])
    min_len=100000000
    final=[]
    for i in result:
        if len(i)>=x:
            min_len=min(min_len,len(i))
    for i in result:
        if(len(i)==min_len):
            final.append(i)
    if(final):
        return final
    else:
        return "Not Found"


s =input()
x=int(input())
print(sub(s,x));
