def codeInverse(mot):
    result=""
    for i in range(len(mot)-1,-1,-1): # len(mot)-1 >= i >= 0
        # soit j un compteur incrémenté à chaque passage de boucle (sousentendu ici car boucle for)
        result+=mot[i] # la i-ème lettre du mot en clair devient la j-ème lettre du mot crypté
    return result

def scan(lettre, alphabet):
    y=0
    while (lettre!=alphabet[y]): #si la i-ème lettre du mot est dans l'alphabet (à l'index y), alors fin de boucle
            y+=1 #passage à la lettre suivante de l'alphabet
            if y==len(alphabet): #si la i-ème lettre n'est pas dans l'alphabet
                print("attention: un des caractères du mot n'est pas dans l'alphabet !")
                exit()
    return y

def codeCezar(alphabet,mot,cle):
    result=""
    for i in range(len(mot)): # 0 <= i <= len(mot)-1
        y=scan(mot[i],alphabet) # position de la i-ème lettre du mot dans l'alphabet ; copions la valeur de y à cette étape sous le nom x
        y=(y+cle)%len(alphabet) # décalage avec la clé cézar (y congru à x + cle modulo la taille de l'alphabet)
        result+=alphabet[y] #la i-ème lettre du mot en clair d'index x dans l'alphabet devient la i-ème lettre du mot crypté d'index y. 
    return result
def decodeCezar(alphabet,mot,cle):
    result=""
    for i in range(len(mot)): # 0 <= i <= len(mot)-1
        y=scan(mot[i],alphabet) # position de la i-ème lettre du mot dans l'alphabet ; copions la valeur de y à cette étape sous le nom x
        y=(y-cle)%len(alphabet) # décalage avec la clé cézar (y congru à x - cle modulo la taille de l'alphabet)
        result+=alphabet[y] #la i-ème lettre du mot en clair d'index x dans l'alphabet devient la i-ème lettre du mot crypté d'index y. 
    return result

def codeCezarAff(alphabet,mot,a,b):
    result=""
    for i in range(len(mot)): # 0 <= i <= len(mot)-1
        y=scan(mot[i],alphabet) # position de la i-ème lettre du mot dans l'alphabet ; copions la valeur de y à cette étape sous le nom x
        y=(a*y+b)%len(alphabet) # cryptage affine (y congru à a*x+b modulo la taille de l'alphabet)
        result+=alphabet[y] #la i-ème lettre du mot en clair d'index x dans l'alphabet devient la i-ème lettre du mot crypté d'index y. 
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
    return [r1,u1,v1] # retourne l'identité de bézout

def inv(a,modulo):
    t=euclideEtt(a,modulo) #import de l'identité de bézout
    if t[0]==1: #si le pgcd=1
        return t[1] # retourne l'inverse modulaire de a :(u)
    else: #si le pgcd!=1
        print("attention: le coefficient A de la fonction affine n'est pas premier avec la taille de l'alphabet !")
        exit()
def decodeCezarAff(alphabet,mot,a,b):
    result=""
    for i in range(len(mot)): # 0 <= i <= len(mot)-1
        y=scan(mot[i],alphabet)  # position de la i-ème lettre du mot dans l'alphabet ; copions la valeur de y à cette étape sous le nom x
        y=(inv(a,len(alphabet))*(y-b))%len(alphabet) # décryptage affine (y congru à a'*(x-b) modulo la taille de l'alphabet)
        result+=alphabet[y] #la i-ème lettre du mot en clair d'index x dans l'alphabet devient la i-ème lettre du mot crypté d'index y.
    return result

a=["""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_'abcdefghijklmnopqrstuvwxyz{é}£ ê""",'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
m=["Si deux hommes ont la même opinion. L'un d'eux est de trop","OUI"]

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
        ca=int(input("Choix du coefficient A:"))
        cb=int(input("Choix du coefficient B:"))
        m[i]=codeCezarAff(a[y],m[i],ca,cb)
        print("Mot codé:",m[i])
        m[i]=decodeCezarAff(a[y],m[i],ca,cb)
        print("Mot décodé:",m[i])
    elif choix=="q":
        exit()
    else:
        print("Veuillez entrer un choix valide.")