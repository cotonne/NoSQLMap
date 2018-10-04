import unittest

import nsmweb


class NsWebMethods(unittest.TestCase):

    def test_build_report(self):
        report = nsmweb.build_report(True, ['127.0.0.1'], True, ['127.0.0.1'])
        self.assertEqual(report, 'Vulnerable URLs:\n127.0.0.1\n\nPossibly Vulnerable URLs:\n127.0.0.1\nTiming based '
                                 'attacks:\nString Attack-Successful\n\nInteger attack-Successful\n\n')

    def test_build_report_with_unsuccessful_attacks(self):
        report = nsmweb.build_report(False, ['127.0.0.1'], False, ['127.0.0.1'])
        self.assertEqual(report, 'Vulnerable URLs:\n127.0.0.1\n\nPossibly Vulnerable URLs:\n127.0.0.1\nTiming based '
                                 'attacks:\nString Attack-Unsuccessful\n\nInteger attack-Unsuccessful\n\n')


if __name__ == '__main__':
    unittest.main()
