import unittest
from Q03 import dna_analysis

class TestDNAAnalysis(unittest.TestCase):

    def test_valid_dna_sequence(self):
        self.assertEqual(
            dna_analysis('ACGCTAGCTAGC'),
            'Dada a sequência ACGCTAGCTAGC, seu reverso complementar é: GCTAGCTAGCGT'
        )

    def test_invalid_dna_sequence(self):
        self.assertEqual(
            dna_analysis('ACGTXAGCTAGC'),
            'Sequência inválida'
        )

    def test_empty_sequence(self):
        self.assertIsNone(dna_analysis(''))

    def test_lowercase_dna_sequence(self):
        self.assertEqual(
            dna_analysis('acgctagctagc'),
            'Dada a sequência ACGCTAGCTAGC, seu reverso complementar é: GCTAGCTAGCGT'
        )

    def test_mixed_case_dna_sequence(self):
        self.assertEqual(
            dna_analysis('aCgCtAgCtAgC'),
            'Dada a sequência ACGCTAGCTAGC, seu reverso complementar é: GCTAGCTAGCGT'
        )

if __name__ == '__main__':
    unittest.main()