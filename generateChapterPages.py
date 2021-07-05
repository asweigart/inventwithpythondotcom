import os


books = {
    'bigbookpython': [('introduction', 'Introduction'), ('project1', 'Bagels'), ('project2', 'Birthday Paradox'), ('project3', 'Bitmap Message'), ('project4', 'Blackjack'), ('project5', 'Bouncing DVD Logo'), ('project6', 'Caesar Cipher'), ('project7', 'Caesar Hacker'), ('project8', 'Calendar Maker'), ('project9', 'Carrot in a Box'), ('project10', 'Cho-Han'), ('project11', 'Clickbait Headline Generator'), ('project12', 'Collatz Sequence'), ('project13', "Conway's Game of Life"), ('project14', 'Countdown'), ('project15', 'Deep Cave'), ('project16', 'Diamonds'), ('project17', 'Dice Math'), ('project18', 'Dice Roller'), ('project19', 'Digital Clock'), ('project20', 'Digital Stream'), ('project21', 'DNA Visualization'), ('project22', 'Ducklings'), ('project23', 'Etching Drawer'), ('project24', 'Factor Finder'), ('project25', 'Fast Draw'), ('project26', 'Fibonacci'), ('project27', 'Fish Tank'), ('project28', 'Flooder'), ('project29', 'Forest Fire Sim'), ('project30', 'Four in a Row'), ('project31', 'Guess the Number'), ('project32', 'Gullible'), ('project33', 'Hacking Minigame'), ('project34', 'Hangman & Guillotine'), ('project35', 'Hex Grid'), ('project36', 'Hourglass'), ('project37', 'Hungry Robots'), ('project38', "J'Accuse!"), ('project39', "Langton's Ant"), ('project40', 'Leetspeak'), ('project41', 'Lucky Stars'), ('project42', 'Magic Fortune Ball'), ('project43', 'Mancala'), ('project44', 'Maze Runner 2D'), ('project45', 'Maze Runner 3D'), ('project46', 'Million Dice Statistics'), ('project47', 'Mondrian Art Generator'), ('project48', 'Monty Hall'), ('project49', 'Multiplication Table'), ('project50', 'Ninety Nine Bottles'), ('project51', 'niNety nniinE BoOttels'), ('project52', 'Numeral Systems'), ('project53', 'Periodic Table of the Elements'), ('project54', 'Pig Latin'), ('project55', 'Powerball Lottery'), ('project56', 'Prime Numbers'), ('project57', 'Progress Bar'), ('project58', 'Rainbow'), ('project59', 'Rock Paper Scissors'), ('project60', 'Rock Paper Scissors (Always-Win Version)'), ('project61', 'ROT 13 Cipher'), ('project62', 'Rotating Cube'), ('project63', 'Royal Game of Ur'), ('project64', 'Seven-Segment Display Module'), ('project65', 'Shining Carpet'), ('project66', 'Simple Substitution Cipher'), ('project67', 'Sine Message'), ('project68', 'Sliding Tile Puzzle'), ('project69', 'Snail Race'), ('project70', 'Soroban Japanese Abacus'), ('project71', 'Sound Mimic'), ('project72', 'sPoNgEcAsE'), ('project73', 'Sudoku Puzzle'), ('project74', 'Text To Speech Talker'), ('project75', 'Three-Card Monte'), ('project76', 'Tic-Tac-Toe'), ('project77', 'Tower of Hanoi Puzzle'), ('project78', 'Trick Questions'), ('project79', 'Twenty Forty Eight'), ('project80', 'Vigenère Cipher'), ('project81', 'Water Bucket Puzzle'), ('appendixa', 'Appendix A'), ('appendixb', 'Appendix B')],
    'beyond': [('chapter0', 'Introduction'), ('chapter1', 'Chapter 1 - Dealing with Errors and Asking for Help'), ('chapter2', 'Chapter 2 - Environment Setup and the Command Line'), ('chapter3', 'Chapter 3 - Code Formatting with Black'), ('chapter4', 'Chapter 4 - Choosing Understandable Names'), ('chapter5', 'Chapter 5 - Finding Code Smells'), ('chapter6', 'Chapter 6 - Writing Pythonic Code'), ('chapter7', 'Chapter 7 - Programming Jargon'), ('chapter8', 'Chapter 8 - Common Python Gotchas'), ('chapter9', 'Chapter 9 - Esoteric Python Oddities'), ('chapter10', 'Chapter 10 - Writing Effective Functions'), ('chapter11', 'Chapter 11 - Comments, Docstrings, and Type Hints'), ('chapter12', 'Chapter 12 - Organizing Your Code Projects with Git'), ('chapter13', 'Chapter 13 - Measuring Performance and Big O Algorithm Analysis'), ('chapter14', 'Chapter 14 - Practice Projects'), ('chapter15', 'Chapter 15 - Object-Oriented Programming and Classes'), ('chapter16', 'Chapter 16 - Object-Oriented Programming and Inheritance'), ('chapter17', 'Chapter 17 - Pythonic OOP: Properties and Dunder Methods')],
    'invent4thed': [('chapter0', 'Introduction'), ('chapter1', 'Chapter 1 - The Interactive Shell'), ('chapter2', 'Chapter 2 - Writing Programs'), ('chapter3', 'Chapter 3 - Guess the Number'), ('chapter4', 'Chapter 4 - A Joke-Telling Program'), ('chapter5', 'Chapter 5 - Dragon Realm'), ('chapter6', 'Chapter 6 - Using the Debugger'), ('chapter7', 'Chapter 7 - Designing Hangman with Flowcharts'), ('chapter8', 'Chapter 8 - Writing the Hangman Code'), ('chapter9', 'Chapter 9 - Extending Hangman'), ('chapter10', 'Chapter 10 - Tic-Tac-Toe'), ('chapter11', 'Chapter 11 - The Bagels Deduction Game'), ('chapter12', 'Chapter 12 - The Cartesian Coordinate System'), ('chapter13', 'Chapter 13 - Sonar Treasure Hunt'), ('chapter14', 'Chapter 14 - Caesar Cipher'), ('chapter15', 'Chapter 15 - The Reversegam Game'), ('chapter16', 'Chapter 16 - Reversegam AI Simulation'), ('chapter17', 'Chapter 17 - Creating Graphics'), ('chapter18', 'Chapter 18 - Animating Graphics'), ('chapter19', 'Chapter 19 - Collision Detection'), ('chapter20', 'Chapter 20 - Using Sounds And Images'), ('chapter21', 'Chapter 21 - A Dodger Game with Sounds and Images')],
    #PYGAME DOESN'T USE TXT FILES#'pygame': [('chapter1', 'Chapter 1 - Installing Python and Pygame'), ('chapter2', 'Chapter 2 - Pygame Basics'), ('chapter3', 'Chapter 3 - Memory Puzzle'), ('chapter4', 'Chapter 4 - Slide Puzzle'), ('chapter5', 'Chapter 5 - Simulate'), ('chapter6', 'Chapter 6 - Wormy'), ('chapter7', 'Chapter 7 - Tetromino'), ('chapter8', 'Chapter 8 - Squirrel Eat Squirrel'), ('chapter9', 'Chapter 9 - Star Pusher'), ('chapter10', 'Chapter 10 - Four Extra Games')],
    'cracking': [('chapter0', 'Introduction'), ('chapter1', 'Chapter 1 - Making Paper Cryptography Tools'), ('chapter2', 'Chapter 2 -Programming in the Interactive Shell '), ('chapter3', 'Chapter 3 - Strings and Writing Programs'), ('chapter4', 'Chapter 4 - The Reverse Cipher'), ('chapter5', 'Chapter 5 - The Caesar Cipher'), ('chapter6', 'Chapter 6 - Hacking the Caesar Cipher with Brute-Force'), ('chapter7', 'Chapter 7 - Encrypting with the Transposition Cipher'), ('chapter8', 'Chapter 8 - Decrypting with the Transposition Cipher'), ('chapter9', 'Chapter 9 - Programming a Program to Test Your Program'), ('chapter10', 'Chapter 10 - Encrypting and Decrypting Files'), ('chapter11', 'Chapter 11 - Detecting English Programmatically'), ('chapter12', 'Chapter 12 - Hacking the Transposition Cipher'), ('chapter13', 'Chapter 13 - A Modular Arithmetic Module for the Affine Cipher'), ('chapter14', 'Chapter 14 - Programming the Affine Cipher'), ('chapter15', 'Chapter 15 - Hacking the Affine Cipher'), ('chapter16', 'Chapter 16 - Programming the Simple Substitution Cipher'), ('chapter17', 'Chapter 17 - Hacking the Simple Substitution Cipher'), ('chapter18', 'Chapter 18 - Programming the Vigenere Cipher'), ('chapter19', 'Chapter 19 - Frequency Analysis'), ('chapter20', 'Chapter 20 - Hacking the Vigenere Cipher'), ('chapter21', 'Chapter 21 - The One-Time Pad Cipher'), ('chapter22', 'Chapter 22 - Finding and Generating Prime Numbers'), ('chapter23', 'Chapter 23 - Generating Keys for the Public Key Cipher'), ('chapter24', 'Chapter 24 - Programming the Public Key Cipher'), ('appendixa', 'Debugging Python Code')],
    }


