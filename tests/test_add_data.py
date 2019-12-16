import jsearch.functions as myfunc
import pandas as pd
import unittest

class TestAdd_Data(unittest.TestCase):
    """
    Test the add_data function from the functions library
    """
 
    def test_add_data(self):
        """
        Test that function successfully adds column to output dataframe
        """
        output_pd = pd.DataFrame([['tom', 10]], columns = ['Name', 'Age'])
        input_pd = pd.DataFrame([[21.0, True]], columns = ['Points', 'Active'])

        result = myfunc.add_data(input_pd, output_pd,  "Active", "Active")
        self.assertEqual( len(result.columns), len(input_pd.columns) + 1 )


if __name__ == '__main__':
    unittest.main()