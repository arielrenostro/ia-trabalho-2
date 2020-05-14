# coding: utf-8

import random
import time

from constants import (
    CITIES,
    GENERATIONS_LIMIT,
    MIN_CHALLENGE_SIZE,
    MAX_CHALLENGE_SIZE,
    GENERATION_SIZE,
    MIN_CITIES_DISTANCE,
    MAX_CITIES_DISTANCE,
    AMOUNT_PARENTS_TO_KEEP,
    WAIT_TIME_FOR_NEW_GENERATION, BEST_GENE_GENERATION_LIMIT)
from model import Generation, Gene


def generate_challenge():
    challenge_size = random.randint(MIN_CHALLENGE_SIZE, MAX_CHALLENGE_SIZE)
    challenge = {}

    while len(challenge) < challenge_size:
        city = random.choice(CITIES)
        if city not in challenge:
            challenge[city] = {}

    for city in challenge:
        adjacencies = challenge[city]

        for another_city in challenge:
            if another_city != city and another_city not in adjacencies:
                distance = random.randint(MIN_CITIES_DISTANCE, MAX_CITIES_DISTANCE)

                adjacencies[another_city] = distance
                challenge[another_city][city] = distance

    return challenge


def init_generation(challenge):
    genes = []
    for i in range(GENERATION_SIZE):
        gene_code = [*challenge.keys()]
        random.shuffle(gene_code)
        gene = Gene(gene_code)
        genes.append(gene)
    return Generation(genes)


def print_challenge(challenge):
    print(' Problema gerado: ')
    for city in challenge:
        print(f'   {city}:')

        adjacencies = challenge[city]
        for adjacency in adjacencies:
            print(f'     {adjacency}: {adjacencies[adjacency]}')
            # print(f'   {city} <---> {adjacency}: {adjacencies[adjacency]}')

        print('')


def print_generation(i, generation):
    print('')
    print(f' Geração {i} - Fitness {generation.fitness}')
    print(f'   Melhor gene: Fitness: {generation.best_gene.fitness} - {" -> ".join(generation.best_gene.gene_code)} -> {generation.best_gene.gene_code[0]}')

    for i in range(len(generation.genes)):
        gene = generation.genes[i]
        print(f'   {i}: Fitness: {gene.fitness} - {" -> ".join(gene.gene_code)} -> {gene.gene_code[0]}')


def avaliate_generation(generation, challenge):
    for gene in generation.genes:
        first_city = None
        last_city = None
        for city in gene.gene_code:
            if not first_city:
                first_city = last_city = city
                continue
            gene.fitness += challenge[city][last_city]
            last_city = city
        gene.fitness += challenge[first_city][last_city]

    generation.update()


def select_parents(generation):
    size = generation.size
    new_genes = generation.genes[0:AMOUNT_PARENTS_TO_KEEP]

    idx_parent = 0
    for _ in range(size - AMOUNT_PARENTS_TO_KEEP):
        gene = new_genes[idx_parent]
        new_genes.append(
            gene.clone()
        )
        idx_parent += 1
        if idx_parent == AMOUNT_PARENTS_TO_KEEP:
            idx_parent = 0

    generation.genes = new_genes


def move_chromo(gene, idx_a, idx_b):
    aux = gene[idx_a]
    gene[idx_a] = gene[idx_b]
    gene[idx_b] = aux


def crossover_parents(cut_idx, parent_a, parent_b):
    new_gene_code = [*parent_a.gene_code]
    for i in range(cut_idx, len(parent_a.gene_code)):
        chromo_b = parent_b.gene_code[i]
        idx_chromo_b_in_a = new_gene_code.index(chromo_b)
        move_chromo(new_gene_code, idx_chromo_b_in_a, i)
    return new_gene_code


def crossover(generation):
    for idx_gen in range(0, generation.size, 2):
        parent_a = generation.genes[idx_gen]
        parent_b = generation.genes[idx_gen + 1]

        cut_idx = random.randint(1, len(parent_a.gene_code) - 1)

        new_parent_a_gene_code = crossover_parents(cut_idx, parent_a, parent_b)
        new_parent_b_gene_code = crossover_parents(cut_idx, parent_b, parent_a)

        parent_a.gene_code = new_parent_a_gene_code
        parent_b.gene_code = new_parent_b_gene_code


def mutation(generation):
    for i in range(generation.size):
        gene = generation.genes[i]
        if (random.random() < (1 / len(gene.gene_code))) or i >= AMOUNT_PARENTS_TO_KEEP:
            idx_a = random.randint(0, len(gene.gene_code) - 1)
            idx_b = random.randint(0, len(gene.gene_code) - 1)
            move_chromo(gene.gene_code, idx_a, idx_b)


def reset_fitness(generation):
    for gene in generation.genes:
        gene.fitness = 0


def change_generation(generation):
    reset_fitness(generation)
    select_parents(generation)
    crossover(generation)
    mutation(generation)


def analyse(best_gene, best_gene_generation, generation, i):
    if not best_gene or (best_gene and best_gene.fitness > generation.best_gene.fitness):
        return generation.best_gene, i, False

    return best_gene, best_gene_generation, (i - best_gene_generation) > BEST_GENE_GENERATION_LIMIT


def main():
    print('----------------------------------------------------')
    print(' FURB 2020/01')
    print(' IA - Trabalho 2 - Questão 2')
    print(' Ariel, Bruno Gabriel Curbani, Gabriel Lepkoski')
    print('----------------------------------------------------')
    print(' Implemente uma solução para o problema do caixeiro ')
    print(' viajante utilizando AG considerando um número ')
    print(' mínimo de 10 cidades. ')
    print(' Mostre as interações realizadas até alcançar ')
    print(' a resolução.')
    print('----------------------------------------------------')

    challenge = generate_challenge()
    print_challenge(challenge)

    input(' Pressione ENTER para continuar ')

    print(' Gerando a primeira geração...')
    generation = init_generation(challenge)

    best_gene = None
    best_gene_generation = -1
    for i in range(1, GENERATIONS_LIMIT):
        avaliate_generation(generation, challenge)
        print_generation(i, generation)

        best_gene, best_gene_generation, stop = analyse(best_gene, best_gene_generation, generation, i)
        if stop:
            break

        time.sleep(WAIT_TIME_FOR_NEW_GENERATION)
        change_generation(generation)

    print(' O melhor gene para o problema é: ')
    print(f' Fitness: {best_gene.fitness} - {" -> ".join(best_gene.gene_code)} -> {best_gene.gene_code[0]}')


if __name__ == '__main__':
    main()
