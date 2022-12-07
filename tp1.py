def codeInverse(mot):
    result=""
    for i in range(len(mot)-1,-1,-1):
        result+=mot[i]
    return result

def codeCezar(alphabet,mot,cle):
    result=""
    for i in range(len(mot)):
        y=0
        while (mot[i]!=alphabet[y]):
            y+=1
            if y==len(alphabet):
                print("attention: un des caractères du mot n'est pas dans l'alphabet !")
                exit()

        y=y+cle%len(alphabet)
        result+=alphabet[y]
    return result
def decodeCezar(alphabet,mot,cle):
    result=""
    for i in range(len(mot)):
        y=0
        while (mot[i]!=alphabet[y]):
            y+=1
            if y==len(alphabet):
                print("attention: un des caractères du mot n'est pas dans l'alphabet !")
                exit()
        
        y=y-cle%len(alphabet)
        result+=alphabet[y]
    return result

def codeCezarAff(alphabet,mot,a,b):
    result=""
    for i in range(len(mot)):
        y=0
        while (mot[i]!=alphabet[y]):
            y+=1
            if y==len(alphabet):
                print("attention: un des caractères du mot n'est pas dans l'alphabet !")
                exit()

        y=(a*y+b)%len(alphabet)

        result+=alphabet[y]
    return result
def euclideEtt(a,b):
    r1=b
    r2=a
    u1=0
    v1=1
    u2=1
    v2=0
    while r2!=0:
        q=r1//r2
        
        r3=r1
        u3=u1
        v3=v1

        r1=r2
        u1=u2
        v1=v2

        r2=r3-q*r2
        u2=u3-q*u2
        v2=v3-q*v2
    return [r1,u1,v1]

def inv(a,modulo):
    t=euclideEtt(a,modulo)
    if t[0]==1:
        return t[1] #u
    else:
        print("erreur")
        exit()
def decodeCezarAff(alphabet,mot,a,b):
    result=""
    for i in range(len(mot)):
        y=0
        while (mot[i]!=alphabet[y]):
            y+=1
        y=inv(a,len(alphabet))*(y-b)
        y=y%len(alphabet)
        result+=alphabet[y]
    return result
a=["""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_'abcdefghijklmnopqrstuvwxyz{é}£ ê""",'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
m=["Si deux hommes ont la même opinion. L'un d'eux est de trop","OUI"]

print(euclideEtt(3,11))

while(1):
    print("=========CHOIX DE LA METHODE===========")
    print("1. Code Inverse")
    print("2. Code Cézar")
    print("3. Code Cézar Affine")
    print("q. Quitter")
    choix=input("choix?:")
    if choix=="1":
        print("=========CODE INVERSE===========")
        print("m=",m,sep="")
        i=int(input("Choix du mot:"))

        m[i]=codeInverse(m[i])
        print("Mot codé:",m[i])
        m[i]=codeInverse(m[i])
        print("Mot décodé:",m[i])
    elif choix=="2":
        print("=========CODE CEZAR===========")
        print("a=",a,sep="")
        print("m=",m,sep="")
        y=int(input("Choix de l'alphabet:"))
        i=int(input("Choix du mot:"))
        c=int(input("Choix de la clé/décalage:"))

        m[i]=codeCezar(a[y],m[i],c)
        print("Mot codé:",m[i])
        m[i]=decodeCezar(a[y],m[i],c)
        print("Mot décodé:",m[i])
    elif choix=="3":
        print("=========CODE CEZAR AFFINE===========")
        print("a=",a,sep="")
        print("m=",m,sep="")
        y=int(input("Choix de l'alphabet:(0 ou 1)"))
        i=int(input("Choix du mot:(0 ou 1)"))
        ca=int(input("Choix du coefficient du polynôme:"))
        cb=int(input("Choix du décalage du polynôme:"))
        m[i]=codeCezarAff(a[y],m[i],ca,cb)
        print("Mot codé:",m[i])
        m[i]=decodeCezarAff(a[y],m[i],ca,cb)
        print("Mot décodé:",m[i])
    elif choix=="q":
        exit()
    else:
        print("Veuillez entrer un choix valide.")