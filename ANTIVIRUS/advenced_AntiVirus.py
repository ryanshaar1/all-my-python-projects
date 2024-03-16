import os
import magic

def is_file_corrupted(file_path):
    try:
        # Create a magic instance
        magic_instance = magic.Magic()#יצירת משתנה מסוג magic 

        
        with open(file_path, 'rb') as file:#(אולי לעשות בדיקה אם הסוג קובץ תואם לסוג מידע שבתוכו)
            file_type = magic_instance.from_buffer(file.read())#קובע את סוג הקובץ על סמך התוכן שלו

        # Print the identified file type
        print(f"The file at '{file_path}' is identified as: {file_type}")

        
        if file_type == "" or "unknown" in file_type.lower() or "undefined" in file_type.lower():
            return True
        else:
            return False
        
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
    except Exception as e:
        print(f"Error occurred while checking file: {e}")
        return False



def scan_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if is_file_corrupted(file_path):
                print(f"File '{file_path}' is corrupted.")
            else:
                print(f"File '{file_path}' is not corrupted.")

if __name__ == "__main__":
    specified_folder = r"C:\Users\Ryan\OneDrive\מסמכים\HTML\pythonLearning\python\images_testing"
    scan_files(specified_folder)
