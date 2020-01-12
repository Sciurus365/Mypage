Title: The Cooperation of LaTeX and Word Users: latex2rtf and difflatex
Date: 2018-7-22 17:00
Tags: LaTeX

Recently, I am cooperating with a colleague in my research group to modify a thesis. The original document is written in .Rnw file (R+LaTeX), while this colleague of mine likes to use Word. I found two software useful in this process.

The first one is [latex2rtf](https://sourceforge.net/projects/latex2rtf/). This tool can convert LaTeX file to .rtf file. Its advantage comparing with pandoc is that the in-text citation can be converted correctly. However, it cannot handle reference lists, pictures and charts. 

The second one is [difflatex](http://www.ctan.org/tex-archive/support/latexdiff/) written in [Perl](http://www.perl.org/). It is a package included in [TeXLive](http://tug.org/texlive/). You can use the following commend

```shell
difflatex old.tex new.tex >diff.tex
```

and compile diff.tex. The output format is fairly good.