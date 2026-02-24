#!/usr/bin/env bash
# script used to feed numbers into pdftk based on section name of notes
#TODO: (multiple) auto complete in .bashrc

toc="Table Of Contents"  # Ignore page numbers for TOC

# args: pattern filename output
# eg:   ./getPdfPages.sh 6.5: math123Notes.pdf math123_NoteKeys/math123Notes_6p5.pdf
pattern=$1
fname=$2
output=$3

#TODO: make help message
#https://www.howtogeek.com/beginner-friendly-ways-to-level-up-your-bash-scripts/
_help() {
  cat <<EOF
Usage: $(basename "$0") [OPTIONS] \"pattern\" \"fname\" \"output\"

OPTIONS
  -h     display this help menu
EOF
}

while getopts "hd" opt; do
    case "$opt" in
	h)
	    _help
	    exit 0
	    ;;
	d)
	    set -x #enable debug
	    ;;
    esac
done
#TODO remove flags from position variables

# Print matching page range
pages=$(comm -23 --nocheck-order \
             <(pdfgrep --page-number --no-filename --cache --fixed-strings "$pattern" $fname | cut -d: -f1 | sort --numeric --unique) \
             <(pdfgrep --page-number --no-filename --cache --fixed-strings "$toc" $fname | cut -d: -f1 | sort --unique ))

# check if $pages is empty
if [ ! -z "$pages" ]; then
    # Check if $output undefined
    if [ ! -n "$output" ]; then
	#TODO: Autocomplete for filenames
	echo $(echo "$pages" | head -n1)-$(echo "$pages" | tail -n1)
	read -p "Specify output file? " output
    fi

    # Check if $output defined now
    if [ -n "$output" ]; then
	# echo output: $output
	pdftk $fname cat $pages output $output
    fi
else
    echo "Empty page range!"
fi
