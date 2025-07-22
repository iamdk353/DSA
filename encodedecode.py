
def encode( strs):
    res=""
    for i in strs:
        res+=f"{len(i)}#{i}"
    return res

def decode( s: str) :
    i=0
    res=[]
    while i<len(s):
        j=i
        while(s[j]!="#"):
            j+=1
        length=int(s[i:j])
        i=j+1
        j=i+length
        res.append(s[i:j])
        i=j
    return res


# print(encode(["hii","hello","ma","ton","prem","karo","chu"]))
print(decode("3#hii5#hello2#ma3#ton4#prem4#karo3#chu"))


            

        
