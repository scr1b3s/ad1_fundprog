"""
Dada uma sequência de DNA, obtenha seu complemento reverso. Cada base nitrogenada do DNA possui seu complemento, a saber A -> T, T -> A, C -> G, G -> C. Assim, o complemento reverso de uma sequência de DNA s é obtido das seguintes etapas: obtenha a sequência reversa de s, seja s' essa sequência resultante; substitua cada elemento de s' pelo seu complemento.

Entrada: Uma string de DNA s.

Saída: Sequência s e seu reverso complementar, se s for uma sequência de DNA. Caso contrário, retorne que esta é uma sequência inválida.
"""

def dna_analysis(s: str) -> str:
    if not s:
        return None
    
    nucleotides = {'A', 'C', 'G', 'T'}
    s = s.upper()
    not_dna = [l for l in s if l not in nucleotides]

    if not_dna:
        return f"Sequência inválida"
    else:
        reverse = comp_sequence(s)
        return f"Dada a sequência {s}, seu reverso complementar é: {reverse}"

def comp_sequence(dna: str) -> str:
    reverse_comp = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    reversed_dna = dna[::-1]
    return ''.join(reverse_comp[e] for e in reversed_dna)

if __name__ == '__main__':
    print(dna_analysis('acgctagctagc'))