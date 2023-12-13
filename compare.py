from requests import post
from config import auth


def compare(file1, file2):
    data = {**auth}
    files = {'image_file1': ('face1.jpg', open(file1, 'rb')),
             'image_file2': ('face2.jpg', open(file2, 'rb'))}
    r = post('https://api-us.faceplusplus.com/facepp/v3/compare',
             files=files, data=data)
    return r.json()


def purge():
    pass
