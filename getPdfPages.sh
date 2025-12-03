#!/usr/bin/env bash
# script used to feed numbers into pdftk based on section name of notes
#TODO: auto complete in .bashrc
#TODO: make help message


toc="Table Of Contents"  # Ignore page numbers for TOC

#TODO: Unnecessary when checking $#
# Default to all pdfs
# fname=${2:- *.pdf}
# echo fname: $fname

# args: pattern filename output
# eg:   ./getPdfPages.sh 6.5: math123Notes.pdf math123_NoteKeys/math123Notes_6p5.pdf
pattern=$1
fname=$2
output=$3

if [ "$#" -ne 3 ]; then
    echo Args: \"pattern\" \"fname\" \"output\"
    if [ "$#" -eq 2 ]; then
	# Print matching page range
	pages=$(comm -23 \
            <(pdfgrep --page-number --no-filename --cache --fixed-strings "$pattern" $fname | cut -d: -f1 | sort -u) \
            <(pdfgrep --page-number --no-filename --cache --fixed-strings "$toc" $fname | cut -d: -f1 | sort -u ))
	echo $(echo "$pages" | head -n1)-$(echo "$pages" | tail -n1)
    fi
else
    # Find pages in $fname containing $pattern, but not containing $toc
    # use the matching, unique, pages in pdftk to create the file $output
    pdftk $fname cat $(comm -23 \
        <(pdfgrep --page-number --no-filename --cache --fixed-strings "$pattern" $fname | cut -d: -f1 | sort -u) \
        <(pdfgrep --page-number --no-filename --cache --fixed-strings "$toc" $fname | cut -d: -f1 | sort -u ) | tr '\n' ' ') output $output
fi
