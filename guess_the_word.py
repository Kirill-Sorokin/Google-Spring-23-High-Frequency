from random import choice

# This is Master's API interface.
# You should not implement it, or speculate about its implementation
class Master:
    def guess(self, word: str) -> int:
        pass

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def match(w1: str, w2: str) -> int:
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        for _ in range(10):
            guess_word = choice(words)
            matching = master.guess(guess_word)
            words = [w for w in words if match(w, guess_word) == matching]
