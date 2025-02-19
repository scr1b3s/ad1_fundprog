"""
Dada uma string, retorne se ela é uma sequência de DNA, ou seja, para isso, todas as letras devem ser A, C, G ou T. Caso não seja, retorne as posições que os elementos diferem das possíveis letras.

Entrada: Uma string s.
Saída: Se s é uma sequência de DNA, retorne ``sequência válida'', caso contrário, retorne as posições (sendo da posição 1 até a posição do tamanho da string s) que não possuem os valores esperados.
"""

def dna_analysis(s: str) -> str:
    if not s:
        return None
    
    sequence = {'A', 'C', 'G', 'T'}
    invalid_positions = [i + 1 for i, nucleotide in enumerate(s) if nucleotide.upper() not in sequence]
    
    if len(invalid_positions) > 1:
        return f"Sequência inválida, pois nas posições {invalid_positions} os elementos não possuem valores esperados"
    elif len(invalid_positions) == 1:
        return f"Sequência inválida, pois na posição {invalid_positions[0]} o elemento não possui valor esperado"
    else:
        return "Sequência válida"

if __name__ == '__main__':
    entries = dna_analysis('acgctasdagctwqa')
    print(entries)