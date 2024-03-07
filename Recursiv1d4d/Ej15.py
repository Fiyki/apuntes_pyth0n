class Palindromo:
    def palindromo(self, s, i, j):
        if i == j:
            return True
        else:
            if s[i] == s[j]:
                return self.palindromo(s, i + 1, j - 1)
            else:
                return False


p = Palindromo()
s = "anitalavalatina"
print(p.palindromo(s, 0, len(s) - 1))