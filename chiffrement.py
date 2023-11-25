listAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d = 3

def position(x) :
    pos = listAlpha.find(x)
    return pos


def interposition(word , d):
    wordcrypte = ""
    for i in word:
        pos = position(i)
        poschiffre = (pos + d) % 26
        index = word.find(i)
        wordcrypte += word[index].replace(word[index],listAlpha[poschiffre])
        
    return wordcrypte


def decryptinterposition(word , d):
    wordcrypte = ""
    for i in word:
        pos = position(i)
        poschiffre = (pos - d) % 26
        index = word.find(i)
        wordcrypte += word[index].replace(word[index],listAlpha[poschiffre])
        
    return wordcrypte
        

def crypte(message , d):
    messagecrypte = []
    messageUpper =  message.upper()
    messagesplit = messageUpper.split()
    print(messagesplit) 
    
    for i in messagesplit:
        messagecrypte = messagecrypte + [interposition(i,d)]   
    print(messagecrypte)
    print(" ".join(messagecrypte))       
    return " ".join(messagecrypte)


def decrypte(message , d):
    messagedecrypte = []
    messageUpper =  message.upper()
    messagesplit = messageUpper.split()
    print(messagesplit)
    for i in messagesplit:
        messagedecrypte = messagedecrypte + [decryptinterposition(i,d)]  
    print(messagedecrypte)      
    return " ".join(messagedecrypte)
     
        
            
def clin(liste):
    liste.clear()         

crypte("BONJOUR LES AMIS" , d)
decrypte("ERQMRXU OHV DPLV",d)