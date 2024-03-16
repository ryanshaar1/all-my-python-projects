import os

def isFileCorrupted(file_path, expected_signature): #a function that getting a file_path, expected_signature of a type of file, and return True if the signature of the file that the method got is equal to the expected_signature
    try:
        with open(file_path, 'rb') as f:
            actual_signature = f.read(len(expected_signature))
            return actual_signature == expected_signature
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
    except Exception as e:
        print(f"Operation was not able to succeed, try again later: {e}")
        return False
def isTxtCorrupted(file_path):
    try:
        with open(file_path, 'rb') as f:
            file_content = f.read()

            for byte in file_content:
                if byte <32 or byte> 126:
                    return False
            else:
                return True
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
    except Exception as e:
        print(f"Operation was not able to succeed, try again later: {e}")
        return False

    







def scanFiles(directory, expected_signature_png, expected_signature_jpeg, expected_signature_gif1, expected_signature_gif2, expected_signature_pdf, expected_signature_zip, expected_signature_mp3 ):#a function that get a directory and expected_signature. the method scan each file that in the folder(if there is a folders inside the folder he scan to this folders too), and calling the isFileCorrupted method for each file. then print if the file is corrupted or not.
    for root, _, files in os.walk(directory):#לכל קובץ שנמצא בתיקייה כלשהי שנמצאת בתוך התיקייה הראשית תעשה את מה שבתוך ההזחה
        for file in files:
            file_path = os.path.join(root, file)#הדרך לקובץ שווה לדרך של הסיפרייה הראשית כאשר בתוך הספרייה הראשית נכנסים לספרייה הנוכחית בלולאה ואז לקובץ הנוכחי בלולאה 
            print(file_path)
            if isFileCorrupted(file_path, expected_signature_png):#check if png
                print("File is not corrupted")
            elif isFileCorrupted(file_path, expected_signature_jpeg):#check if jpeg
                print("File is not corrupted")
            elif isFileCorrupted(file_path, expected_signature_gif1):#check if gif1
                print("File is not corrupted")
            elif isFileCorrupted(file_path, expected_signature_gif2):#check if gif2
                print("File is not corrupted")
            elif isFileCorrupted(file_path, expected_signature_pdf):#check if pdf
                print("File is not corrupted")
            elif isFileCorrupted(file_path, expected_signature_zip):#check if zip
                print("File is not corrupted")
            elif isFileCorrupted(file_path, expected_signature_mp3):#check if mp3
                print("File is not corrupted")
            elif isTxtCorrupted(file_path):#check if txt
                print("File is not corrupted")
            else:
                print("File is definitely corrupted, seek for help")#file is corrupted

if __name__ == "__main__": #check if the script is being run as the main program
    specified_folder = r"C:\Users\Ryan\OneDrive\מסמכים\HTML\pythonLearning\python\images_testing"
    expected_signature_PNG = b"\x89PNG\r\n\x1a\n"
    expected_signature_JPEG = b"\xff\xd8"
    expected_signature_GIF1 = b"GIF87a"
    expected_signature_GIF2 = b"GIF89a"
    expected_signature_PDF = b"%PDF"
    expected_signature_ZIP = b"PK\x03\x04"
    expected_signature_MP3 = b"\x49\x44\x33"

    scanFiles(specified_folder, expected_signature_PNG, expected_signature_JPEG, expected_signature_GIF1, expected_signature_GIF2, expected_signature_PDF, expected_signature_ZIP, expected_signature_MP3)#calling for the functions



