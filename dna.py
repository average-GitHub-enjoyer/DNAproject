# Нуклеотид состоит из букв A, C, G или T. Кодон состоит из трёх таких букв. Ген состоит из кодонов. Похоже, нужно сранивать кодоны в генах.

class Codon:
    def __init__(self, codon_sequence):
        if len(codon_sequence) != 3:
            raise ValueError("Кодон должен иметь ровно 3 нуклеотида!")
        self.codon_sequence = codon_sequence
        # экспериментальная идея ниже: разделять кодон на содержащий тот или иной нуклеотид, чтобы уменьшить время поиска
        # UPD: она мне не нравится

    def __eq__(self, other):
        # переопределение оператора равенства для сравнения кодонов
        is_equal = isinstance(other, Codon) and self.form_aminos() == other.form_aminos()
        return is_equal

    def __ne__(self, other):
        # переопределение оператора неравенства
        return not self.__eq__(other)

    def form_aminos(self):
        # Определение аминокислот, которые формируются кодоном
        genetic_code = {
            "F": ["TTT", "TTC"],
            "L": ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"],
            "I": ["ATT", "ATC", "ATA"],
            "M": ["ATG"],
            "V": ["GTT", "GTC", "GTA", "GTG"],
            "S": ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
            "P": ["CCT", "CCC", "CCA", "CCG"],
            "T": ["ACT", "ACC", "ACA", "ACG"],
            "A": ["GCT", "GCC", "GCA", "GCG"],
            "Y": ["TAT", "TAC"],
            "H": ["CAT", "CAC"],
            "Q": ["CAA", "CAG"],
            "N": ["AAT", "AAC"],
            "K": ["AAA", "AAG"],
            "D": ["GAT", "GAC"],
            "E": ["GAA", "GAG"],
            "C": ["TGT", "TGC"],
            "W": ["TGG"],
            "R": ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
            "G": ["GGT", "GGC", "GGA", "GGG"]
        }


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
            codon_list.append(Codon(codon_sequence))
        return codon_list

    def find_codon(self, given_codon_sequence):
        for i, codon in enumerate(self.codons):
            if codon.codon_sequence == given_codon_sequence:
                return i
        return -1
