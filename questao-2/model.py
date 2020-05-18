from typing import List


class Gene:
    gene_code: List[str]
    fitness: int

    def __init__(self, gene_code: List[str], fitness=0):
        self.gene_code = gene_code
        self.fitness = fitness

    @property
    def gene_size(self):
        return len(self.gene_code)

    def clone(self):
        return Gene([*self.gene_code], self.fitness)


class Generation:
    _fitness = 0
    _best_gene = None
    genes = []

    def __init__(self, genes):
        self.genes = genes

    @property
    def size(self) -> int:
        return len(self.genes)

    @property
    def best_gene(self) -> Gene:
        return self._best_gene

    @property
    def fitness(self):
        return self._fitness

    def update(self):
        self.genes.sort(key=lambda gene: gene.fitness)
        self._fitness = sum(gene.fitness for gene in self.genes)
        self._best_gene = self.genes[0] if len(self.genes) > 0 else None  # the first element is the best gene
