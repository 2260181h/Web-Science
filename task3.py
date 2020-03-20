f = open("3k1.json", "r")
content = f.readlines()
f.close()

RT = {}
AT = {}

for i in range(len(content)):
    text = content[i].split(",")[3][7:]
    userID = content[i].split(",")[1][5:]
    #print (text)
    #print ("This is iiiiiii",i)
    for j in range(len(text)):
        #print("emmmmmmm, so.. what's j??", j)
        if text[j] == '@':
            #print ("Where it happen???",text[j+1])
            k = 0
            while (text[j+k] != " " or text[j+k] != ":") and (j!=len(text)-1 and j+k <len(text)-1):
                userName = text[j:j+k]
                #print ("The user name", userName)
                if text[j+k] == " " or j==len(text)-1:
                    if userID in AT.keys():
                        if userName in AT[userID].keys():
                            AT[userID][userName] = AT[userID][userName] + 1
                        else:
                            AT[userID][userName] = 1
                    else:
                        AT[userID] = {userName:1}
                    #print (AT)
                    break
                elif text[j+k] == ":":
                    #print("have you been here?")
                    if userID in RT.keys():
                        if userName in RT[userID].keys():
                            RT[userID][userName] = RT[userID][userName] + 1
                        else:
                            RT[userID][userName] = 1
                    else:
                        RT[userID] = {userName:1}
                    #print (RT)
                    break
                k = k + 1
                #print (k)
                
                

#print (RT)
#print (AT)
f0 = open("RT.txt", "w")
f1 = open("AT.txt", "w")

f0.write(str(RT))
f1.write(str(AT))

f0.close()
f1.close()
    
