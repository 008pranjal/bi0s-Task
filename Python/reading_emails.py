import re
def reading_emails():
    f= open("list_of_mails.txt","r")
    
    for i in f:
        m = re.match(r'^[a-z0-9!#$%^&*{}|~_+-=/]+([.a-z0-9!#$%^&*{}|~_+-=/]+)*[^.]@[-]*[a-zA-Z0-9]+[-]*(\.[a-zA-Z0-9]{1,3})$', i)
        n = re.match(r'(@[0-9]+\.[a-zA-Z0-9]{1,3})$', i)
        if m != None:
            if n==None:
                print(i)
        


if __name__=="__main__":
    reading_emails()