header = """<html><head><meta http-equiv="Content-Type" content="text/html;charset=utf-8" /><link href="style.css" rel="stylesheet" type="text/css" /><title>%s</title></head><body style="background-color: #fffeee;">

<script type="text/javascript">
//<![CDATA[

var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-5459430-3']);
_gaq.push(['_trackPageview']);

(function() {
  var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
  ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
  var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();

//]]>
</script>


<div style="background-color: #eeeddd; float: right; height: 310px; font-family: sans-serif;" id="otherbooks">
  <a href="#" onclick="document.getElementById('otherbooks').outerHTML='';" style="vertical-align: top;">(close)</a><br />

  <a target="_blank" href="https://nostarch.com/automatestuff2" onclick="javascript: pageTracker._trackPageview('/affiliate_chapters_automate.link');"><img src="/images/cover_automate2_thumb.jpg" style="height: 200px; border: solid black 1px;" /></a>
  <a target="_blank" href="https://nostarch.com/big-book-small-python-projects" onclick="javascript: pageTracker._trackPageview('/affiliate_chapters_bigbookpython.link');"><img src="/images/cover_bigbookpython_thumb.jpg" style="height: 200px; border: solid black 1px;" /></a>
  <a target="_blank" href="https://nostarch.com/beyond-basic-stuff-python" onclick="javascript: pageTracker._trackPageview('/affiliate_chapters_beyond.link');"><img src="/images/cover_beyond_thumb.jpg" style="height: 200px; border: solid black 1px;" /></a>
  <a target="_blank" href="https://nostarch.com/inventwithpython" onclick="javascript: pageTracker._trackPageview('/affiliate_chapters_invent.link');"><img src="/images/cover_invent4th_thumb.png" style="height: 200px; border: solid black 1px;" /></a>
  <a target="_blank" href="https://www.amazon.com/Making-Games-Python-Pygame-Sweigart/dp/1469901730?ie=UTF8&amp;tag=playwithpyth-20&amp;linkCode=as2&amp;camp=1789&amp;creative=9325&amp;creativeASIN=1469901730" onclick="javascript: pageTracker._trackPageview('/affiliate_chapters_pygame.link');"><img src="/images/cover_makinggames_thumb.png" style="height: 200px; border: solid black 1px; /"></a>
  <a target="_blank" href="https://nostarch.com/crackingcodes" onclick="javascript: pageTracker._trackPageview('/affiliate_chapters_hacking.link');"><img src="/images/cover_crackingcodes_thumb.png" style="height: 200px; border: solid black 1px;" /></a>
  <a target="_blank" href="https://nostarch.com/scratchplayground"><img src="/images/cover_scratchprogrammingplayground_thumb.png" style="height: 200px; border: solid black 1px;" /></a>
  <a target="_blank" href="https://nostarch.com/codingwithminecraft"><img src="/images/cover_codingwithminecraft_thumb.jpg" style="height: 200px; border: solid black 1px;" /></a>
  <br />
  <a href="https://inventwithpython.com/automateudemy">Use this link to get 70%% off the Automate the Boring Stuff online video course.</a><br />
  <a href="https://www.patreon.com/AlSweigart">Support me on Patreon</a>
</div>

%s
"""

