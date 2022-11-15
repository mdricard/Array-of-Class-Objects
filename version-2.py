#https://stackoverflow.com/questions/28260443/create-an-array-of-objects-in-python
class TestDat():
    def __init__(self, Dat1, Dat2):
        self.Dat1 = Dat1
        self.Dat2 = Dat2

TestArray = [TestDat(0,1),
             TestDat(3,4)]

print (TestArray[0].Dat1) # this is Test1
print (TestArray[1].Dat1) # this is Test2
