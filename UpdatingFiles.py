import dropbox
import os

from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFiles(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(file_to, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
        with open(file_from, "rb") as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'H5MlzHMkbDEAAAAAAAAAAZoEZ2CNGMgVP51oUy1i27ER_5p_i-XTNlGT5o4Fw-sY'
    transferData = TransferData(access_token)
    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the destination file: ")
    transferData.uploadFiles(file_from, file_to)

    print("File has been moved!")

main()