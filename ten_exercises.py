"""
ten_exercises.py
A single-file Python program that implements 10 small exercises,
plus a demo `main()` that prints example results.

Exercises:
1) Given a list of numbers, find the sum and average.
2) Celsius to Kelvin converter.
3) Check if a string is a palindrome.
4) Reverse a string.
5) Concatenate a list of names with spaces.
6) Check if a string is a pangram (contains all letters a-z).
7) Area and circumference of a circle given its radius.
8) Convert minutes to hours and minutes.
9) Count number of vowels in a string.
10) Check if a number is prime.
"""

from math import pi, sqrt

# 1) Sum and Average
def sum_and_average(numbers):
    total = sum(numbers)
    avg = total / len(numbers) if numbers else 0
    return total, avg

# 2) Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# 3) Palindrome check (alphanumeric, case-insensitive)
def is_palindrome(s):
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

# 4) Reverse a string
def reverse_string(s):
    return s[::-1]

# 5) Concatenate names separated by spaces
def concat_names(names):
    return ' '.join(names)

# 6) Pangram (letters a-z at least once)
def is_pangram(s):
    s = s.lower()
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet.issubset(set(ch for ch in s if ch.isalpha()))

# 7) Circle area & circumference
def circle_area_circumference(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

# 8) Minutes to hours:minutes
def minutes_to_hours_minutes(minutes):
    if minutes < 0:
        raise ValueError("Minutes must be non-negative")
    h = minutes // 60
    m = minutes % 60
    return h, m

# 9) Count vowels (a,e,i,o,u; case-insensitive)
def count_vowels(s):
    vowels = set("aeiou")
    return sum(1 for ch in s.lower() if ch in vowels)

# 10) Prime check
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # check 6k ± 1 up to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def demo():
    print("=== DEMO: 10 Exercises ===")
    # 1
    nums = [3, 7, 2, 9, 5]
    total, avg = sum_and_average(nums)
    print(f"1) Sum & Avg of {nums} -> total={total}, average={avg:.2f}")
    # 2
    c = 25.0
    print(f"2) Celsius to Kelvin: {c}°C -> {celsius_to_kelvin(c)} K")
    # 3
    s1 = "A man, a plan, a canal: Panama!"
    print(f"3) Palindrome? '{s1}' -> {is_palindrome(s1)}")
    # 4
    s2 = "Hello World"
    print(f"4) Reverse '{s2}' -> '{reverse_string(s2)}'")
    # 5
    names = ["Ada", "Lovelace", "Alan", "Turing"]
    print(f"5) Concat names {names} -> '{concat_names(names)}'")
    # 6
    s3 = "The quick brown fox jumps over a lazy dog"
    print(f"6) Pangram? '{s3}' -> {is_pangram(s3)}")
    # 7
    r = 4.5
    area, circumference = circle_area_circumference(r)
    print(f"7) Circle r={r} -> area={area:.4f}, circumference={circumference:.4f}")
    # 8
    mins = 185
    h, m = minutes_to_hours_minutes(mins)
    print(f"8) {mins} minutes -> {h} hour(s) {m} minute(s)")
    # 9
    s4 = "Supercalifragilisticexpialidocious"
    print(f"9) Vowel count in '{s4}' -> {count_vowels(s4)}")
    # 10
    n = 97
    print(f"10) Prime? {n} -> {is_prime(n)}")

if __name__ == "__main__":
    demo()
