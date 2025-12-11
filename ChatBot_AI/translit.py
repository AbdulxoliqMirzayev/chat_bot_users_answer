# bu bo'limda lotincha matnni kirillga o'zgartirish funksiyasini yozib olamiz

def latin_to_cyr(text):
    rules = [
        ("o‘","ў"), ("O‘","Ў"), ("o'","ў"), ("O'","Ў"),
        ("g‘","ғ"), ("G‘","Ғ"), ("g'","ғ"), ("G'","Ғ"),
        ("sh","ш"), ("Sh","Ш"), ("SH","Ш"),
        ("ch","ч"), ("Ch","Ч"), ("CH","Ч"),
        ("yu","ю"), ("Yu","Ю"), ("YU","Ю"),
        ("ya","я"), ("Ya","Я"), ("YA","Я"),
        ("yo","ё"), ("Yo","Ё"), ("YO","Ё"),
        ("ts","ц"), ("Ts","Ц"), ("TS","Ц"),
    ]

    # Katta kombinatsiyalarni almashtiramiz
    for latin, cyr in rules:
        text = text.replace(latin, cyr)

    
    single = {
        'a': 'а', 'b': 'б', 'd': 'д', 'e': 'е', 'f': 'ф', 'g': 'г',
        'h': 'ҳ', 'i': 'и', 'j': 'ж', 'k': 'к', 'l': 'л', 'm': 'м',
        'n': 'н', 'o': 'о', 'p': 'п', 'q': 'қ', 'r': 'р', 's': 'с',
        't': 'т', 'u': 'у', 'v': 'в', 'x': 'х', 'y': 'й', 'z': 'з',
        'A': 'А','B': 'Б','D': 'Д','E': 'Е','F': 'Ф','G': 'Г',
        'H': 'Ҳ','I': 'И','J': 'Ж','K': 'К','L': 'Л','M': 'М',
        'N': 'Н','O': 'О','P': 'П','Q': 'Қ','R': 'Р','S': 'С',
        'T': 'Т','U': 'У','V': 'В','X': 'Х','Y': 'Й','Z': 'З',
    }

    result = ""
    for ch in text:
        result += single.get(ch, ch)

    return result
