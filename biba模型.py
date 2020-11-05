class subject:
    def __init__(self,integrity,mode=""):
        self.integrity = integrity
        self.mode = mode

    def write(self,object):
        if self.integrity >= object.integrity:
            with open(object.name,"w") as f:
                ss = "new_string"
                f.write(ss)
                print("write success!")

        else:
            print("no right")
        
    
    def execute(self,other):
        if self.integrity <= other.integrity:
            print("execute the other.")
        else:
            print("no right")

    def read(self,object):
        if self.mode == "low-water":
            with open(object.name,"r") as f:
                ss = f.read()
                ss = ss.replace("\n","")
                print "file:",ss
            if self.integrity > object.integrity:
                self.integrity = object.integrity
        
            
        
        if self.mode == "ring":
            with open(object.name,"r"):
                print(f.read())
        
        if self.mode == "strict":
            if self.integrity <= object.integrity:
                with open(object.name,"r"):
                    print(f.read())
            else:
                print("no right")


class object:
    def __init__(self,integrity,name):
        self.integrity = integrity
        self.name = name


x = subject(5,"low-water")
y = subject(2, "low-water")
z = object(3,"test.txt")

print "read:"
x.read(z)
print "subject 1's integrity is",x.integrity,"\n"
y.read(z)
print "subject 1's integrity is",y.integrity,"\n"

print "execute:"
x.execute(y)
y.execute(x)

print "\n","write:"
x.write(z)
y.write(z)




