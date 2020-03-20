

f = open("3k0.json", "r")
f0 = open("3k1.json", "w+")
contents = f.readlines()

#for i in range(len(contents)):
    #gg = (contents[i])[:-1]
for i in range(len(contents)):
    if i % 2 == 0:          #because there is always a extra line after each tweets,
        gg = (contents[i])  #and casue error when I import them in MongoDB
    #print (gg)
    #print (type(gg))
    #print (contents)
        f0.write(gg)


f.close()
f0.close()
print ("yess, done")
