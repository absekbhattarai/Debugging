import unittest


def area(l, b):
    if not l or not b:
        raise Exception('A side is not given')
    if type(l) != (int or float):
        raise Exception('Length is not a number')
    if type(b) != (int or float):
        raise Exception('Breadth is not a number')
    if l < 0 or b < 0:
        raise Exception('Dimension cannot be negative')
    return 2 * (l + b)


class MyTestCase(unittest.TestCase):
    def test_case_no_side_given(self):
        with self.assertRaises(Exception) as context_b:
            area(2, None)

        with self.assertRaises(Exception) as context_l:
            area(None, 2)
        self.assertTrue('A side is not given' == context_b.exception.args[0])
        self.assertTrue('A side is not given' == context_l.exception.args[0])

    def test_case_length_num(self):
        with self.assertRaises(Exception) as context:
            area("sa", 2)

        self.assertTrue('Length is not a number' in context.exception.args[0])

    def test_case_breadth_num(self):
        with self.assertRaises(Exception) as context:
            area(2, "sa")

        self.assertTrue('Breadth is not a number' in context.exception.args[0])

    def test_case_neg_dim(self):
        with self.assertRaises(Exception) as context_b:
            area(2, -1)

        with self.assertRaises(Exception) as context_l:
            area(-7, 2)

        self.assertTrue('Dimension cannot be negative' in context_b.exception.args[0])
        self.assertTrue('Dimension cannot be negative' in context_l.exception.args[0])

    def test_case_find_area(self):
        get_area = area(2, 3)
        self.assertEqual(get_area, 10)


if __name__ == '__main__':
    unittest.main()
