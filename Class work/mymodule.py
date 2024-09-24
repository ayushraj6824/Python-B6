PI=3.14
def myadd(a,b):
    return a+b

def mydiff(a,b):
    return a-b


if __name__ =="__main__":
    print("executed as main file")
    a=1
    b=2
    print(f"addition of{a} and {b} ={myadd(a,b)}")

else:
    print("imported as module")