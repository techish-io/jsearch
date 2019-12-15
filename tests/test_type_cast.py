import functions as myfunc
import pandas as pd
import unittest

class TestType_Cast(unittest.TestCase):
    """
    Test the type_cast function from the functions library
    """
 
    def test_type_cast_str(self):
        """
        Test the type cast of dataframe colum of type string
        """
        result = myfunc.type_cast(pd.DataFrame([['tom', 10, 21.0, True]], columns = ['Name', 'Age', 'Points', 'Active'])['Name'], "tom")
        self.assertEqual(result, str("tom"))

    def test_type_cast_int(self):
        """
        Test the type cast of dataframe colum of type int
        """
        result = myfunc.type_cast(pd.DataFrame([['tom', 10, 21.0, True]], columns = ['Name', 'Age', 'Points', 'Active'])['Age'], "10")
        self.assertEqual(result, 10)

    def test_type_cast_float(self):
        """
        Test the type cast of dataframe colum of type float
        """
        result = myfunc.type_cast(pd.DataFrame([['tom', 10, 21.0, True]], columns = ['Name', 'Age', 'Points', 'Active'])['Points'],"21.0")
        self.assertEqual(result, 21.0)
    
    def test_type_cast_bool(self):
        """
        Test the type cast of dataframe colum of type bool
        """
        result = myfunc.type_cast(pd.DataFrame([['tom', 10, 21.0, True]], columns = ['Name', 'Age', 'Points', 'Active'])['Active'], True)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()