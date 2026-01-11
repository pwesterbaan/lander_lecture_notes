# Lander Lecture Notes
This repository contains notes to be used while lecturing at Lander University.

The main files are `math???Notes.{pdf,tex}` which inherit their styling from `mathNotesPreamble.tex`. The `subfile` package is used to import each section's source file, contained in the `subfiles` directory, into the main `math???Notes.tex` file.

* [math121Notes.pdf](https://github.com/pwesterbaan/lander_lecture_notes/raw/main/math121Notes.pdf)
* [math123Notes.pdf](https://github.com/pwesterbaan/lander_lecture_notes/raw/main/math123Notes.pdf)
* [math125Notes.pdf](https://github.com/pwesterbaan/lander_lecture_notes/raw/main/math125Notes.pdf)
* [math211Notes.pdf](https://github.com/pwesterbaan/lander_lecture_notes/raw/main/math211Notes.pdf)

The included preamble files contain packages and macros needed to compile:

* [texPreamble.sty](https://github.com/pwesterbaan/scripts/blob/master/texmf/tex/latex/local/texPreamble.sty)
* [texShortcutsWesterbaan.tex](https://github.com/pwesterbaan/scripts/blob/master/texmf/tex/latex/local/texShortcutsWesterbaan.tex)
* [colorPalette.sty](https://github.com/pwesterbaan/scripts/blob/master/texmf/tex/latex/local/colorPalette.sty)

Note:

* Compiling using the option ```--shell-escape``` takes advantage of the *Externalization Library* provided by Ti*k*Z which converts each image into a separate PDF (located in the ```\images``` folder).
* A standard free Overleaf account times out before this project finishes compiling, but individual sections can be compiled by including the ```mathNotesPreamble.tex``` file as a symlink or by placing it in the same directory/folder.