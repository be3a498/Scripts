import os
import time
import re
import sys

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
slowprint("[!] Starting ......")
time.sleep(3)


print("""                                                                           
                                                                           
BBBBBBBBBBBBBBBBB                      333333333333333                     
B::::::::::::::::B                    3:::::::::::::::33                   
B::::::BBBBBB:::::B                   3::::::33333::::::3                  
BB:::::B     B:::::B                  3333333     3:::::3                  
  B::::B     B:::::B    eeeeeeeeeeee              3:::::3  aaaaaaaaaaaaa   
  B::::B     B:::::B  ee::::::::::::ee            3:::::3  a::::::::::::a  
  B::::BBBBBB:::::B  e::::::eeeee:::::ee  33333333:::::3   aaaaaaaaa:::::a 
  B:::::::::::::BB  e::::::e     e:::::e  3:::::::::::3             a::::a 
  B::::BBBBBB:::::B e:::::::eeeee::::::e  33333333:::::3     aaaaaaa:::::a 
  B::::B     B:::::Be:::::::::::::::::e           3:::::3  aa::::::::::::a 
  B::::B     B:::::Be::::::eeeeeeeeeee            3:::::3 a::::aaaa::::::a 
  B::::B     B:::::Be:::::::e                     3:::::3a::::a    a:::::a 
BB:::::BBBBBB::::::Be::::::::e        3333333     3:::::3a::::a    a:::::a 
B:::::::::::::::::B  e::::::::eeeeeeee3::::::33333::::::3a:::::aaaa::::::a 
B::::::::::::::::B    ee:::::::::::::e3:::::::::::::::33  a::::::::::aa:::a
BBBBBBBBBBBBBBBBB       eeeeeeeeeeeeee 333333333333333     aaaaaaaaaa  aaaa
                                                                           
                  fb.com/Rabeaa.MR
              https://github.com/be3a498                                                   
        I am Not in Danger , Skyler , I am The Danger  


        Features : 

        1 ==== >> [+] Combo Separator To Email.txt & Pass.txt .
        2 ==== >> [+] Email Extractor from List .                                                           
        3 ==== >> [+] Remove Duplicated From Any List .
        4 ==== >> [+] Email Filter .
        5 ==== >> [+] Combo Converter From Mail:Pass To User:Pass .                                                           
                                                                           
                                                                           """)
print("_____________________________________________________________________________________")
slowprint("+====> Simple Script To Help U With Combo Or List ........")

def splitter():
    a = 0


    def update_cmd_title(num):
            os.system('title '+"Number Of Lines [{}]".format(
                num
            ))

    files = open("list.txt" , "r").readlines()

    #x = "word:man:women"
    #z = x.split(":")
    for z in files :
        a += 1
        x = z.split(":")
        #print(x[0])
        #print(x[1])
        with open ("email.txt" , "a+") as f :
            f.write(x[0])
            f.close()
        with open("pass.txt" , "a+") as f :
            f.write(x[1])
            f.close()
        update_cmd_title(a)
    time.sleep(1000)


def emailExtractor():
    def grab_email(file):
        a = 0
        def update_cmd_title(num):
            os.system('title '+"Number Of Emails [{}]".format(
                num
            ))
        email_pattern = re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b',re.IGNORECASE)
        found = set()
        if os.path.isfile(file):
            for line in open(file, 'r'):
                found.update(email_pattern.findall(line))
            for email_address in found:
                print (email_address)
                with open("valid.txt" , "a+") as f:
                    f.write(email_address + "\n")
                    f.close
                    a+=1
            update_cmd_title(a)
            
        print("_____________________________________")
        print("Number Of Emails : " + str(a))


    if __name__ == '__main__':
        be3a = str(input("Your File Path : "))
        grab_email(be3a)
        
        time.sleep(1000)


def removeDuplicated():
    def update_cmd_title(num):
        os.system('title '+"Number Of Lines [{}]".format(
            num
        ))

    def removeDupli():

            xfile = str(input("Your File Path : "))
            lines_seen = set()  
            outfile = open('clean.txt', "w")
            infile = open(xfile, "r")
            for line in infile:
                #print (line)
                if line not in lines_seen: 
                    outfile.write(line)
                    lines_seen.add(line)
            outfile.close()
            


    removeDupli()
    a = 0
    print ("The file clean.txt is as follows")
    for line in open('clean.txt', "r"):
        a += 1
        print(line)
            
    update_cmd_title(a)
    time.sleep(1000)


