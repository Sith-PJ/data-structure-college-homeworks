"""Give a string 'X-DSPAM-Confidence: 0.2304'.  Compute the square root of the number 
after the colon.

Source: http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf 
"""

import math

def ExtractFloatFromString(num):
    root = math.sqrt(float(num))
    return root

def main():
    num = "X-DSPAM-Confidence: 0.2304".split(":")[-1]
    print(ExtractFloatFromString(num))

if __name__ == "__main__":
    main()