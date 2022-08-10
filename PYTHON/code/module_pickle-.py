import pickle

#pickling a python object
# cars=["bmw","farari","rr","duke"]
# file="mycars.pkl"
# with open("mycars.pkl","wb") as fileobj:
#     pickle.dump(cars,fileobj)

file="mycars.pkl"
fileobj=open("mycars.pkl","rb")
mycar = pickle.load(fileobj)
print(mycar )

# pickel.loads=?