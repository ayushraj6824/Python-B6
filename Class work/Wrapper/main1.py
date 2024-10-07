# write a fn to evaluate expression "res = i * 10" for all values between 0 to n,function is taking one input argument "n"
#
import time

nList = [123213,234,33223423,23444444,10000000]
# n = 10000000
def testfn(n):
    for i in range(0,n):
        res = i * 10



for n in nList:
    start_time = time.time() * 1000 #recording timein milli sec
    #execute function
    testfn(n)

    end_time = time.time() * 1000
    diff = end_time - start_time

    print(f"execution time for n = {n} is \n {diff} milli sec")