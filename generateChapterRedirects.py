#! python3
import os

# invent
for i in range(1, 21):
    fp = open(os.path.join('content', 'chapter%s' % i, 'index.html'), 'w')
    fp.write("""<html><head><meta http-equiv="refresh" content="0; url=/chapters/index.html#chapter%s"></head></html>""" % i)
    fp.close()

# pygame
for i in range(1, 10):
    fp = open(os.path.join('content', 'pygame', 'chapter%s' % i, 'index.html'), 'w')
    fp.write("""<html><head><meta http-equiv="refresh" content="0; url=/pygame/chapters/index.html#chapter%s"></head></html>""" % i)
    fp.close()

# hacking
for i in range(1, 25):
    fp = open(os.path.join('content', 'hacking', 'chapter%s' % i, 'index.html'), 'w')
    fp.write("""<html><head><meta http-equiv="refresh" content="0; url=/hacking/chapters/index.html#chapter%s"></head></html>""" % i)
    fp.close()
