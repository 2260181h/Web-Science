f = open("3k3.json", "r")
content = f.readlines()
f.close()

RT = {}
AT = {}

#check every tweets
for i in range(len(content)):
    text = content[i].split(",")[3][7:]
    userID = content[i].split(",")[1][5:]
    for j in range(len(text)):          #indexing the text of each tweet
        if text[j] == '@':
            k = 0
            #check if it's retweet or quote and make sure the index will not be out of range
            while (text[j+k] != " " or text[j+k] != ":") and (j!=len(text)-1 and j+k <len(text)-1):
                userName = text[j:j+k]
                #quote will always followed by blank space
                if text[j+k] == " " or j==len(text)-1:
                    if userID in AT.keys():
                        if userName in AT[userID].keys():
                            AT[userID][userName] = AT[userID][userName] + 1
                        else:
                            AT[userID][userName] = 1
                    else:
                        AT[userID] = {userName:1}
                    break
                #retweet will always followed by a ":"
                elif text[j+k] == ":":
                    if userID in RT.keys():
                        if userName in RT[userID].keys():
                            RT[userID][userName] = RT[userID][userName] + 1
                        else:
                            RT[userID][userName] = 1
                    else:
                        RT[userID] = {userName:1}
                    break
                k = k + 1
#output the file
f0 = open("RT.txt", "w")
f1 = open("AT.txt", "w")

f0.write(str(RT))
f1.write(str(AT))

f0.close()
f1.close()
    
