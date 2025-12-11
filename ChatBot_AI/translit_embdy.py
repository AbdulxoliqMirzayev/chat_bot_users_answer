# Lotin ↔ Kirill o‘tkazuvchi modul

latin_map = {
    "a": "а", "b": "б", "d": "д", "e": "е", "f": "ф", "g": "г", "h": "ҳ",
    "i": "и", "j": "ж", "k": "к", "l": "л", "m": "м", "n": "н", "o": "о",
    "p": "п", "q": "қ", "r": "р", "s": "с", "t": "т", "u": "у", "v": "в",
    "x": "х", "y": "й", "z": "з",

    "sh": "ш",
    "ch": "ч",
    "ng": "нг",
    "o‘": "ў",
    "g‘": "ғ",
    "ʼ": "ъ",
}
cyrillic_map = {v: k for k, v in latin_map.items()}

def latin_to_cyrillic(text):
    text = text.lower()
    result = ""

    i = 0
    while i < len(text):
        
        if text[i:i+2] in latin_map:
            result += latin_map[text[i:i+2]]
            i += 2
        elif text[i] in latin_map:
            result += latin_map[text[i]]
            i += 1
        else:
            result += text[i]
            i += 1

    return result


def cyrillic_to_latin(text):
    result = ""

    i = 0
    while i < len(text):
        
        if text[i:i+2] in cyrillic_map:
            result += cyrillic_map[text[i:i+2]]
            i += 2
        elif text[i] in cyrillic_map:
            result += cyrillic_map[text[i]]
            i += 1
        else:
            result += text[i]
            i += 1

    return result
