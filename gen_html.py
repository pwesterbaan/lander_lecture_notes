#!/usr/bin/python3

import os
from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("docs/"))
template = environment.get_template("annotated_notes_template.html")


#TODO: Generate this array automatically
class_note_dirs=[
    "math121_NoteKeys",
    "math211_NoteKeys"
    ]

for idx in range(len(class_note_dirs)):
    print(f"""{idx}: {class_note_dirs[idx]}""")

dir_idx=input("Select directory index: ")
dir_title=class_note_dirs[int(dir_idx)]
list_of_pdfs=os.listdir(f"""{dir_title}/annotated_notes/""")

notes_list=""
for file in list_of_pdfs:
    new_line=f'''<li><a href="https://github.com/pwesterbaan/lander_lecture_notes/raw/main/{dir_title}/annotated_notes/{file}">{file}</li>
'''
    notes_list+=new_line

#TODO: Generate html using a template and name below
# print(dir_title)
# print(notes_list)
content=template.render(
    title=dir_title,
    notes_list=notes_list
)
filename=f"""docs/{dir_title[:8]}annotated_notes.html"""
# print(filename)
with open(filename, mode="w", encoding="utf-8") as message:
    message.write(content)
print("done!")
