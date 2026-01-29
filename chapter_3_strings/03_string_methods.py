"""
========================================
COMMON STRING METHODS
========================================

Python has many built-in string methods for common operations.
"""

# =============================================================================
# CASE METHODS
# =============================================================================

print("=== Case Methods ===")

text = "Hello World"

# Convert cases
print(f"Original: '{text}'")
print(f"Upper: '{text.upper()}'")
print(f"Lower: '{text.lower()}'")
print(f"Title: '{text.title()}'")
print(f"Capitalize: '{text.capitalize()}'")
print(f"Swapcase: '{text.swapcase()}'")

print("\n" + "="*50 + "\n")

# =============================================================================
# SEARCH AND FIND METHODS
# =============================================================================

print("=== Search and Find Methods ===")

sentence = "Python is awesome. Python is fun."

# Find positions
print(f"Original: '{sentence}'")
print(f"Find 'Python': {sentence.find('Python')}")      # First occurrence
print(f"Find 'is': {sentence.find('is')}")              # First occurrence
print(f"Find 'Java': {sentence.find('Java')}")          # Not found (-1)

# Count occurrences
print(f"Count 'Python': {sentence.count('Python')}")
print(f"Count 'is': {sentence.count('is')}")
print(f"Count 'a': {sentence.count('a')}")

# Check if string contains substring
print(f"Contains 'Python': {'Python' in sentence}")
print(f"Contains 'Java': {'Java' in sentence}")

print("\n" + "="*50 + "\n")

# =============================================================================
# TRIM AND CLEAN METHODS
# =============================================================================

print("=== Trim and Clean Methods ===")

messy_text = "   Hello World!   "
print(f"Original: '{messy_text}'")
print(f"Strip: '{messy_text.strip()}'")      # Remove both ends
print(f"Lstrip: '{messy_text.lstrip()}'")    # Remove left side
print(f"Rstrip: '{messy_text.rstrip()}'")    # Remove right side

# Remove specific characters
dirty_text = "***Hello***"
print(f"Original: '{dirty_text}'")
print(f"Strip '*': '{dirty_text.strip('*')}'")

print("\n" + "="*50 + "\n")

# =============================================================================
# REPLACE METHODS
# =============================================================================

print("=== Replace Methods ===")

text = "I like apples. Apples are red."
print(f"Original: '{text}'")
print(f"Replace 'apples' with 'oranges': '{text.replace('apples', 'oranges')}'")
print(f"Replace 'Apples' with 'Oranges': '{text.replace('Apples', 'Oranges')}'")

# Replace all occurrences
print(f"Replace all 'a' with '*': '{text.replace('a', '*')}'")

print("\n" + "="*50 + "\n")

# =============================================================================
# SPLIT AND JOIN METHODS
# =============================================================================

print("=== Split and Join Methods ===")

# Split string
sentence = "Python is a programming language"
words = sentence.split()
print(f"Original: '{sentence}'")
print(f"Split into list: {words}")

# Split with specific delimiter
csv_data = "John,Doe,25,New York"
person_info = csv_data.split(',')
print(f"CSV data: '{csv_data}'")
print(f"Split by comma: {person_info}")

# Join list into string
words_list = ['Python', 'is', 'awesome']
joined_sentence = ' '.join(words_list)
print(f"List: {words_list}")
print(f"Joined with spaces: '{joined_sentence}'")

# Join with different separator
hyphenated = '-'.join(words_list)
print(f"Joined with hyphens: '{hyphenated}'")

print("\n" + "="*50 + "\n")

# =============================================================================
# CHECK METHODS
# =============================================================================

print("=== Check Methods ===")

test_strings = ["hello", "123", "Hello World", "", "   "]

for s in test_strings:
    print(f"'{s}':")
    print(f"  isalnum(): {s.isalnum()}")
    print(f"  isalpha(): {s.isalpha()}")
    print(f"  isdigit(): {s.isdigit()}")
    print(f"  islower(): {s.islower()}")
    print(f"  isupper(): {s.isupper()}")
    print(f"  isspace(): {s.isspace()}")
    print(f"  startswith('h'): {s.startswith('h')}")
    print(f"  endswith('o'): {s.endswith('o')}")
    print()

print("="*50 + "\n")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

print("=== Practical Examples ===")

# Example 1: Clean and format user input
print("Example 1: Clean User Input")
user_input = "   john doe   "
clean_name = user_input.strip().title()
print(f"Original input: '{user_input}'")
print(f"Cleaned name: '{clean_name}'")

# Example 2: Count words in a sentence
print("\nExample 2: Word Count")
paragraph = "Python is a powerful programming language. Python is easy to learn."
words = paragraph.split()
word_count = len(words)
print(f"Paragraph: '{paragraph}'")
print(f"Word count: {word_count}")

# Example 3: Validate email format
print("\nExample 3: Basic Email Validation")
email = "user@example.com"
if "@" in email and "." in email:
    if email.count("@") == 1:
        print(f"'{email}' appears to be a valid email")
    else:
        print(f"'{email}' has too many @ symbols")
else:
    print(f"'{email}' is not a valid email")

# Example 4: Create username from full name
print("\nExample 4: Create Username")
full_name = "John Smith"
username = full_name.lower().replace(" ", "_")
print(f"Full name: '{full_name}'")
print(f"Username: '{username}'")

print("\n" + "="*50 + "\n")

# =============================================================================
# SUMMARY
# =============================================================================

print("""
📚 COMMON STRING METHODS SUMMARY:

**Case Methods:**
- .upper() - Convert to uppercase
- .lower() - Convert to lowercase
- .title() - Convert to title case
- .capitalize() - Capitalize first letter

**Search Methods:**
- .find(substring) - Find first occurrence (returns -1 if not found)
- .count(substring) - Count occurrences
- 'substring' in string - Check if contains substring

**Trim Methods:**
- .strip() - Remove whitespace from both ends
- .lstrip() - Remove from left side
- .rstrip() - Remove from right side

**Replace Method:**
- .replace(old, new) - Replace all occurrences

**Split/Join Methods:**
- .split() - Split into list
- 'separator'.join(list) - Join list into string

**Check Methods:**
- .isalpha() - All letters?
- .isdigit() - All digits?
- .isalnum() - All alphanumeric?
- .islower()/.isupper() - All lowercase/uppercase?
- .startswith(prefix) - Starts with prefix?
- .endswith(suffix) - Ends with suffix?

💡 TIP: String methods return new strings, they don't modify the original!
""")
