

'''LevensteinLength prints out length of Levenstein between two wards.
Also can modify words by followng simple instructions,
turn one word into another whilst printing the instructions it followed to do that'''

def get_levenshtein_distance(first_word: str, second_word: str) -> int:
    return recurse(len(first_word), len(second_word), first_word, second_word)

def recurse(len_fw, len_sw, first_word, second_word):
        if len_fw == 0 or len_sw == 0:
            return max(len_fw, len_sw)
        elif first_word [len_fw - 1] == second_word [len_sw - 1]:
            return recurse(len_fw - 1, len_sw - 1, first_word, second_word)
        else:
            return 1 + min(
                recurse(len_fw, len_sw - 1, first_word, second_word),
                recurse(len_fw - 1, len_sw, first_word, second_word),
                recurse(len_fw - 1, len_sw - 1, first_word, second_word)
                )

def modify_word(first_word: str, edit_actions: str, letters: str) -> str:
    ans = first_word
    ans_list = []
    for i in ans:
        ans_list.append(i)
    el_num_in_word = el_num_in_letters = 0
    for func in edit_actions:
        if func == "R":
            ans_list[el_num_in_word] = letters[el_num_in_letters]
            el_num_in_letters += 1
        elif func == "I":
            ans_list.insert(el_num_in_word, letters[el_num_in_letters])
            el_num_in_letters += 1
        elif func == "D":
            del ans_list[el_num_in_word]
            el_num_in_word -= 1
        el_num_in_word += 1
    return ''.join(ans_list)