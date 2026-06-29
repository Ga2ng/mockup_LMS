with open('c:/DEV/design_mockup/Guru/Evaluasi-Buat-Soal/Edit/temp_edit.txt', 'r', encoding='utf-8') as f:
    content = f.read()

idx1 = content.find('<b>Soal #7</b>')
idx2 = content.find('<b>Soal #8</b>')
if idx1 != -1 and idx2 != -1:
    block = content[idx1:idx2]
    import re
    tags = re.findall(r'<input[^>]*>|<select[^>]*>.*?</select>|<textarea[^>]*>.*?</textarea>', block, re.DOTALL)
    for tag in tags:
        if 'raw_json' not in tag:
            print(tag)
else:
    print("Could not find boundaries.")
