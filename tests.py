import random
import unittest

from company_share_data import SharePrice

class TestSharePrice(unittest.TestCase):

    def setUp(self):
        self.header = ['Year', 'Month', 'Company-1', 'Company-2', 'Company-3', 'Company-4', 'Company-5']
        self.data = [
                [2013, 'Jan', 123, 31, 199, 257, 61],
                [2013, 'Feb', 124, 32, 198, 255, 62],
                [2013, 'Mar', 125, 33, 197, 253, 63],
                [2013, 'Apr', 126, 34, 196, 251, 71],
                [2013, 'May', 127, 35, 195, 249, 70],
                [2013, 'Jun', 128, 34, 194, 275, 69],
                [2013, 'Jul', 129, 33, 193, 254, 68],
                [2013, 'Aug', 130, 32, 192, 258, 67],
                [2013, 'Sep', 131, 31, 191, 262, 66],
                [2013, 'Oct', 132, 30, 190, 266, 65],
                [2013, 'Nov', 133, 29, 189, 270, 64],
                [2013, 'Dec', 134, 28, 188, 274, 63],
            ]
        self.predicted_result = {'Company-1': '2013-Dec', 'Company-2': '2013-May', 'Company-3': '2013-Jan',
            'Company-4': '2013-Jun', 'Company-5': '2013-Apr'} 

    def test_max_price_share(self):
        # make sure the shuffled data have the same result
        random.shuffle(self.data)
        obj = SharePrice(5,2013)
        obj.header = self.header
        obj.data = self.data
        result = obj.get_max_index()
        self.assertEqual(self.predicted_result, result)


if __name__ == '__main__':
    unittest.main()
