#!/usr/bin/env python3
"""
Smart Text Analyzer
Analyzes text input and provides various statistics.
"""

def main():
    print("=" * 50)
    print("📝 SMART TEXT ANALYZER 📝")
    print("=" * 50)
    sentence = input("Please enter a sentence and our system will do the magic! \n>>> ")
    
    # Handle empty input
    if not sentence.strip():
        print("\n❌ No text entered. Exiting...")
        return
    
    print("\n" + "=" * 50)
    print("📊 ANALYSIS RESULTS 📊")
    print("=" * 50)

    # Character count
    character_number = len(sentence)
    
    # Word analysis
    words = sentence.split()
    word_number = len(words)
    
    # Longest word finder logic
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    # Vowel counter logic
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    for char in sentence.lower():
        if char in vowels:
            vowel_count += 1
    
    # Uppercase and lowercase versions logic
    uppercase_version = sentence.upper()
    lowercase_version = sentence.lower()
    
    # Word frequency
    frequency = {}
    for word in words:
        # Normalize words for frequency counting (remove punctuation)
        clean_word = ''.join(char for char in word if char.isalnum()).lower()
        if clean_word:  # Only count non-empty words
            if clean_word in frequency:
                frequency[clean_word] += 1
            else:
                frequency[clean_word] = 1
    
    # Print results with better formatting
    print(f"📈 Number of characters: {character_number}")
    print(f"📚 Number of words: {word_number}")
    print(f"📏 Longest word: '{longest_word}' ({len(longest_word)} characters)")
    print(f"🎵 Number of vowels: {vowel_count}")
    print(f"👆 Uppercase version: {uppercase_version}")
    print(f"👇 Lowercase version: {lowercase_version}")
    
    print("\n🔍 Word frequencies:")
    if frequency:
        for word, count in sorted(frequency.items(), key=lambda x: x[1], reverse=True):
            if count > 1:
                print(f"   • '{word}' appears {count} times")
            else:
                print(f"   • '{word}' appears {count} time")
    else:
        print("   No words found.")
    
    print("\n" + "=" * 50)
    print("✨ Analysis complete! ✨")
    print("=" * 50)

if __name__ == "__main__":
    main()