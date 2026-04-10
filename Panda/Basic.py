import pandas as p

print(f"Hello Sadman I am Panda")

students = {
    "Students" : ['Sadman',"Avi","Sokal","Tamzid"],
    "Dept" : ["CSE","EEE","BBA","ARCH"],
    "grades" : [3.40,3.52,3.65,3.76]
}
std = p.DataFrame(students)

print(std)

data = [23,423,343,567,31,6788,3133]
print("Series : ")
s = p.Series(data)
print(s)

a = [3.40,3.56,3.12,3.6]
indexing = p.Series(a,index=["sadman","Sakib","Nissan","Avi"])
print(indexing)
print(indexing["sadman"])

df = p.read_json('data.json')

print(df.to_string())
