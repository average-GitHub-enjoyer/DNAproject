import random
import timeit
import functools
import matplotlib.pyplot as plt
from dna_optimized import Gene


@functools.lru_cache(maxsize=None)
def timing_decorator(ndigits: int, number: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> float:
            usage_time = timeit.timeit(
                lambda: func(*args, **kwargs),
                number=number,
            )
            return round(usage_time / number, ndigits)

        return wrapper

    return decorator


# Функция генерации случайной генетической последовательности длиной n
def generate_random_gene_sequence(n):
    gene_sequence = ''.join(random.choice(['T', 'A', 'C']) for _ in range(n - 3))

    # Добавление "TAG" в конец последовательности
    gene_sequence += "TAG"

    return gene_sequence


# Функция для измерения времени выполнения поиска кодона в гене
@timing_decorator(6, 5)
def calculate_gene_search_time(gene, target_codon):
    gene.find_codon(target_codon)


n_values = [1000002, 2000001, 10000002, 50000001]
average_times_gene_search = []

for n in n_values:
    print(f"Generating gene with {n} characters...")

    # Генерация случайной генетической последовательности
    gene_sequence = generate_random_gene_sequence(n)

    # Создание экземпляра класса Gene с сгенерированной последовательностью
    gen = Gene(gene_sequence)

    print(f"Calculating search time for TAG in a gene with {n} characters...")

    # Измерение времени выполнения поиска кодона "TAG"
    average_time = calculate_gene_search_time(gen, "TAG")
    average_times_gene_search.append(average_time)

# Построение графика зависимости времени от количества символов в гене
plt.plot(n_values, average_times_gene_search, linestyle='-', color='r')
plt.title('Зависимость времени поиска кодона "TAG" от длины гена')
plt.xlabel('Длина гена')
plt.ylabel('Среднее время выполнения (секунды)')

plt.savefig('gene_optimized_search_time.png')


