
class SubstringComparison:

    def __init__(self, starting_character: str):
        self.substring = starting_character
        self.substring_length = 1


class Solution:

    def lengthOfLongestSubstring(self, s: str):

        substring = ''
        longest_ever = 0

        for character in s:
            if character in substring:
                if len(substring) > longest_ever:
                    longest_ever = len(substring)

                character_location = substring.index(character)
                substring = substring[(character_location + 1):]
            substring += character

        # Handle case with no repeats
        if len(substring) >= longest_ever:
            longest_ever = len(substring)

        return longest_ever


    def lengthOfLongestSubstring1(self, s: str):
        """Actual question just wants the length, not the substring itself, so optimize for that here"""

        longest_substring_length = 0
        substrings = []

        for character in s:

            substring_index = 0

            while substring_index < len(substrings):
                substring = substrings[substring_index]

                if character in substring:
                    if len(substring) > longest_substring_length:
                        longest_substring_length = len(substring)
                    substrings.pop(substring_index)
                else:
                    substrings[substring_index] += character
                    substring_index += 1

            substrings.append(character)

        if substrings:
            last_longest_substring = substrings[0]
            if len(last_longest_substring) > longest_substring_length:
                longest_substring_length = len(last_longest_substring)

        return longest_substring_length

    def find_longest_substring(self, s: str):

        longest_substring = ''
        longest_substring_length = len(longest_substring)
        substrings = []

        for character in s:

            for substring_index, substring in enumerate(substrings):
                if character in substring:
                    if len(substring) > longest_substring_length:
                        longest_substring = substring
                        longest_substring_length = len(substring)
                    substrings.pop(substring_index)
                    continue
                else:
                    substrings[substring_index] += character
            substrings.append(character)

        if substrings:
            last_longest_substring = substrings[0]
            if len(last_longest_substring) > longest_substring_length:
                longest_substring = last_longest_substring
                longest_substring_length = len(longest_substring)

        return longest_substring
