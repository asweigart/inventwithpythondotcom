#!python3

# Generates the /chapters, /pygame/chapters, and /hacking/chapters pages from source data.

import os


inventData = [{'name': 'Installing Python',
               'videos': [{'name': 'Installing Python on Windows', 'url': 'http://www.youtube-nocookie.com/embed/4Mf0h3HphEA'},
                          {'name': 'Installing Python 3.1 under MacOSX', 'url': 'http://www.youtube-nocookie.com/embed/MEmEJCLLI2k'},
                          {'name': 'Install Python 3.1 using Linux', 'url': 'http://www.youtube-nocookie.com/embed/RLPYBxfAud4'}],
                          },
            {'name': 'The Interactive Shell'},
            {'name': 'Strings',
             'programs': ['hello.py']},
            {'name': 'Guess the Number',
             'programs': ['guess.py']},
            {'name': 'Jokes',
             'programs': ['jokes.py']},
            {'name': 'Dragon Realm',
             'programs': ['dragon.py']},
            {'name': 'Using the Debugger'},
            {'name': 'Flow Charts'},
            {'name': 'Hangman',
             'programs': ['hangman.py']},
            {'name': 'Tic Tac Toe',
             'programs': ['tictactoe.py']},
            {'name': 'Bagels',
             'programs': ['bagels.py']},
            {'name': 'Cartesian Coordinates'},
            {'name': 'Sonar',
             'programs': ['sonar.py']},
            {'name': 'Caesar Cipher',
             'programs': ['cipher.py']},
            {'name': 'Reversi',
             'programs': ['reversi.py']},
            {'name': 'AI Simulation',
             'programs': ['AISim1.py', 'AISim2.py', 'AISim3.py']},
            {'name': 'Graphics and Animation',
             'programs': ['pygameHelloWorld.py'],
             'videos': [{'name': 'Installing Pygame on Windows', 'url': 'http://www.youtube-nocookie.com/embed/0xgn-HKzZes'}]},
            {'name': 'Collision Detection and Input',
             'programs': ['collisionDetection.py', 'pygameInput.py']},
            {'name': 'Sounds and Images',
             'programs': ['spritesAndSounds.py'],
             'downloads': ['cherry.png', 'player.png', 'background.mid', 'pickup.wav']},
            {'name': 'Dodger',
             'programs': ['dodger.py'],
             'downloads': ['baddie.png', 'player.png', 'background.mid', 'gameover.wav']}
             ]

pygameData = [{'name': 'Installing Python'},
            {'name': 'Pygame Basics',
             'programs': ['blankpygame.py', 'drawing.py', 'catanimation.py']},
            {'name': 'Memory Puzzle',
             'programs': ['memorypuzzle.py']},
            {'name': 'Slide Puzzle',
             'programs': ['slidepuzzle.py']},
            {'name': 'Simulate',
             'programs': ['simulate.py']},
            {'name': 'Wormy',
             'programs': ['wormy.py']},
            {'name': 'Tetromino',
             'programs': ['tetromino.py', 'pentomino.py', 'tetrominoforidiots.py'],
             'downloads': ['tetromino.zip']},
            {'name': 'Squirrel Eat Squirrel',
             'programs': ['squirrel.py'],
             'downloads': ['squirrel.zip']},
            {'name': 'Star Pusher',
             'programs': ['starpusher.py']},
            {'name': 'Four Extra Games',
             'programs': ['flippy.py', 'inkspill.py', 'fourinarow.py', 'gemgem.py'],
             'downloads': ['flippy.zip', 'inkspill.zip', 'fourinarow.zip', 'gemgem.zip']}]

