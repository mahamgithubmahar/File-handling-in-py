file_read=open('Codingal.txt','r')
print(file_read.read())
file_read.close()

file_write=open("Codingal.txt","w")
file_write.write("\n Hi, my name is Maham")
file_write.close()

file_append=open("Codingal.txt","a")
file_append.write("\n Hi, my name is Priyanka")
file_append.close()