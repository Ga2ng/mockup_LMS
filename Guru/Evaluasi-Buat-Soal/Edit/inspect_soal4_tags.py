with open('c:/DEV/design_mockup/Guru/Evaluasi-Buat-Soal/Edit/temp_edit.txt', 'r', encoding='utf-8') as f:
    content = f.read()

idx1 = content.find('<b>Soal #4</b>')
idx2 = content.find('<b>Soal #5</b>')
if idx1 != -1 and idx2 != -1:
    block = content[idx1:idx2]
    # Let's find all HTML tags: <input ...> or <select ...> or <textarea ...>
    import re
    tags = re.findall(r'<input[^>]*>|<select[^>]*>.*?</select>|<textarea[^>]*>.*?</textarea>', block, re.DOTALL)
    for tag in tags:
        # ignore raw_json textarea
        if 'raw_json' not in tag:
            print(tag)
else:
    print("Could not find boundaries.")
