with open('c:/DEV/design_mockup/Guru/Evaluasi-Buat-Soal/Edit/temp_edit.txt', 'r', encoding='utf-8') as f:
    content = f.read()

idx1 = content.find('<b>Soal #4</b>')
idx2 = content.find('<b>Soal #5</b>')
if idx1 != -1 and idx2 != -1:
    block = content[idx1:idx2]
    # Find all instances of correct or kunci
    for line in block.split('\n'):
        if 'correct' in line or 'kunci' in line or 'ans' in line:
            print(line)
else:
    print("Could not find block boundaries.")
