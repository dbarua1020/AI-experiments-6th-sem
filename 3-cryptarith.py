import itertools

def is_valid_solution(letters, word1, word2, result, permutation):
    # Convert letters to digits based on the current solution
    letter_to_digit = {letter: digit for letter, digit in zip(letters, permutation)}
    
    # Convert words to their corresponding integer values
    int_word1 = int(''.join(str(letter_to_digit[letter]) for letter in word1))
    int_word2 = int(''.join(str(letter_to_digit[letter]) for letter in word2))
    int_result = int(''.join(str(letter_to_digit[letter]) for letter in result))
    
    # Check if the current solution is valid
    return int_word1 + int_word2 == int_result

def solve_crypt_arithmetic(word1, word2, result):
    # Get unique letters from all words
    letters = set(word1 + word2 + result)
    
    # Generate all possible permutations of digits from 0 to 9
    permutations = itertools.permutations(range(10), len(letters))
    
    # Try each permutation to find a valid solution
    for permutation in permutations:
        if is_valid_solution(letters, word1, word2, result, permutation):
            return {letter: digit for letter, digit in zip(letters, permutation)}
    
    return None

# Example usage
word1 = 'BASE'
word2 = 'BALL'
result = 'GAMES'
solution = solve_crypt_arithmetic(word1, word2, result)

if solution:
    print("Valid solution found:")
    for letter, digit in solution.items():
        print(f"{letter}: {digit}")
else:
    print("No valid solution found.")
