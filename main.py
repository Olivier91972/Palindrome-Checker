#Verificateur Palindrome

def is_palindrome(word):
  """Vérifie si un mot est un palindrome."""
  return word == word[::-1]

# Exemple d'utilisation :
word = "radar"
if is_palindrome(word):
  print(f"{word} est un palindrome.")
else:
  print(f"{word} n'est pas un palindrome.")