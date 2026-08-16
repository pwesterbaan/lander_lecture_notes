%.pdf: %.tex
	# pdflatex --shell-escape $<
	latexmk -pdf --shell-escape $<

clean:
	@latexmk -c
