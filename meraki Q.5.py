my_file=open("delhi.txt","x")
my_file=open("shimla.txt","x")
my_file=open("others.txt","x")
my_file=open("question3.txt","r")
for i in my_file:

    if "delhi" in my_file[i]:
        f=open("delhi.txt","a")
        f.write(my_file[i])
    elif "shimla" in my_file[i]:
        g=open("shimla.txt","a")
        g.write(my_file[i]) 
    else:
        n=open("others.txt","a")
        n.write(my_file[i])
