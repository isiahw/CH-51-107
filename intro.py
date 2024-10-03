print("Hello World")
# console.log("Hello world");

# variables
name = "adrian"
age = 38
found = False
name = True
name = 12
# let name = "adrian";
# const name = "adrian";
print(name)

# if/else statement
if age<100:
    print("dnt worry you're not that old")
    # this is on the same level
    # also on the same level
elif age==100:
    print("wow you're a century")
else:
    print("Well seems that you're a little bit old")

#functions
def say_Hello():
    print ("Hello there")
# function say_Hello(){}

# call functions
say_Hello()

print("my age is "+str(age)+" years old")

# array -- list
colors = ["yellow","green","blue"]
print(colors)

# add
colors.append("pink")
print(colors)

# remove using the name
colors.remove("yellow")
print(colors)

# remove using the index
colors.pop(0)
print(colors)

# remove by slice by index
del colors[1]
print(colors)

# for loops
for x in colors:
    print(x)

# for(let i=0;i<colors.length;i++){
# let temp = colors[i];
# console.log(temp)
# }

for x in colors[::2]:
    print (x)

# dictionary
me = {
    "first_name":"Raymond",
    "last_name":"Wiggins"
    "age":38
}

print(me)
print(me["first_name"])
me["first_name"] = "Raymond"
print(me["first_name"])
    
