with open('c:/DEV/design_mockup/Guru/Evaluasi-Buat-Soal/Edit/temp_edit.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's search inside the area of Soal #4 (index of "Soal #4" to "Soal #5")
idx1 = content.find('<b>Soal #4</b>')
idx2 = content.find('<b>Soal #5</b>')
if idx1 != -1 and idx2 != -1:
    block = content[idx1:idx2]
    # Find all inputs or checkboxes
    for line in block.split('\n'):
        if 'type="checkbox"' in line or 'name=' in line:
            if 'choices' not in line and 'raw_json' not in line and 'stem' not in line and 'q_remove' not in line:
                print(line)
else:
    print("Could not find block boundaries.")
