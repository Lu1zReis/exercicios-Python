# map
valores = [1, 2, 3]
factor = [3]
novos_valores = list(map(lambda x, f: x*f, valores, factor*len(valores)))
print(novos_valores)

# ordenando com key
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


# filtrando só os pares
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x%2==0, numbers))
print(even_numbers)
