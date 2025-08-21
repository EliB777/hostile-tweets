class min_word:
    def get_min_word(self, text):
        words = text.split()
        min_word = {}
        for word in words:
            min_word[word] = min_word.get(word, 0) + 1
        min_word = min(min_word, key=min_word.get) if min_word else None
        return min_word