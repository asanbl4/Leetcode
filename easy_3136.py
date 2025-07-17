class Solution:
    def isValid(self, word: str) -> bool:
        valid_letters_and_digits = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        vowels = [['a', 'e', 'i', 'o', 'u'], 0]
        consonants = [['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r',
                            's', 't', 'v', 'w', 'x', 'y', 'z'], 0]
        if len(word) < 3:
            return False
        try:
            for i in word:
                if i.lower() not in valid_letters_and_digits:
                    return False
                if i.lower() in vowels[0]:
                    vowels[1] += 1
                elif i.lower() in consonants[0]:
                    consonants[1] += 1
        except Exception:
            return False

        if vowels[1] == 0 or consonants[1] == 0:
            return False

        return True

solution = Solution()
print(solution.isValid("a3$e"))


