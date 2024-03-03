class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        count = 0
        current_val = None
        check_list = ["I", "X", "C"]
        for i in s:
            if current_val in check_list:
                if (current_val == "I") and (i == "V"):
                    count += 4
                    current_val = None
                    count += -1
                elif (current_val == "I") and (i == "X"):
                    count += 9
                    current_val = None
                    count += -1
                elif (current_val == "X") and (i == "L"):
                    count += 40
                    current_val = None
                    count += -10
                elif (current_val == "X") and (i == "C"):
                    count += 90
                    current_val = None
                    count += -10
                elif (current_val == "C") and (i == "D"):
                    count += 400
                    current_val = None
                    count += -100
                elif (current_val == "C") and (i == "M"):
                    count += 900
                    current_val = None
                    count += -100
                else:
                    count += roman_dict.get(i)
                    # current_val = None
            else:
                count += roman_dict.get(i)

            if i in check_list:
                current_val = i

        return count
        