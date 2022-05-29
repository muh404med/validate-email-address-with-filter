
def fun(email):
    s = True
    try:

        if '@' in email.split("@" , 1)[0] or '@' in email.split("@" , 1)[1] :
            s = False
    except IndexError:
        s = False
     
    approved = ["a","@",".", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","_","-",'1', '2', '3', '4', '5', '6', '7', '8', '9']
    if email.find(".")>email.find("@") and email.find("@")>0 :
        for i in email:
            if '.' and '@' in email and 1<len(email.split('.')[1]) < 4 :  
                if i in approved :
                    pass
                else:
                    s = False
            else:
                s = False
            
          
    else:
        s = False
   
             
    if s == True:
        if '-' in email.split('@')[1] or '_' in email.split('@')[1]:
            s = False
    return s












    # return True if s is a valid email, else return False
