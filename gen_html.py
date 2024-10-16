#!/usr/bin/python3

from glob import glob
from jinja2 import Environment, FileSystemLoader
import os
from pathlib import Path

github_url="https://github.com/pwesterbaan/lander_lecture_notes/raw/main"

# change to directory containing this file
file_dir=os.path.dirname(os.path.realpath(__file__))
os.chdir(file_dir)

# prepare html template
environment = Environment(loader=FileSystemLoader(f"""{file_dir}/docs/"""))
template    = environment.get_template("annotated_notes_template.html")

# get directories for each set of class notes
directories=glob(os.path.join(file_dir,"*_NoteKeys"))
for dir_title in directories:
    noteKeys_dir=Path(dir_title).name
    ann_notes_dir=os.path.join(noteKeys_dir,"annotated_notes")

    # create annotated_notes directory if non-existent
    if not os.path.isdir(ann_notes_dir):
        os.makedirs(ann_notes_dir)

    print(f'''Generating {noteKeys_dir} list''')
    list_of_pdfs=os.listdir(ann_notes_dir)
    list_of_pdfs.sort()

    # generate list html
    notes_list=''.join([f'''<li><a href="{github_url}/{noteKeys_dir}/annotated_notes/{file}">{file}</li>
''' for file in list_of_pdfs])

    # use template to write file
    content=template.render(
        title=noteKeys_dir,
        notes_list=notes_list
    )
    filename=os.path.join(file_dir,"docs",f"""{noteKeys_dir[:8]}annotated_notes.html""")
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
print("done!")
