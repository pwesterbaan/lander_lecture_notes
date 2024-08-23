#!/usr/bin/python3

import os
from jinja2 import Environment, FileSystemLoader
from glob import glob

environment = Environment(loader=FileSystemLoader("docs/"))
template = environment.get_template("annotated_notes_template.html")
github_url="https://github.com/pwesterbaan/lander_lecture_notes/raw/main"

directories=glob("*_NoteKeys")
directories.sort()
for dir_title in directories:
    # print(f'''Generating {dir_title} list''')
    list_of_pdfs=os.listdir(f"""{dir_title}/annotated_notes/""")
    list_of_pdfs.sort()
    print(list_of_pdfs)

    notes_list=''.join([f'''<li><a href="{github_url}/{dir_title}/annotated_notes/{file}">{file}</li>
''' for file in list_of_pdfs])

    content=template.render(
        title=dir_title,
        notes_list=notes_list
    )
    filename=f"""docs/{dir_title[:8]}annotated_notes.html"""
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
print("done!")
