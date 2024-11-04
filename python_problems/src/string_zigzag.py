class Solution:

    def convert(self, s, numRows):


        row_lists = [
            list()
            for row in range(numRows)
        ]

        s_length = len(s)
        current_row = numRows - 1
        s_index = 0
        at_end_of_string = False

        while not at_end_of_string:
            if current_row == 0 or current_row == (numRows - 1):
                for row_list in row_lists:
                    row_list.append(s[s_index])
                    s_index += 1
                    if s_index >= s_length:
                        at_end_of_string = True
                        break
            else:
                row_lists[current_row].append(s[s_index])
                s_index += 1
            current_row -= 1
            if current_row < 0:
                current_row = numRows - 2
            if s_index >= s_length:
                at_end_of_string = True

        return ''.join([''.join(row_list) for row_list in row_lists])
