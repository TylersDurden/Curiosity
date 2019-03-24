import os, sys


def create_simple_latex_pdf(text_data,link, filename):
    Latex_PDF = '\\documentclass[12pt]{article}\n' \
                "\usepackage{hyperref}\n\\usepackage{graphicx}\n" \
                "\\begin{document}\n" \
                "\centering\n" +\
                text_data+"\n\linebreak\n"\
                "\href{"+link+"}{Click It}\n\end{document}"

    # Save as f.tex and then pdflatex > f.pdf
    texname = filename+'.tex'
    open(texname, 'w').write(Latex_PDF)
    os.system('pdflatex -quiet '+filename+'.tex > /dev/null 2>&1')
    os.system('rm dummy.log dummy.aux dummy.tex dummy.out')


def bare_bones_pdf(filename):
    pdf_hak = '%PDF-1.0\n' \
              '1 0 obj<</Type/Catalog/Pages 2 0 R>>' \
              'endobj' \
              '2 0 obj<</Type/Pages/Kids[3 0 R]/Count 1>>' \
              'endobj' \
              '3 0 obj<</Type/Page/MediaBox[0 0 3 3]>>' \
              'endobj' \
              'trailer<</Size 5/Root 1 0 R>>'
    open(filename, 'w').write(pdf_hak)


def main():
    if '-latex' in sys.argv:
        link = 'https://github.com/TylersDurden/Audio-Visual/raw/master/Video/tre.mp4'
        create_simple_latex_pdf('Hey There Neighbor.', link, 'dummy')
    if '-blank' in sys.argv:
        bare_bones_pdf('dummy.pdf')
    # EOF


if __name__ == '__main__':
    main()
