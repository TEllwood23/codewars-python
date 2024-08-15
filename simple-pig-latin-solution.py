def pig_it(text):
    print("!" in text)
    #remove exclamation mark
    no_excl = text.replace("!", "")
    no_ques = no_excl.replace("?", "")
    #split string into seperate words
    text_words = no_ques.split()
    # for each word, split the remaining letters, add the first letter to the end and then add "ay"
    new_list = []
    for word in text_words:
        new_list.append(word[1:] + word[0] + "ay")

    print("!" in text)

    if "!" in text:
        print("! seen")
        final_list = " ".join(new_list) + " !"
    elif "?" in text:
        final_list = " ".join(new_list) + " ?"
    else:
        final_list = " ".join(new_list)
    return final_list

# sentence = "Pig latin is cool!"
# print("!" in sentence)

# no_exl = "Pig latin is cool"
# print("!" in no_exl)

text = "O tempora o mores !"
print(pig_it(text))
