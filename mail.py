email=input("Enter you E-mail address: ") #g@g.in , miimum len=6
k,j,d=0,0,0
if(len(email)>=6): # check the length of the mail 
    if(email[0].isalpha()): # check your mail and ensure start with alphabet
        if(("@" in email)and(email.count("@")==1)): # check the @ sign in your mail and it can only 1 time enter in your mail
            if((email[-4]==".")or(email[-3]==".")): # check the position of the dot and check its position on the revetse side of the mail
                for i in email: # loop used here to check the entire mail
                    if(i==i.isspace()): # check the mail and ensure there is no space enter in it
                        k=1
                    elif(i==i.isupper()): # it helps to check the mail and indicate the lower case==upper case letter
                        j=1
                    elif(i==i.isdigit()): #check the mail and after the first letter you can enter the digit 
                        continue
                    elif((i=="_")or(i==".")or(i=="@")): # ensure if user can enter any special letter rather than . _ @ msg of invalid mail
                        continue
                    else:
                        d=1
            if((k==1)or(j==1)or(d==1)):
                print("Your email is invalid due to space in your mail or maybe be you can enter any of the special character rather than the dot, underscore or at the rate sign!!")
            else:
                print("The position of the dot is in wrong position!")
        else:
            print("In your mail you can enter the '@' sign more than one time. So, please correct it!")
    else:
        print("Email start with the number ake sure write your mail start with the alphabet!")
else:
    print("Wrong Email due to the minimum length!")