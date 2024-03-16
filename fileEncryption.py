
def file_encryption_with_xor(input_file, output_file,  key):

    with open(input_file, 'rb') as f:
        data = f.read()
        f.close()
    

    encrypted_data = bytearray()
    
    for i in data:
        print(i)
        encrypted_byte = i ^ key  
        encrypted_data.append(encrypted_byte)

    with open(output_file, 'wb') as f_out:
        f_out.write(encrypted_data)
        f.close()




input_file = input("enter the path to the input file: ")
output_file = input("enter the path to the output file: ")
key = int(input("enter the encryption/decryption key"))

file_encryption_with_xor(input_file, output_file, key)