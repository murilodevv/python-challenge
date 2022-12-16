# PDF to Audio

# Requirements:
# pip install pyttsx3
# pip install PyPDF2

import pyttsx3, PyPDF2

pdf = PyPDF2.PdfFileReader(open('./text.pdf', 'rb'))
speaker = pyttsx3.init()

for page in range(pdf.numPages):
    text = pdf.getPage(page).extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()