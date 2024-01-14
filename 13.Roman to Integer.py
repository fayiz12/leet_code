class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        total_sum = 0
        prev_value = 0 
        for i in s:
            if i in roman_dict:
                current_value = roman_dict[i]
                

                if current_value > prev_value:
                    total_sum += current_value - 2 * prev_value
                else:
                    total_sum += current_value

                prev_value = current_value

        return total_sum