def emailFilter():
    def slowprint(s):
        for c in s + '\n' :
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(10. / 100)
    slowprint("[!] Starting ......")
    time.sleep(3)




    gmail = ("gmail.com\n")
    yahoo = ('yahoo.com\n')
    yahooo = ('yahoo.fr\n')
    outlook = ('outlook.com\n')
    web = ("web.com\n")
    hotmail = ('hotmail.com\n')
    wanadoo = ("wanadoo.com\n")
    gmx = ("gmx.com\n")
    aol = ("aol.com\n")
    msn = ("msn.com\n")
    live = ("live.com\n")
    yandex = ("yandex.ru\n")
    bk = ("bk.ru\n")
    inbox = ("inbox.ru\n")
    mailru = ("mail.ru\n")
    a = ('prodigy.net\n')
    b = ('rogers.com\n')
    c = ('cox.net\n')
    d = ('centurytel.net\n')
    f = ('juno.com\n')
    g = ('comcast.net\n')
    h = ('sympatico.ca\n')
    l = ('earthlink.net\n')
    k = ('bellsouth.net\n')
    v = ('verizon.net\n')
    print("__________________________________________________\n")
    be3a=input("Enter Your mail-list : ")
    list = open((be3a), "r")
    hot = list.readlines()

    slowprint("Filtering .....")

    for tezo in hot : 
              if tezo.endswith(gmail) :
                        file = open("gmail.txt","a")
                        file.write((tezo)+"")
                        file.close()        
              if tezo.endswith(yahoo) :
                        file = open("yahoo.txt","a")
                        file.write((tezo)+"")
                        file.close()    
              if tezo.endswith(yahooo) :
                        file = open("yahoo.txt","a")
                        file.write((tezo)+"")
                        file.close()          
              if tezo.endswith(outlook) :
                        file = open("outlook.txt","a")
                        file.write((tezo)+"")
                        file.close()       
              if tezo.endswith(hotmail) :
                        file = open("hotmail.txt","a")
                        file.write((tezo)+"")
                        file.close()       
              if tezo.endswith(web) :
                        file = open("web.txt","a")
                        file.write((tezo)+"")
                        file.close()  
              if tezo.endswith(aol) :
                        file = open("aol.txt","a")
                        file.write((tezo)+"")
                        file.close() 
              if tezo.endswith(msn) :
                        file = open("msn.txt","a")
                        file.write((tezo)+"")
                        file.close() 
              if tezo.endswith(a) :
                        file = open("other.txt","a")
                        file.write((tezo)+"")
                        file.close() 
              if tezo.endswith(b) :
                        file = open("other.txt","a")
                        file.write((tezo)+"")
                        file.close() 
              if tezo.endswith(c) :
                        file = open("other.txt","a")
                        file.write((tezo)+"")
                        file.close() 
              if tezo.endswith(d) :
                        file = open("other.txt","a")
                        file.write((tezo)+"")
                        file.close() 
              if tezo.endswith(f) :
                        file = open("other.txt","a")
                        file.write((tezo)+"")
                        file.close() 
              if tezo.endswith(g) :
                        file = open("other.txt","a")
                        file.write((tezo)+"")
                        file.close() 
              if tezo.endswith(h) :
                        file = open("other.txt","a")
                        file.write((tezo)+"")
                        file.close() 
              if tezo.endswith(l) :
                        file = open("other.txt","a")
                        file.write((tezo)+"")
                        file.close() 
              if tezo.endswith(k) :
                        file = open("other.txt","a")
                        file.write((tezo)+"")
                        file.close() 
              if tezo.endswith(v) :
                        file = open("other.txt","a")
                        file.write((tezo)+"")
                        file.close() 
              if tezo.endswith(live) : 
                        file = open("live.txt","a")
                        file.write((tezo)+"")
                        file.close() 
              if tezo.endswith(yandex) :
                        file = open("yandex.txt","a")
                        file.write((tezo)+"")
                        file.close() 
              if tezo.endswith(mailru) : 
                        file = open("mail.ru.txt","a")
                        file.write((tezo)+"")
                        file.close() 
              if tezo.endswith(bk) : 
                        file = open("mail.ru.txt","a")
                        file.write((tezo)+"")
                        file.close() 
              if tezo.endswith(inbox) : 
                        file = open("mail.ru.txt","a")
                        file.write((tezo)+"")
                        file.close()
              

    slowprint("[+] Done!")
    time.sleep(1000)

def comboUser():
    a = 0


    def update_cmd_title(num):
            os.system('title '+"Number Of Lines [{}]".format(
                num
            ))
    love = str(input("Your File Path : "))
    files = open(love , "r").readlines()

    #x = "word:man:women"
    #z = x.split(":")
    for z in files :
        a += 1
        x = z.split(":")
        #print(x[0])
        be3a = x[0].split("@")
        with open("out.txt" , "a+") as f :
            f.write(be3a[0] + ":" + x[1])
            f.close()
        update_cmd_title(a)
    time.sleep(1000)


print("____________________________________________________\n")
choice = str(input("[=] Now Enter Num of Ur Choice : "))

if choice == '1':
    slowprint("\n[+] Loading .........\n")
    splitter()
    time.sleep(1000)

elif choice == '2':
    slowprint("\n[+] Loading .........\n")
    emailExtractor()
    time.sleep(1000)

elif choice == '3':
    slowprint("\n[+] Loading .........\n")
    removeDuplicated()
    time.sleep(1000)

elif choice == '4':
    slowprint("\n[+] Loading .........\n")
    emailFilter()
    time.sleep(1000)

elif choice == '5':
    slowprint("\n[+] Loading .........\n")
    comboUser()
    time.sleep(1000)

else :
    slowprint("\n[+] Loading .........\n")
    slowprint("[-] Your Choice Is Wrong ......")
    time.sleep(1000)