# https://codelearn.io/training/detail/45172
def teeNine(message):
    key2char = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9:'wxyz'}
    char2key = {v:key for key, val in key2char.items() for v in val}
    
    message = message.lower()
    out = []
    last_key = -1
    repeat = 0
    
    for char in message:
        if not char.isalpha():
            if last_key != -1:
                out.append(key2char[last_key][(repeat-1) % len(key2char[last_key])])
                last_key = -1
                repeat = 0
            out.append(char)
        else:
            key = char2key[char]
            if key == last_key:
                repeat += 1
            else:
                if last_key != -1:
                    out.append(key2char[last_key][(repeat-1) % len(key2char[last_key])])
                last_key = key
                repeat = 1
    
    if last_key != -1:
        out.append(key2char[last_key][(repeat-1) % len(key2char[last_key])])
    
    return ''.join(out)
