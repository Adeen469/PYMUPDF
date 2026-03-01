"""
Function: fitz.get_tessdata
Signature: get_tessdata(tessdata=None)
Description:
Detect Tesseract language support folder.

This function is used to enable OCR via Tesseract even if the language
support folder is not specified directly or in environment variable
TESSDATA_PREFIX.

* If <tessdata> is set we return it directly.

* Otherwise we return `os.environ['TESSDATA_PREFIX']` if set.

* Otherwise we search for a Tesseract installation and return its language
  support folder.

* Otherwise we raise an exception.
"""

import fitz

# Source code of fitz.get_tessdata:
def get_tessdata(tessdata=None):
    """Detect Tesseract language support folder.

    This function is used to enable OCR via Tesseract even if the language
    support folder is not specified directly or in environment variable
    TESSDATA_PREFIX.

    * If <tessdata> is set we return it directly.
    
    * Otherwise we return `os.environ['TESSDATA_PREFIX']` if set.
    
    * Otherwise we search for a Tesseract installation and return its language
      support folder.

    * Otherwise we raise an exception.
    """
    if tessdata:
        return tessdata
    tessdata = os.getenv("TESSDATA_PREFIX")
    if tessdata:  # use environment variable if set
        return tessdata

    # Try to locate the tesseract-ocr installation.
    
    import subprocess
    
    cp = subprocess.run('tesseract --list-langs', shell=1, capture_output=1, check=0, text=True)
    if cp.returncode == 0:
        m = re.search('List of available languages in "(.+)"', cp.stdout)
        if m:
            tessdata = m.group(1)
            return tessdata
    
    # Windows systems:
    if sys.platform == "win32":
        cp = subprocess.run("where tesseract", shell=1, capture_output=1, check=0, text=True)
        response = cp.stdout.strip()
        if cp.returncode or not response:
            raise RuntimeError("No tessdata specified and Tesseract is not installed")
        dirname = os.path.dirname(response)  # path of tesseract.exe
        tessdata = os.path.join(dirname, "tessdata")  # language support
        if os.path.exists(tessdata):  # all ok?
            return tessdata
        else:  # should not happen!
            raise RuntimeError("No tessdata specified and Tesseract installation has no {tessdata} folder")

    # Unix-like systems:
    attempts = list()
    for path in 'tesseract-ocr', 'tesseract':
        cp = subprocess.run(f'whereis {path}', shell=1, capture_output=1, check=0, text=True)
        if cp.returncode == 0:
            response = cp.stdout.strip().split()
            if len(response) == 2:
                # search tessdata in folder structure
                dirname = response[1]  # contains tesseract-ocr installation folder
                pattern = f"{dirname}/*/tessdata"
                attempts.append(pattern)
                tessdatas = glob.glob(pattern)
                tessdatas.sort()
                if tessdatas:
                    return tessdatas[-1]
    if attempts:
        text = 'No tessdata specified and no match for:\n'
        for attempt in attempts:
            text += f'    {attempt}'
        raise RuntimeError(text)
    else:
        raise RuntimeError('No tessdata specified and Tesseract is not installed')
