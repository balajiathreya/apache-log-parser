import random
import unittest
import yapta

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        # no initial setups require. The necessary files are already bundled    
        print "setting up test"

    def test_test1(self):
        print "file in format 1. test1 has one valid user_id. SO COUNT SHOULD BE 1"
        yapta.process_file("test1");
        f = open("test1.out", 'r')
        count = 0;
        for line in f:
            count = count + 1
        print "COUNT: "+str(count)+"\n"
        self.assertEqual(count, 1)

        print "file in format 2. test2 has one valid user_id. SO COUNT SHOULD BE 1"    
        yapta.process_file("test2");
        f = open("test2.out", 'r')
        count = 0;
        for line in f:
            count = count + 1
        print "COUNT: "+str(count)+"\n"
        self.assertEqual(count, 1)

    def test_test2(self):
        print "file in format 1. test3 has entries in incorrect format. For ex - in correct date, missing page and user id. SO COUNT SHOULD BE 0"
        yapta.process_file("test3");
        f = open("test3.out", 'r')
        count = 0;
        for line in f:
            count = count + 1
        print "COUNT: "+str(count)+"\n" 
        self.assertEqual(count, 0)
        print "file in format 2. test4 has entries in incorrect format. For ex - in correct date, missing page and user id. SO COUNT SHOULD BE 0"
        yapta.process_file("test4");
        f = open("test4.out", 'r')
        count = 0;
        for line in f:
            count = count + 1
        print "COUNT: "+str(count)+"\n"
        self.assertEqual(count, 0)
   

if __name__ == '__main__':
    unittest.main()
