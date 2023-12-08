# Нуклеотид состоит из букв A, C, G или T. Кодон состоит из трёх таких букв. Ген состоит из кодонов. Похоже, нужно сранивать кодоны в генах.

class Codon:
    def __init__(self, codon_sequence, contains_A, contains_C, contains_G, contains_T):
        if len(codon_sequence) != 3:
            raise ValueError("Кодон должен иметь ровно 3 нуклеотида!")
        self.codon_sequence = codon_sequence
        # экспериментальная идея ниже: разделять кодон на содержащий тот или иной нуклеотид, чтобы уменьшить время поиска
        self.contains_A = contains_A
        self.contains_C = contains_C
        self.contains_G = contains_G
        self.contains_T = contains_T
        # что-то типо флагов

class Gene:
    def __init__(self, gene_sequence):
        self.gene_sequence = gene_sequence
        self.codons = self._split_into_codons()

    def _split_into_codons(self):
        codon_list = []
        if len(self.gene_sequence) % 3 == 1:
            self.gene_sequence = self.gene_sequence[:-1]
        elif len(self.gene_sequence) % 3 == 2:  # Обрубаем последние две буквы в нуклеотиде, так как они не образуют кодон и мешают бездумно проходить по циклу. все равно не пригодятся
            self.gene_sequence = self.gene_sequence[:-2]
        for i in range(0, len(self.gene_sequence), 3):
            codon_sequence = self.gene_sequence[i:i + 3]
            contains_A = 'A' in codon_sequence
            contains_C = 'C' in codon_sequence
            contains_G = 'G' in codon_sequence
            contains_T = 'T' in codon_sequence
            codon_list.append(Codon(codon_sequence, contains_A, contains_C, contains_G, contains_T))
        return codon_list

    def find_codon(self, given_codon_sequence):
        for i, codon in enumerate(self.codons):
            if codon.codon_sequence == given_codon_sequence:
                return i
        return -1


gen = Gene("TAGGGAТТAACCGТТATATATATATAGCCATGGATCGAТТATATAGGGAТТAACCGТТATATATATATAGCCATGGATCGAТТATA")
a = gen.find_codon("ATA")
print(a)
