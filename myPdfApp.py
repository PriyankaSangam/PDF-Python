import os
from werkzeug.utils import secure_filename
from flask import Flask,flash,request,redirect,send_file,render_template
from PyPDF2 import PdfFileReader, PdfFileWriter
import img2pdf

# UPLOAD_FOLDER = 'uploads/'
DOWNLOAD_FOLDER = 'downloads'

#app = Flask(__name__)
app = Flask(__name__, template_folder='templates')
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER


def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = "{}{}{}{}".format(name_of_split,"_",page,".pdf")
        output_path = os.path.join(app.config['DOWNLOAD_FOLDER'], output)
        with open(output_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    output_path = os.path.join(app.config['DOWNLOAD_FOLDER'], output)
    with open(output_path, 'wb') as out:
        pdf_writer.write(out)

def rotate_pages(pdf_path):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path)
    # Rotate page 90 degrees to the right
    page_1 = pdf_reader.getPage(0).rotateClockwise(90)
    pdf_writer.addPage(page_1)
    # Rotate page 90 degrees to the left
    # page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
    # pdf_writer.addPage(page_2)
    # Add a page in normal orientation
    # pdf_writer.addPage(pdf_reader.getPage(2))

    output_path = os.path.join(app.config['DOWNLOAD_FOLDER'], 'rotate_pages.pdf')
    with open(output_path, 'wb') as out:
        pdf_writer.write(out)

def img_convert(img_path):
    a4inpt = (img2pdf.mm_to_pt(215.9),img2pdf.mm_to_pt(279.4))
    layout_fun = img2pdf.get_layout_fun(a4inpt)

    output_path = os.path.join(app.config['DOWNLOAD_FOLDER'], 'image_convert.pdf')
    with open(output_path,"wb") as f:
	    f.write(img2pdf.convert(img_path, layout_fun=layout_fun))

        
@app.route('/', methods=['GET', 'POST'])
def myPDF():
    if request.method == 'POST':

        if request.form['submit_button'] == 'split':
            file2 = request.files['file2']
            if file2.filename == '':
                print('no filename')
                return redirect(request.url)
            else:
                split(file2,file2.filename)

        elif request.form['submit_button'] == 'merge':
            file3 = request.files.getlist("file3")
            if file3 == []:
                print('no files')
                return redirect(request.url)
            else:
                merge_pdfs(file3,"merged.pdf")

        elif request.form['submit_button'] == 'rotate':
            file4 = request.files['file4']
            if file4.filename == '':
                print('no filename')
                return redirect(request.url)
            else:
                rotate_pages(file4)
                #change rotate_pages function for 2 or more pages rotation

        elif request.form['submit_button'] == 'convert':
            file5 = request.files['file5']
            if file5.filename == '':
                print('no filename')
                return redirect(request.url)
            else:
                img_convert(file5)

        else:
            pass # unknown
   
    return render_template('base.html')  

if __name__ == "__main__":
    app.run()