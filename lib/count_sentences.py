#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print('The value must be a string.')

    def is_sentence(self):
        return self.value.strip().endswith('.')

    def is_question(self):
        return self.value.strip().endswith('?')

    def is_exclamation(self):
        return self.value.strip().endswith('!')

    def count_sentences(self):
        value = self.value.strip()
        punctuation_set = {'.', '!', '?'}
        sentences = []
        sentence = ""
        i = 0
        n = len(value)

        while i < n:
            char = value[i]
            sentence += char

            if char in punctuation_set:
                next_char = value[i + 1] if i + 1 < n else None

                while next_char == char:
                    sentence += next_char
                    i += 1
                    next_char = value[i + 1] if i + 1 < n else None
                
                if char == '.' and next_char == '.':
                    while next_char == '.':
                        sentence += next_char
                        i += 1
                        next_char = value[i + 1] if i + 1 < n else None

                if not next_char or next_char not in punctuation_set:
                    sentences.append(sentence.strip())
                    sentence = ""

            i += 1

        if sentence:
            sentences.append(sentence.strip())

        return len(sentences)


string_obj = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
print(string_obj.count_sentences())

simple_string = MyString("one. two. three?")
print(simple_string.count_sentences())

empty_string = MyString()
print(empty_string.count_sentences())