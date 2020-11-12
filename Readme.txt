PDF-Python

Steps on how to use this project:
1.	Download this repository (PDF-Python) and save it at any location on your computer.
2.	Install Python 2.7 or Python 3
3.	Go to the PDF-Python folder and create a virtual environment of Python 
4.	To create virtual environment on Windows. Open PowerShell. Change directory to the PDF-Python. Use this command “python -m venv pdf_env” to create venv in the PDF-Python folder like the following:
PS C:\Users\Username\Path\PDF-Python > python -m venv pdf_env

Do the following in powershell:
PS C:\Users\Username\Path\PDF-Python > cd pdf_env
PS C:\Users\Username\Path\PDF-Python\pdf_env > cd scripts
PS C:\Users\Username\Path\PDF-Python\pdf_env\scripts > ./activate 
Now the virtual env is activated 
(pdf_env) PS C:\Users\Username\Path\PDF-Python\pdf_env\scripts > 
Once activated use command “cd..” twice to go to PDF-Python path
(pdf_env) PS C:\Users\Username\Path\PDF-Python > 

Install the required packages: Flask, PyPDF2 and img2pdf:
(pdf_env) PS C:\Users\Username\Path\PDF-Python > pip install Flask
(pdf_env) PS C:\Users\Username\Path\PDF-Python > pip install PyPDF2
(pdf_env) PS C:\Users\Username\Path\PDF-Python > pip install img2pdf

To run the app:
(pdf_env) PS C:\Users\Username\Path\PDF-Python > $env:FLASK_APP = "myPdfApp.py"
(pdf_env) PS C:\Users\Username\Path\PDF-Python > $env:FLASK_ENV = "development"
(pdf_env) PS C:\Users\Username\Path\PDF-Python > flask run

When the app runs successfully copy the link http://127.0.0.1:5000/ in browser.
You use the app to split, merge, rotate or convert images to pdf.
All the files will be automatically downloaded in the “downloads” folder within the PDF-Python folder.
