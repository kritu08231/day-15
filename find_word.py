# WAF Search if the word "learning" exists in the file or not.
def check_word():
    with open("practise.txt","r")as  f:
        data = f.read()
        if(data.find("learning")):
            print("learning Exist in file")
        else:
            print("Not exist")

check_word()
