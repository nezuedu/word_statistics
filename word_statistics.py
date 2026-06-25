def word_statistics(string: str) -> dict:
    """
    Function which can determine how many times a word is seen in the same string value.
    :param string:Any input text.
    :return: Dictionary which contains words from the input text as keys and their count inside the text as their values
    """

    string = string.lower()
    dic = {}
    for sym in ",.;:'\"?!-()[]{}1234567890":
        string = string.replace(sym, "")
    for word in string.split():
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic
