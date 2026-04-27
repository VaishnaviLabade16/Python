def word_count(text):
    words = text.lower().split()
    freq = {}
    
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    return freq

print(word_count("data analyst data science data"))