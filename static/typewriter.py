import sys, random, time

def slowPrint(message, end='\n'):
    for c in message:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.randint(40, 100)/ 1000)
    sys.stdout.write(end)
