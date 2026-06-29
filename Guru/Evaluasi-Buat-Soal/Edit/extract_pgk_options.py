with open('c:/DEV/design_mockup/Guru/Evaluasi-Buat-Soal/Edit/temp_edit.txt', 'r', encoding='utf-8') as f:
    content = f.read()

idx1 = content.find('name="edit_items[4][choices][A]"')
if idx1 != -1:
    print(content[idx1-500:idx1+1500])
else:
    print("Could not find PGK options block.")
