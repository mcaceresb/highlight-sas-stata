Highlight SAS and Stata
=======================

SAS and Stata, while relatively simple to highlight, are not popular
enough to be part of most highlighting packages. I use them quite
extensively, however, and recently my RA work has required me
to document work that uses SAS and Stata. Since I like pretty
documentation, I have had to implement SAS and Stata highlghting in a
variety of places.

I should recommend @kylebarron's excellent
[language-stata](https://github.com/kylebarron/language-stata),
which implements very extensive Stata highlighting for Atom.  These
implementations are more basic.

Implementations
---------------

This repo contains SAS and Stata highlighting implementations for
- [Pygments](https://bitbucket.org/birkenfeld/pygments-main), a syntax highlighter written in python. I wrote this to use with [minted](https://github.com/gpoore/minted), a LaTeX code highlighter uses pygments.
- [Listings](http://tug.ctan.org/tex-archive/macros/latex/contrib/listings/), a LaTeX implementation of syntax highlighting.
- [Highlight.js](https://github.com/isagalaev/highlight.js), a syntax highlighter written in JavaScript. (SAS only; Stata was already available).

This project started with me using `listings` and `minted` from LaTeX. Since I code in `vim`, I also wrote a short script to highlight code in LaTeX using the appropriate `syntax/<lang>.vim`. See [here](https://github.com/mcaceresb/dotvim/tree/master/bundle/latex-fenced-languages).

### [Minted](https://github.com/gpoore/minted) and [Pygments](https://bitbucket.org/birkenfeld/pygments-main)

[Minted](https://github.com/gpoore/minted) is a LaTeX package that uses
[pygments](https://bitbucket.org/birkenfeld/pygments-main) to highlight
code. Pygments is quite complex and has a lot of options, but this means
highlighting here should be free of any issues. I added sas.py and
stata.py styles to match the SAS and Stata editors (styles are just a
list of types and colors, so defining them is quite easy).

The pull request was accepted into the main branch for pygments
2.2; you can try highlighting code on [the pygments project
website](http://pygments.org). However, @kylebarron has found some
mistakes which have been fixed in the latest version, along with some
improvements. To update, copy the lexer from this repo into your
`pygments` installation. For instance,
```bash
rootpypkg=`python -c "import site; print(site.getsitepackages()[0])"`
ls -sf $PWD/pygments/pygments/lexers/stata.py ${rootpypkg}/pygments/lexers/stata.py
```

### [Listings](http://tug.ctan.org/tex-archive/macros/latex/contrib/listings)

I used to use this before I discovered minted and pygments. Defining a
package is extremely hard because the implementation is in TeX and it
has all those limitations. I include it here because not everyone can or
wants to go through installing pygments, but the drawback is that there
will be highlighting quirks and errors I am unsure how to deal with.

To install, from a bash prompt
```bash
localtexmf=`kpsewhich -var-value=TEXMFHOME`/tex/latex/local
mkdir -p $localtexmf
cp -s $PWD/listings/lstsas.tex   $localtexmf/lstsas.tex
cp -s $PWD/listings/lststata.tex $localtexmf/lststata.tex
```

Now add this to your preamble
```tex
\input{lstsas}
\input{lststata}
```

### [Highlight.js](https://github.com/isagalaev/highlight.js)

This already had Stata support. I added SAS support only, mainly to use
with Redmine. Defining the languages was pretty simple, and it should be
mostly fine, but I don't think I have as fine-grained control as with
Pygments. I did add sas.css and stata.css styles to match the SAS and
Stata editors (styles are pretty straightforward CSS files).

I opened [a pull request](https://github.com/isagalaev/highlight.js/pull/1165)
that has recently been accepted.  To install, simply [install highlight.js](https://github.com/isagalaev/highlight.js).
