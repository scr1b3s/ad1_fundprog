"""
Dada uma sequência de DNA válida (contendo apenas A, C, G e T), escreva um programa que conte o número de substrings distintas de tamanho k na sequência. Caso a sequência não seja válida, retorne 'Sequência inválida'.

Entrada: Um inteiro k e uma string s representando uma sequência de DNA.

Saída: O número de substrings distintas de tamanho k, ou a mensagem de sequência inválida se s não for uma sequência de DNA.
"""

def dna_analysis(k: int, s: str) -> str | int:
    if not s:
        return None
    
    nucleotides = {'A', 'C', 'G', 'T'}
    s = s.upper()
    not_dna = [l for l in s if l not in nucleotides]

    if not_dna:
        return f"Sequência inválida"
    else:
        return find_subs(s, k) if k > 0 else 0

def find_subs(s: str, k: int = 0) -> int:
    substrings = set()
    for i in range(len(s) - k + 1):
        sub = s[i : i + k]
        substrings.add(sub)
        
    return len(substrings)

if __name__ == "__main__":
    print(dna_analysis(4, "ACGTACGT"))