import unittest
from Q02 import dna_analysis

class TestDNAAnalysis(unittest.TestCase):
    def AD1_test(self):
        self.assertEqual(
            dna_analysis("acgcacgtca"),
            "Sequência válida. Além disso, a contagem de cada base nitrogenada é: A: 3 C: 4 G: 2 T: 1"
        )
    
    def test_valid_dna_sequence(self):
        self.assertEqual(
            dna_analysis("ACGTACGT"),
            "Sequência válida. Além disso, a contagem de cada base nitrogenada é: A: 2 C: 2 G: 2 T: 2"
        )
    
    def test_invalid_dna_sequence_single_error(self):
        self.assertEqual(
            dna_analysis("ACGTXCGT"),
            "Sequência inválida, pois na posição 5 o elemento não possui valor esperado."
        )
    
    def test_invalid_dna_sequence_multiple_errors(self):
        self.assertEqual(
            dna_analysis("ACGTXCGY"),
            "Sequência inválida, pois nas posições [5, 8] os elementos não possuem valores esperados."
        )
    
    def test_empty_string(self):
        self.assertEqual(
            dna_analysis(""),
            "Sequência válida. Além disso, a contagem de cada base nitrogenada é: "
        )
    
    def test_lowercase_dna_sequence(self):
        self.assertEqual(
            dna_analysis("acgtacgt"),
            "Sequência válida. Além disso, a contagem de cada base nitrogenada é: A: 2 C: 2 G: 2 T: 2"
        )

if __name__ == '__main__':
    unittest.main()