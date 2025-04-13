
sentence = "Python is awesome"
vowel = ["a","e","i","o","u"]
vowel_count = 0
for word in vowel:
    vowel_count += sentence.count(word)

print(f"모음 개수:{vowel_count}")