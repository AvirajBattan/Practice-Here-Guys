import unittest
from fun import solve

class TestFun(unittest.TestCase):
    
    
    i=1
    #checking for the correct input

    def setUp(self):
        print("==========Running Test Case=========")
        print(" ")
        print(" ")
        

    # def tearDown(self):
        # i+=1
    def test1(self): 
        ans=solve(1,5)
        self.assertEqual(ans,50)

    #checking for--if anyone is given null
    def test2(self):
        ans=solve(5,None)
        self.assertEqual(ans,"Enter Valid value")
    
    #if any value is the string
    def test3(self):
        ans=solve(5,"avi")
        self.assertEqual(ans,"Enter integer")


if __name__=="__main__":
    unittest.main()
    