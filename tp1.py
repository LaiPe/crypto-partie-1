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
        y+=cle
        if y>=len(alphabet):
            y=y%len(alphabet)
        result+=alphabet[y]
    return result
def decodeCezar(alphabet,mot,cle):
    cle=cle%len(alphabet)
    result=""
    for i in range(len(mot)):
        y=0
        while (mot[i]!=alphabet[y]):
            y+=1
        result+=alphabet[y-cle]
    return result

a=["""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_'abcdefghijklmnopqrstuvwxyz{é}£ ê""",'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
m=["Si deux hommes ont la même opinion. L'un d'eux est de trop","OUI"]

while(1):
    print("=========CHOIX DE LA METHODE===========")
    print("1. Code Inverse")
    print("2. Code Cézar")
    print("q. Quitter")
    choix=input("choix?:")
    if choix=="1":
        print("=========CODE INVERSE===========")
        i=int(input("Choix du mot:"))

        m[i]=codeInverse(m[i])
        print("Mot codé:",m[i])
        m[i]=codeInverse(m[i])
        print("Mot décodé:",m[i])
    elif choix=="2":
        print("=========CODE CEZAR===========")
        y=int(input("Choix de l'alphabet:"))
        i=int(input("Choix du mot:"))
        c=int(input("Choix de la clé/décalage:"))

        m[i]=codeCezar(a[y],m[i],c)
        print("Mot codé:",m[i])
        m[i]=decodeCezar(a[y],m[i],c)
        print("Mot décodé:",m[i])
    elif choix=="q":
        exit()
    else:
        print("Veuillez entrer un choix valide.")