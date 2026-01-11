#!/usr/bin/env python

import datetime
import posixpath
from pathlib import Path
from urllib.parse import urljoin

import pandas as pd
from jinja2 import Environment, FileSystemLoader

github_url="https://github.com/pwesterbaan/lander_lecture_notes/raw/main"
# Default future date when no release date given
future_date=datetime.datetime(3000,1,1,13,0,0).isoformat()

# change to directory containing this file
file_dir = Path(__file__).resolve().parent

# prepare html template
environment = Environment(loader=FileSystemLoader(f"""{file_dir}/docs/"""))
template    = environment.get_template("index_template.md")

list_of_class_dicts=[]
# get directories for each set of class notes
directories = sorted(file_dir.glob("*_NoteKeys"))
for dir_path in directories:
    info_dict={}

    noteKeys_dir=dir_path.name
    print(f'''Generating {noteKeys_dir} list''')

    class_name=noteKeys_dir.split('_')[0]
    info_dict['name']=class_name
    info_dict['file_name']=class_name+"Notes.pdf"
    info_dict['list_id']=class_name+"_NoteKeys"

    annotated_notes_dir=dir_path / "annotated_notes"
    # create annotated_notes directory if non-existent
    annotated_notes_dir.mkdir(parents=True,exist_ok=True)

    release_date_csv_file=dir_path / f'''{class_name}_releaseDates.csv'''
    if release_date_csv_file.is_file():
        # Create dictionary from csv with release dates for each section of notes
        df = pd.read_csv(release_date_csv_file)
        df=df.fillna(future_date) # Handles missing dates
        info_dict['release_date']=dict(zip(df['filename'],df['release date']))
    else:
        print(f'''{release_date_csv_file:=} does not exist yet!''')

    # Create list of annotated notes pdfs sorted alphabetically then by release date
    list_of_pdfs=[file.name for file in annotated_notes_dir.iterdir() if file.suffix=='.pdf']
    list_of_pdfs.sort()
    list_of_pdfs=sorted(list_of_pdfs,key=lambda x: info_dict.get('release_date',{}).get(x,future_date))
    info_dict['list_of_pdfs']=list_of_pdfs

    info_dict['base_url']=urljoin(github_url,posixpath.join(noteKeys_dir,"annotated_notes"))

    list_of_class_dicts.append(info_dict)

# use template to write file
content=template.render(list_of_class_dicts=list_of_class_dicts)

filename=file_dir / "docs" / "index.md"
with open(filename, mode="w", encoding="utf-8") as message:
    message.write(content)
print("done!")
