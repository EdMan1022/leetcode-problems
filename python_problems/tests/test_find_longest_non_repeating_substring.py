from unittest import TestCase
from python_problems.src.find_longest_non_repeating_substring import Solution


class TestSubstring(TestCase):

    def test_substring_at_front(self):
        input_string = 'abcabcbb'
        expected_substring = 'abc'
        actual_substring = Solution().find_longest_substring(input_string)
        assert expected_substring == actual_substring

    def test_all_repeat(self):
        input_string = 'bbbb'
        expected_substring = 'b'
        actual_substring = Solution().find_longest_substring(input_string)
        assert expected_substring == actual_substring

    def test_sub_at_back(self):
        input_string = 'pwwkew'
        expected_substring = 'wke'
        actual_substring = Solution().find_longest_substring(input_string)
        assert expected_substring == actual_substring


class TestSubstringLength(TestCase):

    def test_substring_at_front(self):
        input_string = 'abcabcbb'
        expected_substring_length = 3
        actual_substring = Solution().lengthOfLongestSubstring(input_string)
        assert expected_substring_length == actual_substring

    def test_all_repeat(self):
        input_string = 'bbbb'
        expected_substring_length = 1
        actual_substring = Solution().lengthOfLongestSubstring(input_string)
        assert expected_substring_length == actual_substring

    def test_pop_causes_skipped_substring_addition(self):
        """
        When the too long substring is popped from the list, the python for loop doesn't compensate for this

        Causes the substring immediately after the popped one to not have the current character added to it
        """
        input_string = 'dvdfv'
        expected_substring_length = 3
        actual_substring = Solution().lengthOfLongestSubstring(input_string)
        assert actual_substring == expected_substring_length

    def test_continue_issue(self):
        input_string = ''

    def test_sub_at_back(self):
        input_string = 'pwwkew'
        expected_substring_length = 3
        actual_substring = Solution().lengthOfLongestSubstring(input_string)
        assert expected_substring_length == actual_substring

    def test_no_repeats(self):
        input_string = 'abcdefghijklmnop'
        expected_substring_length = 16
        actual_substring = Solution().lengthOfLongestSubstring(input_string)
        assert expected_substring_length == actual_substring
