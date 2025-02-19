"""
Dada uma string, retorne se ela é uma sequência de DNA. Caso não seja, retorne as posições que os elementos diferem das possíveis letras. Caso seja, retorne dizendo que ela é uma sequência de DNA juntamente com a quantidade de cada uma das possíveis letras A, C, G, T.

Entrada: Uma string s.

Saída: Se s é uma sequência de DNA, retorne "sequência válida", juntamente com a quantidade de cada uma das possíveis letras A, C, G, T, caso contrário, retorne as posições (sendo da posição 1 até a posição do tamanho da string s) que não possuem os valores esperados.
"""

def dna_analysis(s: str) -> str:
    if not s:
        return None
    
    sequence = {'A', 'C', 'G', 'T'}
    not_dna = [i + 1 for i, l in enumerate(s) if l.upper() not in sequence]
    
    if not_dna:
        if len(not_dna) > 1:
            return f"Sequência inválida, pois nas posições {not_dna} os elementos não possuem valores esperados"
        elif len(not_dna) == 1:
            return f"Sequência inválida, pois na posição {not_dna[0]} o elemento não possui valor esperado"
    else:
        dna_obj = {}
        s = s.upper()

        for l in s:
            dna_obj[l] = dna_obj.get(l, 0) + 1
        
        dna_obj = dict_to_string(dna_obj)
        return f"Sequência válida. Além disso, a contagem de cada base nitrogenada é: {dna_obj.strip()}"

def dict_to_string(d: dict) -> str:
    return ' '.join(f"{k}: {v}" for k,v in d.items())
        
if __name__ == '__main__':
    data = dna_analysis("acgcacgtca")
    print(data)