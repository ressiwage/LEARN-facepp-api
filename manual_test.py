from requests import post

#тестим загрузку на гослинге
r = post('http://127.0.0.1:5000/upload', files={
    'file': (
        'face.jpg',
        open('files/1.jpg', 'rb')
        )})
print(r, r.text)

#тестим рамку на гослинге
r = post('http://127.0.0.1:5000/detect', json={
    'file': '1.jpg',
    'color': '#fcba03'})
print(r, r.text)

#тестим сравнение на гослингах
r = post('http://127.0.0.1:5000/compare', json={
    'file1': '1.jpg',
    'file2': '1.jpg'
})
print(r, r.text)
