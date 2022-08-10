# import time

# def work(n):
#     #task taking 1 secornd
#     time.sleep(n)
#     return n
# if __name__=='__main__':
#     print("now running work")
#     work(3)
#     print("done....calling again")
#     work(3)
#     print("called again")


import time
from functools import lru_cache

@lru_cache(maxsize=3)
def work(n):
    #task taking 1 secornd
    time.sleep(n)
    return n
if __name__=='__main__':
    print("now running work")
    work(3)
    print("done....calling again")
    work(3)
    print("called again")
    work(3)
    print("called again")
    work(4)
    print("called again")
    work(4)
    print("called again")
    work(5)
    print("called again")
    