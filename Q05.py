"""
Dada uma sequência de DNA válida (contendo apenas A, C, G e T), escreva um programa que encontre todas as substrings de tamanho k que aparecem ao menos n vezes. Caso a sequência não seja válida, retorne "Sequência inválida".

Entrada: Dois inteiros k e n, seguidos de uma string s representando a sequência de DNA.

Saída: Liste todas as substrings de tamanho k que aparecem ao menos n vezes, uma por linha, ou a mensagem "Sequência inválida".
"""

def dna_analysis(s: str, k: int = 0, n: int = 0) -> str | None:
    if not s:
        return None
    
    nucleotides = {'A', 'C', 'G', 'T'}
    s = s.upper()
    not_dna = [l for l in s if l not in nucleotides]

    if not_dna:
        return "Sequênca inválida"
    else:
        return find_subs(s, k, n)

def find_subs(s: str, k: int = 0, n: int = 0) -> str | None:
    substrings = {}
    for i in range(len(s) - k + 1):
        sub = s[i : i + k]
        substrings[sub] = substrings.get(sub, 0) + 1
    
    result = []
    for k, v in substrings.items():
        if v >= n:
            result.append(k)

    return '\n'.join(result)

if __name__ == '__main__':
    print(dna_analysis("ACGACGTAGACG", 3, 2))