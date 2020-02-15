# 299. Bulls and Cows

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        secret_list = [int(x) for x in str(secret)]
        guess_list = [int(x) for x in str(guess)]
        for i in range(0, len(str(secret))):
            if secret_list[i] == guess_list[i]:
                bull += 1
                secret_list[i] = -1
                guess_list[i] = -1

        for i in range(0, len(str(secret))):
            if guess_list[i] == -1:
                continue
            else:
                if guess_list[i] in secret_list:
                    secret_list[secret_list.index(guess_list[i])] = -1
                    cow += 1

        return str(bull) + "A" + str(cow) + "B"
