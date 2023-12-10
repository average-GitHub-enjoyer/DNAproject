class Codon:
    def __init__(self, codon_sequence, index=None):
        if len(codon_sequence) != 3:
            raise ValueError("Кодон должен иметь ровно 3 нуклеотида!")
        self.codon_sequence = codon_sequence
        self.index = index

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
        self.codons_T, self.codons_A, self.codons_G, self.codons_C = self._split_into_codons()

    def _split_into_codons(self):
        codon_list_T = []
        codon_list_A = []
        codon_list_G = []
        codon_list_C = []
        codon_index = 0
        if len(self.gene_sequence) % 3 == 1:
            self.gene_sequence = self.gene_sequence[:-1]
        elif len(self.gene_sequence) % 3 == 2:  # Обрубаем последние две буквы в нуклеотиде, так как они не образуют кодон и мешают бездумно проходить по циклу. все равно не пригодятся
            self.gene_sequence = self.gene_sequence[:-2]
        for i in range(0, len(self.gene_sequence), 3):
            codon_sequence = self.gene_sequence[i:i + 3]
            if "T" in codon_sequence:
                codon_list_T.append(Codon(codon_sequence, codon_index))
            if "A" in codon_sequence:
                codon_list_A.append(Codon(codon_sequence, codon_index))
            if "G" in codon_sequence:
                codon_list_G.append(Codon(codon_sequence, codon_index))
            if "C" in codon_sequence:
                codon_list_C.append(Codon(codon_sequence, codon_index))
            codon_index += 1
        return codon_list_T, codon_list_A, codon_list_G, codon_list_C

    def find_codon(self, given_codon_sequence):
        nucleotides = set(given_codon_sequence)
        min_length = float('inf')  # Изначально устанавливаем минимальную длину как бесконечность
        selected_codons = None

        for nucleotide in nucleotides:
            codon_list = getattr(self, f"codons_{nucleotide}", [])  # Получаем список кодонов для данного нуклеотида
            if codon_list and len(codon_list) < min_length:
                min_length = len(codon_list)
                selected_codons = codon_list

        if selected_codons:
            for codon in selected_codons:
                if given_codon_sequence == codon.codon_sequence:
                    return codon.index

        # Возвращаем None, если кодон не найден
        return None


codon1 = Codon("CGT")
codon2 = Codon("AGA")

print(codon1 == codon2)