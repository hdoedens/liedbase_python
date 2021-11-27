import unittest

import helpers

class TestHelpers(unittest.TestCase):
    
    def test_validate_line_lied(self):
        line = "psalm 1: 1,3"
        result = helpers.validate_line(line)
        self.assertEqual(result, True)
        
        line = "psalm 1: 1,3a"
        result = helpers.validate_line(line)
        self.assertEqual(result, False)
        
        line = "psal m 1: 1,3"
        result = helpers.validate_line(line)
        self.assertEqual(result, False)
        
        line = "psal m 1: 13"
        result = helpers.validate_line(line)
        self.assertEqual(result, False)
        
        line = "gezang 14: 1"
        result = helpers.validate_line(line)
        self.assertEqual(result, True)
    
    def test_validate_line_bijbel(self):
        line = "exodus 1: 13-26"
        result = helpers.validate_line(line)
        self.assertEqual(result, True)
        
        line = "exodus 1: 16"
        result = helpers.validate_line(line)
        self.assertEqual(result, False)
        
        line = "1 johannes 1: 1-6"
        result = helpers.validate_line(line)
        self.assertEqual(result, True)
        
        line = "1johannes 1: 1-6"
        result = helpers.validate_line(line)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()