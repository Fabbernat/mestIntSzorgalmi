import unittest
import time
from main import build_tree, max_value, hasznossag
from io import StringIO
from main import main

# StringIO objektum létrehozása a standard output eltereléséhez
class TestMain(unittest.TestCase):

    def test_main_example_input(self):
        # Eltereljük a standard outputot
        with StringIO() as captured_output:
            # Átirányítjuk a standard inputot
            with StringIO("x x x x 3 x 8 x x 6 14 x 5 . . . 12 -7 . . . . 2 . . 4 . . . . . . . . 1") as stdin:
                import sys
                sys.stdin = stdin
                
                main()  
            # Ellenőrizzük a kimenetet
            self.assertIn("A minimális érték: 3\n", captured_output.getvalue())
            self.assertIn("A maximális érték: 8\n", captured_output.getvalue())

    def test_main_3_3_2_1_3_12_8_2_4_6_14_1_5(self):
        with StringIO() as captured_output:
            with StringIO("3 3 2 1 3 12 8 2 4 6 14 1 5 . . . 12 -7 . . . . 2 . . 4 . . . . . . . . 1") as stdin:
                import sys
                sys.stdin = stdin
                main()
            self.assertIn("A minimális érték: 1\n", captured_output.getvalue())
            self.assertIn("A maximális érték: 12\n", captured_output.getvalue())

    def test_main_3_5_6_x_x_1_4(self):
        with StringIO() as captured_output:
            with StringIO("3 5 6 x x 1 4") as stdin:
                import sys
                sys.stdin = stdin
                main()
            self.assertIn("A minimális érték: 1\n", captured_output.getvalue())
            self.assertIn("A maximális érték: 6\n", captured_output.getvalue())

    def test_main_1_2_3_4_5_x_x_x_x_6_7(self):
        with StringIO() as captured_output:
            with StringIO("1 2 3 4 5 x x x x 6 7") as stdin:
                import sys
                sys.stdin = stdin
                main()
            self.assertIn("A minimális érték: 1\n", captured_output.getvalue())
            self.assertIn("A maximális érték: 7\n", captured_output.getvalue())

    def test_main_10_20_x_30_40_50_x_x_x_x_60_70_80(self):
        with StringIO() as captured_output:
            with StringIO("10 20 x 30 40 50 x x x x 60 70 80") as stdin:
                import sys
                sys.stdin = stdin
                main()
            self.assertIn("A minimális érték: 10\n", captured_output.getvalue())
            self.assertIn("A maximális érték: 80\n", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()