def is_isogram(string):
    if string == "":
        return True
    else:
        set_string= set(string.lower())
        string=string.lower()
        if (len(set_string)==len(string)):
            return True
        else:
            return False
