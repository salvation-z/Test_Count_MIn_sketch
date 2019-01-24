import sys
import subprocess
import pdfkit
path_wk = r'D:\programs\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf = path_wk)
inputfile = sys.argv[1].replace(" ","\ ")
temp_html = inputfile[0:inputfile.rfind('.')]+'.html'
command = 'jupyter nbconvert --to html ' + inputfile
subprocess.call(command,shell=True)
print('============success===========')
output_file =inputfile[0:inputfile.rfind('.')]+'.pdf'
pdfkit.from_file(temp_html,output_file,configuration=config)
subprocess.call('rm '+temp_html,shell=True)