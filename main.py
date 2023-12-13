from flask import Flask, request, jsonify
from compare import compare
from detect import detect
from os import listdir, getcwd
from os.path import isfile, join


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def faq():
    return jsonify({
        '_comment': """пример использования сервиса -- в manual_test.py, 
        мной было принято решение не загружать фото в датасеты и на сайт, а загружать их 
        на бэк, чтобы потом сравнивать напрямую. это обусловлено тем, что с сайта 
        нельзя (или я не нашёл) скачивать загруженные файлы.""",
        'available photos for compare/detect':[f for f in listdir(getcwd()+'/files') if isfile(join(getcwd()+'/files', f))]
    })


@app.route('/compare', methods=['POST'])
def compare_files():
    content = request.json
    if content.get('file1') is None or content.get('file2') is None:
        return 'file1 or file2 not specified', 400

    return f"""confidence: {compare('files/'+content['file1'], 'files/'+content['file2'])['confidence']}%""", 200


@app.route('/detect', methods=['POST'])
def detect_file():
    content = request.json
    if content.get('file') is None:
        return 'file not specified', 400

    return detect('files/'+content['file'],
                  'out/'+content['file'],
                  color=content.get('color', '#000000')), 200


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = 'files/uploaded_'+file.filename
        file.save(filename)
    else:
        return 'no files in request', 400
    return f'uploaded to {filename}', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
