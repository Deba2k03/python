f1=open("file_x.txt")
try:
    # f=open("does.txt")
    pass
except Exception as e:
    print(e)
else:
    print("it is run only exception is not runing")
finally:  #used to cleanup-
    print("run this any way")
    # f.close()
    f1.close()

print("important stuff")