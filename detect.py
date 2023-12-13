from requests import post
from PIL import Image, ImageDraw
from config import auth


def detect(file, file_out, color='#000000'):
    '''
    detect(file, file_out, color) -> new_path
    file -- string -- название исходного файла
    file_out -- string -- название получившегося файла
    color -- string -- название цвета рамки в hex формате (необязательный)
    '''
    data = {**auth}
    files = {'image_file': ('face.jpg', open(file, 'rb'))}
    r = post('https://api-us.faceplusplus.com/facepp/v3/detect',
             files=files, data=data)
    rectangles = [i['face_rectangle'] for i in r.json()['faces']]
    im = Image.open(file)
    for r in rectangles:
        img1 = ImageDraw.Draw(im)
        img1.line([r['left'], r['top'],
                   r['left'] + r['width'], r['top']], fill=color, width=2)
        img1.line([r['left'], r['top'],
                   r['left'], r['top']+r['height']], fill=color, width=2)
        img1.line([r['left'], r['top']+r['height'],
                   r['left'] + r['width'], r['top']+r['height']], fill=color, width=2)
        img1.line([r['left']+r['width'], r['top'], 
                   r['left'] + r['width'], r['top']+r['height']], fill=color, width=2)
    new_path = file_out
    im.save(new_path)
    return new_path
