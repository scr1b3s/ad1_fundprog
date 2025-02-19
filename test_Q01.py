import unittest
from Q01 import dna_analysis

class TestDNAAnalysis(unittest.TestCase):
    def test_AD1_sequences(self):
        self. assertEqual(dna_analysis("acgctasdagctwqa"), "Sequência inválida, pois nas posições [7, 8, 13, 14] os elementos não possuem valores esperados")
        self. assertEqual(dna_analysis("acctctccta"), "Sequência válida")
        self. assertEqual(dna_analysis("sactg"), "Sequência inválida, pois na posição 1 o elemento não possui valor esperado")

    def test_valid_dna_sequence(self):
        self.assertEqual(dna_analysis("ACGTACGT"), "Sequência válida")
    
    def test_invalid_dna_sequence(self):
        self.assertEqual(dna_analysis("ACGTXCGT"), "Sequência inválida, pois na posição 5 o elemento não possui valor esperado")
    
    def test_empty_string(self):
        self.assertIsNone(dna_analysis(''))
    
    def test_all_invalid_characters(self):
        self.assertEqual(dna_analysis("XYZ"), "Sequência inválida, pois nas posições [1, 2, 3] os elementos não possuem valores esperados")
    
    def test_mixed_valid_and_invalid_characters(self):
        self.assertEqual(dna_analysis("ACGTXYZ"), "Sequência inválida, pois nas posições [5, 6, 7] os elementos não possuem valores esperados")
    
    def test_single_valid_character(self):
        self.assertEqual(dna_analysis("A"), "Sequência válida")
    
    def test_single_invalid_character(self):
        self.assertEqual(dna_analysis("X"), "Sequência inválida, pois na posição 1 o elemento não possui valor esperado")

if __name__ == '__main__':
    unittest.main()