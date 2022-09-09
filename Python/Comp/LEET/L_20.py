def isvalid(s):
    queue = []
    for index, value in enumerate(s):
        if value in ['{', '[', '(']:
            queue.append(value)
        elif queue == []:
            return False
        elif queue[-1] in [chr(ord(value) - 2), chr(ord(value) - 1)]:
            queue = queue[:-1]
        else:
            return False
    return queue == []
