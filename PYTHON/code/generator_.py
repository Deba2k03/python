#iterable=__iter__() or __getitem__()
#iterator=__next__()
#iteration=


def gen(n):
    for i in  range(n):
        yield i

g=gen(3)
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in g:
#     print(i)

h="hello"
# print(h[0])
# # for c in h:
# #     print(c)
ir=iter(h)
print(ir.__next__())
print(ir.__next__())

a=123
# print(iter(a))   #'int' object is not iterable