# MDTex to HTML

Convert markdown+latex to html+[mathjax](https://www.mathjax.org).

The script `mdtex-to-html.py` reads a file written in markdown+latex
and converts it to html+mathjax.
If an output path is specified, it writes the html file at that path.
Otherwise, it writes the html to a temporary file and opens that file in your browser.

## How to use

* Make sure you have python version 3.4 or above.
* Install python dependencies via pip: `pip install -r requirements.txt`.
* Run on input file: `./mdtex-to-html.py example.md`.

Run `./mdtex-to-html.py --help` for more options.

## Known issues

There is no provision on Windows to write to a temporary file and open that in browser.
On Windows, you must specify an output path.
If you know how to fix this, please send me a pull request.
