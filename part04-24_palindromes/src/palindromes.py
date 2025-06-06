# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(word:str) -> bool:
    return word == word[::-1]

def main():
    while True:
        word = input('Please type in a palindrome:')
        if palindromes(word):
            print(f'{word} is a palindrome!')
            break
        else:
            print("That wasn't a palindrome")

#if __name__ == '__main__':
#   main()