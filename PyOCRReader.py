
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract, sys, os, getopt

def PyOCRReader(file): #use pytesseract to convert find strings in the image
    text = pytesseract.image_to_string(Image.open(file))
    return text

def main(argv):

    #Script only takes two agruments, the directory with the images, and the text output file
    if len(sys.argv) > 3: 
        print('Usage: PyOCRReader.py <directory> <output file>')
        sys.exit()
    elif len(sys.argv) is 1:
        print('Usage: PyOCRReader.py <directory> <output file>')
        sys.exit()

    directory = sys.argv[1]
    outputfile = sys.argv[2]

    #Loop through every jpg and png in the directory and send the file names to the ocr function, then append the result to the outputfile
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            imgfile = os.path.join(directory, filename)

            with open(outputfile, 'a') as f:
                sys.stdout = f #Set standard out to the output file
                print(PyOCRReader(imgfile))
        else:
            continue

if __name__ == "__main__":
   main(sys.argv[1:])