#!/usr/bin/env python3
# ------
# SETUP
# ------

import sys

# Settings
enable_uppercase = True
enable_newline_perword = False

def newline_disabled(passed_sentence):
    temp_sentence = ""
    for i in range(len(passed_sentence)):
        temp_sentence += f"{passed_sentence[i]} "
    return temp_sentence

def newline_enabled(passed_sentence):
    temp_sentence = ""
    for i in range(len(passed_sentence)):
        if (passed_sentence[i] == " "):
            temp_sentence += f"{passed_sentence[i]}\n"
        else:
            temp_sentence += f"{passed_sentence[i]} "
    return temp_sentence

sentence = input("Enter text to be converted to ANT text: ")

# -----------
# CONVERSION
# -----------

# Convert to uppercase if selected
if (enable_uppercase):
    sentence = sentence.upper()

new_sentence = ""

if (enable_newline_perword):
    new_sentence = newline_enabled(sentence)
    print(new_sentence)
elif not (enable_newline_perword):
    new_sentence = newline_disabled(sentence)
    print(new_sentence)
else:
    print("Conversion stage error - check newline enablement")
    sys.exit(1)
