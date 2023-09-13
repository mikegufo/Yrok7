def count_vowels(word):
    vowels = "AEIOUaeiou"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

def check_rhythm(poem):
    lines = poem.split()
    syllable_count = count_vowels(lines[0])
    
    for line in lines[1:]:
        if count_vowels(line) != syllable_count:
            return "Пам парам"
    
    return "Парам пам-пам"

poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)