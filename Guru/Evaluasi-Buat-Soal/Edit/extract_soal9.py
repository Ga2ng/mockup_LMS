with open('c:/DEV/design_mockup/Guru/Evaluasi-Buat-Soal/Edit/temp_edit.txt', 'r', encoding='utf-8') as f:
    content = f.read()

idx1 = content.find('<b>Soal #9</b>')
idx2 = content.find('<b>Soal #10</b>')
if idx1 != -1 and idx2 != -1:
    block = content[idx1:idx2]
    print(block)
else:
    print("Could not find boundaries.")
