#练习(参考书籍《Python编程:从入门到实践》)
#hello world!
print("Hello,Python world!")
a="Hello,Python world!"
print(a)
b="hello,Python world!"
print(b.title())
c="Hello"
d="Python world"
e=c+","+d+"!"
print(e)
#列表,for循环,if语句
f=["miny","caorizhou"]
print(f)
print(f[0].title())
print(f[1].title())
print(f[-1].title())
f.append("hhh")
print(f)
print(f[-1].title())
del f[-1]
print(f)
for people in f:
    print("Hello!"+people.title()+"!")
print("Thank you!")
for g in range(1,100):
    print(g)
h=["miny","caorizhou","hhh"]
for i in h:
    if i == "hhh":
        print("hhh!")
    else:
        print("Hello!"+i.title()+"!")
j=["a","b","c","d","e"]
if "a" in j:
    print("Hello!"+j[0]+"!")
for k in j:
    if "a" == j:
        print("Hello!a!")
    if "a" != j:
        print("Hello!"+k+"!")
age=13
if age <= 4:
    print("Hello!")
elif age <= 18:
    print("Hey!")
else:
    print("Hi!")
#字典
cats={"rn":"gary","ns":"blue"}
print(cats["rn"])
print(cats["ns"])
for abcde in range(0,1000000):
    print(abcde)
