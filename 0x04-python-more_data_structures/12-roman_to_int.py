#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_sign = {"I": 1, "V": 5, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000}
    arabic_num = 0
    i = 0
    if not isinstance(roman_string, str) or len(roman_string) == 0:
        return None
    while i < len(roman_string):
        if roman_string[i] == "I":
            if (i + 1) <= len(roman_string) - 1:
                if roman_string[i + 1] != "I":
                    arabic_num += roman_sign[roman_string[i + 1]] - 1
                    i += 1

            else:
                arabic_num += roman_sign[roman_string[i]] + 1
        else:
            arabic_num += roman_sign[roman_string[i]]
        i += 1
    return arabic_num
