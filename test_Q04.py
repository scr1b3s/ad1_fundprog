import unittest
from Q04 import dna_analysis

class TestDNAAnalysis(unittest.TestCase):
    def test_valid_dna_sequence(self):
        self.assertEqual(dna_analysis(3, "ACGACGTAG"), 6)
        self.assertEqual(dna_analysis(2, "ACGT"), 3)
        self.assertEqual(dna_analysis(1, "ACGT"), 4)
        self.assertEqual(dna_analysis(4, "ACGTACGT"), 4)

    def test_invalid_dna_sequence(self):
        self.assertEqual(dna_analysis(3, "ACGX"), "Sequência inválida")
        self.assertEqual(dna_analysis(2, "1234"), "Sequência inválida")
        self.assertEqual(dna_analysis(1, "ACGTX"), "Sequência inválida")

    def test_empty_sequence(self):
        self.assertIsNone(dna_analysis(3, ""))
        self.assertIsNone(dna_analysis(0, ""))

    def test_zero_k(self):
        self.assertEqual(dna_analysis(0, "ACGT"), 0)
        self.assertEqual(dna_analysis(0, "ACGTACGT"), 0)

if __name__ == "__main__":
    unittest.main()