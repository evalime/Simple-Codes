def syllables(texts):
    count = 0

    vowels = ['a','e','i','o','u','y']
    for i in range(0,len(texts)):
        if texts[i] in vowels:
            count += 1
            if i != (len(texts)-1):
                if texts[i+1] in vowels:
                    count -= 1
    if texts[-1] == 'e':
        count -= 1

    if count == 0:
        count = 1
    print(f"It's a {count} syllable word")

if __name__ == "__main__":
    syllables(input("Enter the word:"))