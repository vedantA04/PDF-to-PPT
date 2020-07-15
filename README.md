# PDF-to-PPT
A simple tool to convert PDFs to PPTs.

This tool automates the process of converting PDFs containing images to well formatted PPTs.

---

To install dependencies run:
```
pip3 install pdf2image && natsort && pptx && image
```
To use the tool:
```
python3 pdf2powerpoint.py
```

---

**For Windows:**

You need to install poppler as well. You can install it from [here](http://blog.alivate.com.au/poppler-windows/ "Poppler Installation Link").

After installation you need to add poppler to PATH.

Extract the downloaded file, _poppler-0.68.0_x86.7z_ into ```C:\Program Files```. The directory structure should look something like this:
```
C:
    └ Program Files
        └ poppler-0.68.0_x86
            └ bin
            └ include
            └ lib
            └ share
```
Add ```C:\Program Files\poppler-0.68.0_x86\bin``` to your system PATH by doing the following: 

Click on the Windows start button, search for **Edit the system environment variables**, click on **Environment Variables...**, under **System variables**, double-click on **Path**, click on **New**, then paste ```C:\Program Files\poppler-0.68.0_x86\bin``` in the text box formed and click OK.

Reopen your terminal.

---

**For Linux/Mac:**

Poppler is pre-installed.
