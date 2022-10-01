def getHoursMinutesSeconds(totalSeconds):
    # If totalSeconds is 0, just return '0s':
    if totalSeconds == ____:
        return ____

    # Set hours to how many times 3600 seconds can divide
    # totalSeconds. Then set totalSeconds to the remainder:
    if totalSeconds >= 3600:
        hours = totalSeconds // 3600
        totalSeconds = totalSeconds % 3600
    else:
        hours = 0

    # Set minutes to how many times 60 seconds can divide
    # totalSeconds. Then set totalSeconds to the remainder:
    if totalSeconds >= 60:
        minutes = totalSeconds // 60
        totalSeconds = totalSeconds % 60
    else:
        minutes = 0

    # Set seconds to the remaining totalSeconds value:
    seconds = ____

    # Create an hms list that contains the string hour/minute/second amounts:
    hms = []
    # If there are one or more hours, add the amount with an 'h' suffix:
    if hours > ____:
        ____.append(str(____) + 'h')
    # If there are one or more minutes, add the amount with an 'm' suffix:
    if minutes > 0:
        hms.append(____(minutes) + 'm')
    # If there are one or more seconds, add the amount with an 's' suffix:
    if seconds > 0:
        hms.append(str(seconds) + ____)

    # Join the hour/minute/second strings with a space in between them:
    return ' '.join(____)
