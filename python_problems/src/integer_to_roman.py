import math
roman_num_conversion_table = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}
place_conversion_table = {
    4: 'M',
    3: 'C',
    2: 'X',
    1: 'I'
}

place_5_conversion_table = {
    3: 'D',
    2: 'L',
    1: 'V'
}


class Solution:

    def intToRoman(self, num):
        """
        Convert an integer number into the Roman Numeral format
        :param num: integer to be converted
        :return: (str) Roman numeral representation of the num
        """


        string_num = str(num)
        places = len(string_num)
        roman_string = ''

        for index, place_value in enumerate(string_num):
            current_place = places - index
            place_value = int(place_value)
            if current_place not in place_5_conversion_table:
                roman_string += place_value * place_conversion_table[current_place]
            else:
                if place_value < 4:
                    roman_string += place_value * place_conversion_table[current_place]
                elif place_value == 4:
                    roman_string += place_conversion_table[current_place] + place_5_conversion_table[current_place]
                elif place_value == 9:
                    roman_string += place_conversion_table[current_place] + place_conversion_table[current_place + 1]
                else:
                    roman_string += place_5_conversion_table[current_place] + ((place_value - 5) * place_conversion_table[current_place])

        return roman_string
