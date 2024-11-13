# PROBLEM-5: find the vowels in text
def find_vowels (text):
    vowels = 'aeiouAEIOU'
    vowels_found = []

    for vowel in text:
        if vowel in vowels:
            vowels_found.append(vowel)
    return vowels_found

vowels_in_text = find_vowels(input('Enter a String: '))
print('Vowels: ', vowels_in_text)