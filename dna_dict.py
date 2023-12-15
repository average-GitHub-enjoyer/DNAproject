from dna import Codon




class Gene:
    def __init__(self, gene_sequence):
        self.gene_sequence = gene_sequence
        self.codons = self._split_into_codons()
        self.codon_dict = self._create_codon_dict()

    def _create_codon_dict(self):
        codon_dict = {}
        for i in range(0, len(self.gene_sequence) - 2, 3):
            codon_sequence = self.gene_sequence[i:i +3]
            if len(codon_sequence) == 3:
                codon = Codon(codon_sequence)
                codon_dict[codon_sequence] = codon
        return codon_dict

    def find_codon_by_sequance(self, target_sequence):
        return self.codon_dict.get(target_sequence, None)

    def _split_into_codons(self):
        codon_list = []
        gene_len = len(self.gene_sequence)
        for i in range(0, gene_len, 3):
            codon_sequence = self.gene_sequence[i:i + 3]
            if len(codon_sequence) == 3:
                codon_list.append(Codon(codon_sequence))
        return codon_list



