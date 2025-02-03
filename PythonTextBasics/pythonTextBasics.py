import PyPDF2
import sys
sys.stdout.reconfigure(encoding='utf-8')
from  datetime import  datetime

# person = "John";
# print("my name is {}".format(person));
# print(f"my name is {person}");
# d = {'a':123, 'b':456};
# print(f"my number is {d['a']}");
# myList = ['john', 'joe', 'jim'];
# print(f"my name is {myList[0]}");
# library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)];
# print(library);
# for book in library:
#     print(f"author : {book[0]}");
# for author, topic, pages in library:
#     print(f"{author:{10}} {topic:{30}} {pages:>{10}}");

# from datetime import datetime;
# today = datetime(year=2025, month=2, day=1);
# print(f"{today:%B %d, %Y}");


# myfile = open('e:/NLP/text.txt', 'r')
# content = myfile.read()
# print(content)
# myfile.seek(0);
# myfile.close()

# myfile = open('e:/NLP/text.txt', 'w+')
# myfile = open('e:/NLP/text.txt', 'a+')
# contennt=myfile.write('my new text');
# print(contennt)
# myfile.close()

# myfile = open('e:/NLP/sample.pdf','rb')
# pdf_reader = PyPDF2.PdfReader(myfile)
# print(len(pdf_reader.pages))
# page_one = pdf_reader.pages[0]
# mytext=print(page_one.extract_text())
# myfile.close()

f = open('e:/NLP/sample.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f)
first_page = pdf_reader.pages[0]
pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(first_page)
pdf_output = open('e:/NLP/NewPDF.pdf','wb')
pdf_writer.write(pdf_output)
pdf_output.close()
f.close()

f = open('e:/NLP/PythonTextBasics/sample.pdf', 'rb')
pdf_text = []
pdf_reader = PyPDF2.PdfReader(f)
for num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[num]
    text = page.extract_text()
    pdf_text.append(text)
print(pdf_text)
f.close()
# this is just a commit command to execute 
