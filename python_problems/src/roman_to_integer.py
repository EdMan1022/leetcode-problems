class Solution:
    def romanToInt(self, s: str) -> int:
        """Takes a roman numeral and returns an integer"""
        s += 'I'

        symbol_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        combined_symbol_map = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        output_sum = 0

        if len(s) == 1:
            return symbol_map[s]

        first_symbol = s[0]
        skip_one = False
        for second_symbol in s[1:]:

            if skip_one:
                skip_one = False
                first_symbol = second_symbol
                continue

            if combined_symbol_value := combined_symbol_map.get(first_symbol + second_symbol):
                output_sum += combined_symbol_value
                skip_one = True
            else:
                output_sum += symbol_map[first_symbol]
            first_symbol = second_symbol

        return output_sum
