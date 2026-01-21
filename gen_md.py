#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "datetime>=6.0",
#     "jinja2>=3.1.6",
#     "pandas>=3.0.0",
#     "pathlib>=1.0.1",
# ]
# ///

from datetime import datetime
import posixpath
from pathlib import Path
from urllib.parse import urljoin

import pandas as pd
from jinja2 import Environment, FileSystemLoader

github_url="https://github.com/pwesterbaan/lander_lecture_notes/raw/main"
# Default future date when no release date given
future_date=datetime(3000,1,1,13,0,0).isoformat()

# change to directory containing this file
working_dir = Path(__file__).resolve().parent

# prepare html template
environment = Environment(loader=FileSystemLoader(working_dir))
template    = environment.get_template("index_template.jinja2")

list_of_class_dicts=[]
# get directories for each set of class notes
directories = sorted(working_dir.glob("*_NoteKeys"))
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
        release_dates=dict(zip(df['filename'],df['release date']))
        info_dict['release_date']=release_dates
    else:
        print(f'''{release_date_csv_file:=} does not exist yet!''')

    # Create list of annotated notes pdfs sorted alphabetically then by release date
    list_of_pdfs=[pdf.name for pdf in annotated_notes_dir.iterdir() if pdf.suffix=='.pdf']
    # Verify each pdf has a release date. Default to future otherwise
    for filename in list_of_pdfs:
        if filename not in release_dates:
            print(f'''\t****{filename} not listed in {release_date_csv_file}****''')
            release_dates[filename]=future_date
            info_dict['release_date']=release_dates

    list_of_pdfs.sort()
    list_of_pdfs=sorted(list_of_pdfs,key=lambda x: info_dict.get('release_date',{}).get(x,future_date))
    info_dict['list_of_pdfs']=list_of_pdfs

    info_dict['base_url']=urljoin(github_url,posixpath.join(noteKeys_dir,"annotated_notes"))

    list_of_class_dicts.append(info_dict)

# use template to write file
kwargs={}
kwargs['list_of_class_dicts']=list_of_class_dicts
kwargs['today_str']=datetime.now().strftime('%Y-%m-%d %H:%M')
content=template.render(**kwargs)

filename=working_dir / "docs" / "index.md"
with open(filename, mode="w", encoding="utf-8") as message:
    message.write(content)
print("done!")