hackingData = [{'name': 'Making Paper Cryptography Tools',
                'links': [{'name':'PDF of the Caesar Cipher Wheel', 'url':'http://inventwithpython.com/cipherwheel/cipherdisk_cutout_page.pdf'},
                          {'name':'Interactive Virtual Cipher Wheel', 'url':'http://inventwithpython.com/cipherwheel'}]},
            {'name': 'Downloading and Installing Python',
             'links': [{'name':'Download Python 3', 'url':'http://www.python.org/getit/'},
                       {'name':'Download pyperclip.py', 'url':'http://inventwithpython.com/pyperclip.py'}]},
            {'name': 'The Interactive Shell'},
            {'name': 'String and Writing Programs',
             'programs': ['hello.py']},
            {'name': 'The Reverse Cipher',
             'programs': ['reverseCipher.py']},
            {'name': 'The Caesar Cipher',
             'programs': ['caesarCipher.py', 'caesarCipher2.py', 'password.py', 'password2.py', 'elifeggs.py']},
            {'name': 'Hacking the Caesar Cipher with the Brute Force Technique',
             'programs': ['caesarHacker.py']},
            {'name': 'The Transposition Cipher, Encrypting',
             'programs': ['transpositionEncrypt.py']},
            {'name': 'The Transposition Cipher, Decrypting',
             'programs': ['transpositionDecrypt.py']},
            {'name': 'Programming a Program to Test Our Program',
             'programs': ['transpositionTest.py']},
            {'name': 'Encrypting and Decrypting Files',
             'programs': ['transpositionFileCipher.py']},
            {'name': 'Detecting English Programmatically',
             'programs': ['detectEnglish.py']},
            {'name': 'Hacking the Transposition Cipher',
             'programs': ['transpositionHacker.py']},
            {'name': 'Modular Arithmetic and the Multiplicative Cipher',
             'programs': ['cryptomath.py']},
            {'name': 'The Affine Cipher',
             'programs': ['affineCipher.py', 'affineKeyTest.py']},
            {'name': 'Hacking the Affine Cipher',
             'programs': ['affineHacker.py']},
            {'name': 'The Simple Substitution Cipher',
             'programs': ['simpleSubCipher.py']},
            {'name': 'Hacking the Simple Substitution Cipher',
             'programs': ['makeWordPatterns.py', 'wordPatterns.py', 'simpleSubHacker.py']},
            {'name': 'The Vigenère Cipher',
             'programs': ['vigenereCipher.py']},
            {'name': 'Frequency Analysis',
             'programs': ['freqAnalysis.py']},
            {'name': 'Hacking the Vigenère Cipher',
             'programs': ['vigenereHacker.py', 'vigenereDictionaryHacker.py']},
            {'name': 'The One-Time Pad Cipher'},
            {'name': 'Finding Prime Numbers',
             'programs': ['primeSieve.py', 'rabinMiller.py']},
            {'name': 'Public Key Cryptography and the RSA Cipher',
             'programs': ['makeRsaKeys.py', 'rsaCipher.py']}
            ]


bookData = {'': inventData,
            'pygame': pygameData,
            'hacking': hackingData}
bookTitle = {'': 'Invent Your Own Computer Games with Python',
             'pygame': 'Making Games with Python & Pygame',
             'hacking': 'Hacking Secret Ciphers with Python',}

for book in bookData.keys():
      fp = open(os.path.join('content', book, 'chapters', 'index.html'), 'w', encoding='utf-8')
      fp.write("""{%% extends "base.html" %%}
{%% set title = '%s' %%}
{%% block content %%}

<h1>Chapters</h1>

TODO - DOWNLOAD PDF LINK

""" % (bookTitle[book]))

      for chapterIndex in range(len(bookData[book])):
            fp.write('<div><a href="chapter%s.html" class="chapterlink">Chapter %s - %s</a><a href="index.html#chapter%s" class="relatedcontentlink"> [related content]</a></div>\n' % (chapterIndex+1, chapterIndex+1, bookData[book][chapterIndex]['name'], chapterIndex+1))

      fp.write('\n\n')

      for chapterIndex in range(len(bookData[book])):
            fp.write('<a name="chapter%s"><h2>Chapter %s</h2></a>\n' % (chapterIndex+1, chapterIndex+1))
            fp.write('<p><span>Read online:</span> <a href="chapter%s.html">Chapter %s - %s</a></p>\n' % (chapterIndex+1, chapterIndex+1, bookData[book][chapterIndex]['name']))

            if 'programs' in bookData[book][chapterIndex]:
                  for program in bookData[book][chapterIndex]['programs']:
                        fp.write("""<p><span>Download source:</span>  <a href="../source/%s">%s</a></p>

<p><span>Copy source to clipboard:</span><br />
<textarea style="width: 100%%; height:200px" id='src_%s'></textarea>
</p>

<p>Use the online diff tool to find typos in your code: <a href="diff/index.html?p=%s">%s</a></p>""" % (program, program, program[:-3], program[:-3], program))

            if 'downloads' in bookData[book][chapterIndex]:
                  fp.write('<p>Downloads:<br /><ul>\n')
                  for download in range(len(bookData[book][chapterIndex]['downloads'])):
                        fp.write('<li><a href="../resources/%s">%s</a></li>\n' % (bookData[book][chapterIndex]['downloads'][download], bookData[book][chapterIndex]['downloads'][download]))
                  fp.write('</ul></p>\n\n')

            if 'videos' in bookData[book][chapterIndex]:
                  fp.write('<p>Videos:<br /><ul>\n')
                  for video in range(len(bookData[book][chapterIndex]['videos'])):
                        fp.write('<li><a href="%s">%s</a></li>\n' % (bookData[book][chapterIndex]['videos'][video]['url'], bookData[book][chapterIndex]['videos'][video]['name']))
                  fp.write('</ul></p>\n\n')

            if 'links' in bookData[book][chapterIndex]:
                  for link in range(len(bookData[book][chapterIndex]['links'])):
                        fp.write('<li><a href="%s">%s</a></li>\n' % (bookData[book][chapterIndex]['links'][link]['url'], bookData[book][chapterIndex]['links'][video]['name']))
                  fp.write('</ul></p>\n\n')

      fp.write("""\n\n{% endblock %}""")
      fp.close()