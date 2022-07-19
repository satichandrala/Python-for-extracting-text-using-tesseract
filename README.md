
### NLP for daily tasks using Python
- The image, text.png is from a document of admission checklist by Sunny Jain
> Reference: Jain, S. (2021) ‘Admissions checklists (UK and USA) for parents and students. Created by Sunny Jain. Intellectual property of A&J Education ©.’ A and J Education, 124 City Road, London, EC1V 2NX www.aandjeducation.co.uk.
- I was trying to understand how to talk to a professor and saw this awesome document through his mailing list, but felt that it's too much of a manual task to extract the info, since there was an image of it.
- Hence I used the code to do that work for me.

### Code:

**Libraries Used**:
- OpenCV, Tesseract (you need to download tesseract, I used their github page, https://github.com/tesseract-ocr/tessdoc and downloaded the new 5.x, tesseract-ocr-w64-setup-v5.2.0.20220712.exe). 
- You can download whatever is new and stable at the time you use the code.

Main.ipynb is the jupyter notebook I used to write the code.
text.png is the image used for the analysis
recognize.txt is the result after processing the image through code.
