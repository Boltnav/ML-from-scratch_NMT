import random

def create_bilingual_variations(english, kannada, num_variations=2):
    eng_words = english.split()
    kan_words = kannada.split()
    eng_length = len(eng_words)
    kan_length = len(kan_words)
    variations = []
    
    for _ in range(num_variations):
        # Creating variations for English
        eng_random_index = random.randint(0, eng_length - 1)
        new_eng = ' '.join(eng_words[:eng_random_index] + [random.choice(eng_words)] + eng_words[eng_random_index + 1:])
        
        # Creating variations for Kannada
        kan_random_index = random.randint(0, kan_length - 1)
        new_kan = ' '.join(kan_words[:kan_random_index] + [random.choice(kan_words)] + kan_words[kan_random_index + 1:])
        
        variations.append((new_eng, new_kan))
    
    return variations

# Load the original data from a file
with open('train.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()

# Generate bilingual variations for each sentence pair in the dataset
bilingual_variations_set_1 = []
bilingual_variations_set_2 = []

for line in data:
    english, kannada = line.strip().split('\t')[:2]
    variations = create_bilingual_variations(english, kannada)
    bilingual_variations_set_1.append(variations[0])
    bilingual_variations_set_2.append(variations[1])

# Save the complete sets to two new text files
with open('variations_set_11111.txt', 'w', encoding='utf-8') as file1, open('variations_set_211111.txt', 'w', encoding='utf-8') as file2:
    for (eng1, kan1), (eng2, kan2) in zip(bilingual_variations_set_1, bilingual_variations_set_2):
        file1.write(f"{eng1}\t{kan1}\n")
        file2.write(f"{eng2}\t{kan2}\n")
