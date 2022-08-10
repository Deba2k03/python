# def function_name_print(a,b,c,d):
#     print(a,b,c,d)
# function_name_print("deb","ruturaj","rahul","shiba","sridhanta")
'''def funargs( *args):
    for item in args:
        print(item)
    # print(type(args))
    # print(args[0])'''


'''
def funagrs(normal,*args,**kwargs):  
    print(normal)
    for item in args:
        print(item)
    print("the celebrity are:")
    for key,value in kwargs.items():
        print(f"{key} is a {value}")
list={"deb","ruturaj","rahul","shiba","sridhanta","the prpgrammer"}
normal1="this is normal argument and students are:"
kw={"deb":"programmer","shiba":"teacher","rutu":"hacker"}
funagrs(normal1,*list,**kw)
'''

# s={"d","e","b","a"}
# for i in s:
#     print(i)

def ss(*a,**x):
    # print(n)
    for i in a:
        print(i)
    for i,c in x.items():
        print(i,c)

n="hey"

v={"a":"b","c":"d"}
s=["d","e","b","a"]
ss(n,*s,**v)