footer = """%s
</body></html>"""

for book, chapters in books.items():
    for i, (filename, title) in enumerate(chapters):


        if i == 0:
            nextFullPath = '/'.join([chapters[i + 1][0] + '.html'])
            nextTitle = chapters[i + 1][1]
            prevNextHtml = '<a href="%s">Next: %s</a>' % (nextFullPath, nextTitle)
        elif i == len(chapters) - 1:
            prevFullPath = '/'.join([chapters[i - 1][0] + '.html'])
            prevTitle = chapters[i - 1][1]
            prevNextHtml = '<a href="%s">Prev: %s</a>' % (prevFullPath, prevTitle)
        else:
            prevFullPath = '/'.join([chapters[i - 1][0] + '.html'])
            nextFullPath = '/'.join([chapters[i + 1][0] + '.html'])
            prevTitle = chapters[i - 1][1]
            nextTitle = chapters[i + 1][1]
            prevNextHtml = '<a href="%s">Prev: %s</a> | <a href="%s">Next: %s</a>' % (prevFullPath, prevTitle, nextFullPath, nextTitle)

        fullPathHtml = os.path.join('static', book, filename + '.html') # `book` is also the folder name
        fullPathTxt = os.path.join('static_src', book, filename + '.txt')


        with open(fullPathHtml, 'w', encoding='utf-8') as outputHtmlFile:
            print('Writing', fullPathHtml)
            with open(fullPathTxt, encoding='utf-8') as chapterSourceFile:
                chapterContent = chapterSourceFile.read()

                outputHtmlFile.write(header % (title, prevNextHtml))
                outputHtmlFile.write('\n\n' + chapterContent + '\n\n\n')
                outputHtmlFile.write(footer % (prevNextHtml))

