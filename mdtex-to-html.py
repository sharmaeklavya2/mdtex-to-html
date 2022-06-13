#!/usr/bin/env python3

"""Convert markdown+latex to html+mathjax"""

import sys
import os
from os.path import join as pjoin
import argparse
import platform
import subprocess

from markdown import Markdown
from jinja2 import Template
from tex_md_escape import tex_md_escape


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DEFAULT_TEMPLATE_PATH = pjoin(BASE_DIR, 'template.html')
DEFAULT_MATHJAX = 'https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js'


def read_file(fpath):
    with open(fpath) as fp:
        return fp.read()


def convert(md_text):
    return Markdown(extensions=['fenced_code']).convert(tex_md_escape(md_text))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('in_path', help='path to input file')
    parser.add_argument('-o', '--out', help='path to output file')
    parser.add_argument('--mathjax-url',
        help='URL of MathJax to use. Use empty string to omit including MathJax.')
    args = parser.parse_args()

    template = Template(read_file(DEFAULT_TEMPLATE_PATH))
    html_body = convert(read_file(args.in_path))
    if args.mathjax_url is None:
        args.mathjax_url = DEFAULT_MATHJAX
    html = template.render({'body': html_body, 'mathjax_url': args.mathjax_url})

    if args.out is not None:
        with open(args.out, 'w') as fp:
            fp.write(html)
    else:
        plat = platform.system()
        print('platform:', plat, file=sys.stderr)
        if plat.lower() in ('darwin', 'linux'):
            fpath = pjoin(os.environ['TMPDIR'], 'mdtex-to-html-output.html')
            with open(fpath, 'w') as fp:
                fp.write(html)
            print('output file:', file=sys.stderr)
            print(fpath)
            if plat.lower() in ('darwin',):
                subprocess.check_call(['open', fpath])
            if plat.lower() in ('linux',):
                subprocess.check_call(['xdg-open', fpath])
        else:
            raise Exception('out_path must be specified on platform ' + repr(plat))


if __name__ == '__main__':
    main()
