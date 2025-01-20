file_lines=open("Codingal2.txt","r")
count=0
content=file_lines.read()
Colist=content.split("\n")
for i in Colist:
    if i:
        count+=1
print("The number of lines in the file are ",count)