
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

concatenated_string = str1 + str2
print("Concatenated String: ", concatenated_string)


reversed_string = concatenated_string[::-1]
print("Reversed String: ", reversed_string)


vowels = "aeiouAEIOU"
modified_string = ''.join(['$' if char in vowels else char for char in reversed_string])
print("Modified String (Vowels replaced with $): ", modified_string)


if concatenated_string.startswith(str1):
    print(f"The concatenated string starts with '{str1}'")
else:
    print(f"The concatenated string does not start with '{str1}'")


char_to_count = input("Enter a character to count its occurrences: ")
count = concatenated_string.count(char_to_count)
print(f"The character '{char_to_count}' appears {count} times in the concatenated string.")
