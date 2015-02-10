__author__ = 'Lenovo'
import sys
import re
accs = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455","xjhd53e", "45da", "de37dp"]
for acc in accs:
    #contain the number 5
    if re.search(r"5",acc):
        print("contain the number 5: "+acc)

    #contain the letter d or e
    if (re.search(r"d|e",acc)):
        print("contain the letter d or e: " + acc)

    #contain the letters d and e in that order
    if (re.search(r"d.*e",acc)):
        print("contain the letters d and e in that order: " + acc)

    #contain the letters d and e in that order with a single letter between them
    if (re.search(r"d.e",acc)):
        print("contain the letters d and e in that order with a single letter between them: " + acc)

    #contain both the letters d and e in any order
    if (re.search(r"d.*e",acc) or re.search(r"e.*d",acc)):
        print("contain both the letters d and e in any order: " + acc)

    #start with x or y
    if (re.search(r"^(x|y)",acc)):
        print("start with x or y:" + acc)

    #start with x or y and end with e
    if (re.search(r"^(x|y).*e$",acc)):
        print("start with x or y and end with e: " + acc)

    #contain three or more numbers in a row
    if (re.search(r"\d{3,}",acc)):
        print("contain three or more numbers in a row: " + acc)

    #end with d followed by either a, r or p
    if re.search(r"d[arp]$", acc):
        print("end with d followed by either a, r or p: " + acc)