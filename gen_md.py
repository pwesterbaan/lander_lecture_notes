#!/usr/bin/python3

from glob import glob
from jinja2 import Environment, FileSystemLoader
import os
import pandas as pd
from pathlib import Path

github_url="https://github.com/pwesterbaan/lander_lecture_notes/raw/main"
#Default future date when no release date given
future_date='2500-01-01T13:00:00'

# change to directory containing this file
file_dir=os.path.dirname(os.path.realpath(__file__))
os.chdir(file_dir)

# prepare html template
environment = Environment(loader=FileSystemLoader(f"""{file_dir}/docs/"""))
template    = environment.get_template("index_template.md")

list_of_class_dicts=[]
# get directories for each set of class notes
directories=glob(os.path.join(file_dir,"*_NoteKeys"))
directories.sort()
for dir_title in directories:
    info_dict={}
    noteKeys_dir=Path(dir_title).name
    annotated_notes_dir=os.path.join(noteKeys_dir,"annotated_notes")
    class_name=noteKeys_dir.split('_')[0]
    info_dict['name']=class_name
    info_dict['file_name']=class_name+"Notes.pdf"
    info_dict['list_id']=class_name+"_NoteKeys"

    # create annotated_notes directory if non-existent
    if not os.path.isdir(annotated_notes_dir):
        os.makedirs(annotated_notes_dir)

    # Create dictionary from csv with release dates for each section
    df = pd.read_csv(f'''{noteKeys_dir}/{class_name}_releaseDates.csv''')
    info_dict['release_date']=dict(zip(df['filename'],df['release date']))

    print(f'''Generating {noteKeys_dir} list''')
    list_of_pdfs=os.listdir(annotated_notes_dir)
    # Sort alphabetically first
    list_of_pdfs.sort()
    # Sort by release date
    list_of_pdfs=sorted(list_of_pdfs,key=lambda x: info_dict.get('release_date').get(x,future_date))
    info_dict['list_of_pdfs']=list_of_pdfs
    info_dict['base_url']=f'''{github_url}/{noteKeys_dir}/annotated_notes/'''

    list_of_class_dicts.append(info_dict)

# use template to write file
content=template.render(list_of_class_dicts=list_of_class_dicts)

filename=os.path.join(file_dir,"docs","index.md")
with open(filename, mode="w", encoding="utf-8") as message:
    message.write(content)
print("done!")
