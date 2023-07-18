import magic
from rest_framework import serializers

def validate_file(file):
    allowed_formats = ['pdf', 'csv', 'docx',] # Allowed File Format
    max_file_size = 5*1024*1024 # maximum file size in bytes

    # check file format
    file_format = magic.from_buffer(file.read(), mime=True).split('/')[1]
    if file_format not in allowed_formats:
        raise serializers.ValidationError("Invalid file format")
    
    # check file size
    file.seek(0,2) # Move the file pointer to the end of the file
    file_size = file.tell() # Get the current position, which represents the file size
    file.seek(0) # Reset the file pointer to the beginning of the file
    if file_size > max_file_size:
        raise serializers.ValidationError("File too large. Please upload maximum 5MB file.")
    
    return file

def get_file_format(file):
    file.seek(0)  # Move the file pointer to the beginning
    file_format = magic.from_buffer(file.read(), mime=True).split('/')[1]
    file.seek(0)  # Reset the file pointer to the beginning
    return file_format
