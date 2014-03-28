import random
import unittest

from company_share_data import SharePrice

class TestSharePrice(unittest.TestCase):
    """
        UnitTest case for SharePrice
    """
    def setUp(self):
        #given test sample data file
        self.file_name = 'sample_test_data.csv'

        #expected result from given csv file
        self.predicted_result = {'Company-1': '2012-May',
                                 'Company-2': '2013-Dec',
                                 'Company-3': '2007-May',
                                 'Company-4': '1995-Oct, 1997-Dec',
                                 'Company-5': '2011-Dec',
                                 'Company-6': '1998-Nov',
                                 'Company-7': '1996-Dec',
                                 'Company-8': '2000-Oct',
                                 'Company-9': '1995-Nov',
                                 'Company-10': '2010-Dec'}

    def test_max_price_share(self):
        #print "\nExpected result : %s" %(self.predicted_result)
        #parse data from the given test file
        obj = SharePrice()
        obj.read_from_csv(self.file_name)
        result = obj.get_max_index()
        #compare with the calculated result
        self.assertEqual(self.predicted_result, result)


if __name__ == '__main__':
    unittest.main()
