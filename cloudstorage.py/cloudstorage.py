from os import access
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

    def main():
      
        access_token ='sl.A6tEEzJalNlqxjS8a7GSvLYBUK5JKHBODPbx5VTxYRAs0lGkegpS28rpoz5iWVAqk75xYDG70fO4SgbD2wnpXqzvJb2MuXjzwRIoAdDc1yuS4I6LI1vV-Q7TQwPiZ0HYIrI3qmo'
        transferData = TransferData(access_token)

        file_from = input('Enter The File Path To Transfer:-')
        file_to = input('Enter The Full Path To Upload To DropBox :-')

        transferData.upload_file(file_from,file_to)
        print('File Has Been Moved !!!')


    main()
    