def pig_it(text):
    #split string into seperate words
    text_words=text.split()
    # for each word, split the remaining letters, add the first letter to the end and then add "ay"
    new_list = []
    for word in text_words:
        new_list.append(word[1:] + word[0] + "ay")

    return new_list


print(" ".join(pig_it('Pig latin is cool')))
