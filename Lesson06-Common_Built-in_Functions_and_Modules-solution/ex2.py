def caesar_cipher(name,shift):
    n=name
    l=len(name)
    s=shift
    M=''
    #print(name.lower())#全小寫印出
   
    for i in range(l):
        aa=ord(name[i])+s #ord是數字轉編碼(a=97,z=122)．chr是編碼轉數字
        if aa>122:
            aa=(aa-123)+97 #超過122將差值加回去
        M=M+(chr(aa))
    return M

x=caesar_cipher("xviLLAge",3)
print(x)



'''
def caesar_code(s,t):
    s = str(s)
    t = int(t)
    l = []
    for i in range(len(s)):
        aa = ord(s[i])+t
        if aa > 122:
            b = aa-123
            aa = 97+b
        l.append(chr(aa))
        
    return ''.join(l)
caesar_code('xvillage',3)
'''