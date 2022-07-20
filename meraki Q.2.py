
my_file = open("people1-exercise.txt","w")
file_data = my_file.write("Rishabh - meerut\n"
"imtiyaz - delhi\n"
"nilima - cochin\n"
"rati - shimla\n"
"ayishah - delhi\n"
"raghu - shimla\n"
"naseer - kanpur\n"
"karthikeyan - delhi\n"
"salma - jaipur\n"
"pankaj - delhi\n"
"brijesh - delhi\n"
"govind - delhi\n"
"puneet - shimla\n"
"siddhi - delhi\n"
"suman - jaipur\n"
"rajeev - shimla\n"
"mohinder- delhi\n"
"rajendra - jaipur\n"
"priyanka - shimla\n"
"neela - delhi\n"
"sashi - jaipur\n"
"sarika - delhi\n"
"deepti - shimla\n"
"harshad - delhi\n"
"trishna - raipur\n"
"pradeep - jaipur\n"
"sekhar - delhi\n")
my_file.close()


file=open("people1-exercise.txt",'r')
count=0
for item in file:
    count+=1
print("my_file count is",count)

