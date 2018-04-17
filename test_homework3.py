
import unittest
import numpy as np
from homework3 import create_dataframe

def raises_error(*args, **kwds):
    raise ValueError('Invalid value: %s%s' % (args, kwds))
class Homework3Test(unittest.TestCase):

    #unittest setup
    def setUp(self):
        """
        ###!!!Change filepath to appropriate _correct_ filepath containing class.db
        """
        self.filepath = './class.db'
        self.fixture = create_dataframe(self.filepath)

    def test_columns(self):
        df = self.fixture
        cols = df.columns.values
        self.assertIn('video_id', cols)
        self.assertIn('category_id', cols)
        self.assertIn('language', cols)

    def test_length(self):
        df = self.fixture
        self.assertTrue(df.shape[0] >= 10)

    def test_valueError(self):
        bad_args = [None, "blah.db", ""]
        for argv in bad_args:
            try:
                raises_error(create_dataframe(argv))
            except ValueError:
                pass
            else:
                self.fail('Did not see ValueError')



    def testKey(self):
        df = self.fixture
        cols = df.columns.values
        """Assert that no _non-trivial_ combination of columns in the data frame from HW2/3
        is NOT a candidate key for the relation
        """

        self.assertFalse( not np.array(df.groupby(   [cols[0]]   ).agg(['nunique']) >1).any())
        self.assertFalse( not np.array(df.groupby([cols[1]]).agg(['nunique']) >1).any())
        self.assertFalse( not np.array(df.groupby([cols[0], cols[1]]).agg(['nunique']) >1).any())
        self.assertFalse( not np.array(df.groupby([cols[1], cols[0]]).agg(['nunique']) >1).any())

    #unittest teardown 
    def tearDown(self):
        del self.fixture

if __name__ == '__main__':
    unittest.main()
