chapters = [
'Introduction',
'Chapter 1 - Dealing with Errors and Asking for Help',
'Chapter 2 - Environment Setup and the Command Line',
'Chapter 3 - Code Formatting with Black',
'Chapter 4 - Choosing Understandable Names',
'Chapter 5 - Finding Code Smells',
'Chapter 6 - Writing Pythonic Code',
'Chapter 7 - Programming Jargon',
'Chapter 8 - Common Python Gotchas',
'Chapter 9 - Esoteric Python Oddities',
'Chapter 10 - Writing Effective Functions',
'Chapter 11 - Comments, Docstrings, and Type Hints',
'Chapter 12 - Organizing You Code Projects with Git',
'Chapter 13 - Measuring Performance and Big O Algorithm Analysis',
'Chapter 14 - Practice Projects',
'Chapter 15 - Object-Oriented Programming and Classes',
'Chapter 16 - Object-Oriented Programming and Inheritance',
'Chapter 17 - Python OOP: Properties and Dunder Methods',
]
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
# <a href="chapter%s.html">Prev: %s</a>
# <a href="chapter%s.html">Next: %s</a>
for i in range(18):
    with open('chapter' + str(i) + '.html', 'w', encoding='utf-8') as fo:
        with open('chapter' + str(i) + '.txt', encoding='utf-8') as chapterFile:
            chapterContent = chapterFile.read()
            if i == 0:
                prevNextHtml = '<a href="chapter%s.html">Next: %s</a>' % (i + 1, chapters[i + 1])
            elif i == 17:
                prevNextHtml = '<a href="chapter%s.html">Prev: %s</a>' % (i - 1, chapters[i - 1])
            else:
                prevNextHtml = '<a href="chapter%s.html">Prev: %s</a> | <a href="chapter%s.html">Next: %s</a>' % (i - 1, chapters[i - 1], i + 1, chapters[i + 1])

            fo.write(header % (chapters[i], prevNextHtml))
            fo.write('\n\n' + chapterContent + '\n\n\n')
            fo.write(footer % (prevNextHtml))

