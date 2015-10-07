__author__ = 'Darrell.Skogman'
def seven(str):
    str.lower()
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    freqs = []
    letterlist=list(str)
    print(str)

    for i in range (0,len(letterlist)):
        if not(letterlist[i] in alphabet):
            letterlist[i] = ""

    for i in range (0, len(alphabet)):
        c=0
        for j in range (0,len(letterlist)):
            if alphabet[i]==letterlist[j]:
                c=c+1
        alphabet[i]=alphabet[i] + alphabet[i]*c
        frequency = (len(alphabet[i])-1)/len(letterlist)
        freqs.append(frequency)

    alphabet = sorted(alphabet,key = len)
    alphabet = alphabet[::-1]
    freqs = sorted(freqs)
    freqs = freqs[::-1]

    for t in range (0,len(alphabet)):
        print(alphabet[t][0], freqs[t] )

gizmo = input("Enter a string: ")
seven(gizmo)




