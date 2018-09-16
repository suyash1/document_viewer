from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from config import DevelopmentConfig

gauth = GoogleAuth()

gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

class GoogleDriveUtil(object):
    def __init__(self):
        self.gauth = GoogleAuth()
        self.gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(self.gauth)
    
    def create_folder(self, folder_name):
        '''
        creating folder in top level directory, i.e., root for now
        TODO: extension for subdirectories
        '''
        folder_metadata = {
            'title' : folder_name,
            # The mimetype defines this new file as a folder
            'mimeType' : 'application/vnd.google-apps.folder'
        }
        folder = drive.CreateFile(folder_metadata)
        folder.Upload()
        return folder

    def upload_file(self, file_name, folder_name=None):
        if folder_name:
            if not self.folder_found(folder_name):
                folder = self.create_folder(folder_name)
            f = self.drive.CreateFile({
                'parents': [{
                    'kind': 'drive#file',
                    'id': folder['id']
                }]
            })

            f.SetContentFile('/'.join([DevelopmentConfig.UPLOAD_FOLDER, file_name]))
            f.Upload()
        else:
            f = self.drive.CreateFile({
                'title': file_name
            })
            f.SetContentFile('/'.join([DevelopmentConfig.UPLOAD_FOLDER, file_name]))
            f.Upload()
        

    def folder_found(self, folder_name):
        contents = self.drive.ListFile({'q': "'root' in parents and trashed=false" }).GetList()
        for content in contents:
            if content.get('mimeType') == 'application/vnd.google-apps.folder' and content.get('title') == folder_name:
                return True
        return False
               