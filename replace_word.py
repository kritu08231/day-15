#WAF that replace all occurrences of "java" with "python" in above file.
with open("practise.txt","r")as  f:
    data=f.read()
    
new_data=data.replace("Java","Python")
print(new_data)

with open("practise.txt","w")as  f:
    f.write(new_data)
