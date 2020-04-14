word = ["t", "i", "g", "e", "r"]
win = ["[t]", "[i]", "[g]", "[e]", "[r]"]
number = 0

while True:
    guess = input()
    A = [i for i in guess]
    number += 1
    if A == word:
        print("".join(win))
        if number == 1:
            print("You win! You took 1 guess!")
            break
        else:
            print("You win! You took {0} guesses!".format(number))
            break
    for i in range(0, 5):
        if guess[i] in word and word[i] == A[i]:
            A[i] = ("[{0}]".format(A[i]))
        elif guess[i] in word and word[i] != A[i]:
            A[i] = ("({0})".format(A[i]))
    print("".join(A))
