d2={"deb":"cs","netra":"math","pratap":"botany","ruturaj":"mth"}
print("Enter name:")
n=input()
if n in d2:
    print(f"{n}, your  subject is {d2[n]}")
else:
    print("invalid name")
