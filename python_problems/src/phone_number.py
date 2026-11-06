digit_map = {
    '1': [],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
    '0': []
}

def recursive_combine(full_output_list, root: str, remaining_digit_lists: list):
    this_level_digits = remaining_digit_lists[0]
    deeper_level_digits = remaining_digit_lists[1:]

    if deeper_level_digits:
        for this_level_digit in this_level_digits:
            this_root = root + this_level_digit
            recursive_combine(full_output_list, this_root, deeper_level_digits)

    else:
        for this_level_digit in this_level_digits:
            this_root = root + this_level_digit
            full_output_list.append(this_root)


class Solution:

    def letterCombinations(self, digits):

        output_list = []
        start_root = ''

        if digits == '':
            return output_list
        else:
            list_of_digit_combos = [digit_map[digit] for digit in digits]
            recursive_combine(output_list, start_root, list_of_digit_combos)
            result = output_list
            return result
