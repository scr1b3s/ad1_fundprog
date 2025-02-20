import unittest
from Q05 import dna_analysis

class TestDNAAnalysis(unittest.TestCase):

    def test_valid_dna(self):
        self.assertEqual(dna_analysis("ACGACGTAGACG", 3, 2), "ACG\nGAC")
        self.assertEqual(dna_analysis("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", 10, 2), "AAAAACCCCC\nCCCCCAAAAA")
        self.assertEqual(dna_analysis("AAAAAAAAAAAAA", 2, 5), "AA")

    def test_invalid_dna(self):
        self.assertEqual(dna_analysis("ACGTX", 3, 2), "Sequênca inválida")
        self.assertEqual(dna_analysis("12345", 3, 2), "Sequênca inválida")
        self.assertEqual(dna_analysis("ACGTACGTACGT", 3, 2), "ACG\nCGT\nGTA\nTAC")

    def test_empty_string(self):
        self.assertIsNone(dna_analysis("", 3, 2))

    def test_no_repeating_substrings(self):
        self.assertEqual(dna_analysis("ACGT", 2, 2), "")

    def test_edge_cases(self):
        self.assertEqual(dna_analysis("A", 1, 1), "A")
        self.assertEqual(dna_analysis("A", 2, 1), "")
        self.assertEqual(dna_analysis("ACGT", 4, 1), "ACGT")

if __name__ == '__main__':
    unittest.main()