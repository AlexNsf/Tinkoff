import random


class TextGenerator:
    def __init__(self):
        self.word_dict = {}

    @staticmethod
    def delete_symbols(text):
        text = ''.join(char for char in text if char.isalpha() or char in " \n")
        return text

    def add_word(self, key_word, value_word):
        if self.word_dict.get(key_word) is not None:
            self.word_dict[key_word].append(value_word)
        else:
            self.word_dict[key_word] = [value_word]

    def fit(self, text):
        text = self.delete_symbols(text.lower()).split()
        for word_num in range(len(text) - 1):
            self.add_word(text[word_num], text[word_num + 1])
        return text

    def rand_next_word(self, word):
        word_list = self.word_dict[word]
        next_word = word_list[random.randint(0, len(word_list) - 1)]
        return next_word

    def generate(self, length, word=None):
        answer = []
        if word is not None and self.word_dict.get(word) is not None:
            answer.append(word)
        else:
            word, word_list = random.choice(list(self.word_dict.items()))
            answer.append(word)
        for new_word in range(length - 1):
            word = self.rand_next_word(word)
            answer.append(word)
        answer = ' '.join(answer).capitalize() + '.'
        return answer


if __name__ == '__main__':
    text_generator = TextGenerator()
    file_to_read = open("cheh.txt", "r", encoding="utf8")
    file_to_write = open("answer.txt", "w", encoding="utf8")
    text_generator.fit(file_to_read.read())
    print(text_generator.generate(100), file=file_to_write)







