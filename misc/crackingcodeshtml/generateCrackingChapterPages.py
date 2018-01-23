import os


header = """<html><head><meta http-equiv="Content-Type" content="text/html;charset=utf-8" /><link href="style_cracking.css" rel="stylesheet" type="text/css" /><title>Cracking Codes with Python</title></head><body style="background-color: #fffeee;">

"""

footer = """
</body></html>"""


adLink = """<div><a target="_blank" href="https://www.amazon.com/gp/product/1593278225/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1593278225&linkCode=as2&tag=playwithpyth-20&linkId=bf3b22819f0886d277e88b8a653b81ad">
<img src="images/cover_crackingcodes_thumb.png" /><br />Buy the print or ebook online.</a></div>"""


prevLinks = """<div><a href="chapter%s.html">Previous Chapter - %s</a></div>"""
nextLinks = """<div><a href="chapter%s.html">Next Chapter - %s</a></div>"""
prevNextLinks = """<div><a href="chapter%s.html">Previous Chapter - %s</a> | <a href="chapter%s.html">Next Chapter - %s</a></div>"""


chapterNames = """Introduction
Making Paper Cryptography Tools
Programming in the Interactive Shell
String and Writing Programs
The Reverse Cipher
The Caesar Cipher
Hacking the Caesar Cipher with Brute-Force
Encrypting with the Transposition Cipher
Decrypting with the Transposition Cipher
Programming a Program to Test Your Program
Encrypting and Decrypting Files
Detecting English Programmatically
Hacking the Transposition Cipher
A Modular Arithmetic Module for the Affine Cipher
Programming The Affine Cipher
Hacking the Affine Cipher
Programming the Simple Substitution Cipher
Hacking the Simple Substitution Cipher
Programming the Vigenère Cipher
Frequency Analysis
Hacking the Vigenère Cipher
The One-Time Pad Cipher
Finding and Generating Prime Numbers
Generating Keys for the Public Key Cipher
Public Key Cryptography and the Public Key Cipher""".split('\n')

for chapterNum in range(25):
    print(chapterNum)

    sourceTextFileObj = open('chapter%s.txt' % (chapterNum), encoding='utf-8')
    sourceContent = sourceTextFileObj.read()
    sourceTextFileObj.close()

    if chapterNum == 24:
        pnLinks = prevLinks % (chapterNum - 1, chapterNames[chapterNum - 1])
    elif chapterNum == 0:
        pnLinks = nextLinks % (chapterNum + 1, chapterNames[chapterNum + 1])
    else:
        pnLinks = prevNextLinks % (chapterNum - 1, chapterNames[chapterNum - 1], chapterNum + 1, chapterNames[chapterNum + 1])

    htmlFileObj = open('chapter%s.html' % (chapterNum), 'w', encoding='utf-8')
    htmlFileObj.write('\n'.join([header, adLink, pnLinks, sourceContent, pnLinks, adLink]))
    htmlFileObj.close()
