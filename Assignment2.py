s=input()
s=list(s)
n=len(s)
done=[]
for i in range(n):
        
        asci=ord(s[i])
        if asci%2==0 and (i-1 not in done) and i!=n-1:
            k=asci%7
            if(k!=0):
                if(ord(s[i+1])+k)<=126:
                    s[i+1]=chr(ord(s[i+1])+k)
                    done.append(i+1)
                else:
                    s[i+1]=chr(83)
                    done.append(i+1)
        elif asci%2!=0 and (i-1 not in done) and i!=0:
            k=asci%5
            if k!=0:
                if(ord(s[i-1])-k)<=126:
                    s[i-1]=chr(ord(s[i-1])-k)
                    done.append(i-1)
                else:
                    s[i-1]=chr(83)
                    done.append(i-1)
print("".join(s))
