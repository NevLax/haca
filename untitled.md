≡ Краткое руководство Markdown

#### Документация Swagger
url: //server/swagger

##### How to use

![try it out](/try_it_out.png)

![Tux, the Linux mascot](/one.png)
Загрузить изобрвжние можно с помомщью следующей формы
![Tux, the Linux mascot](/load_image.png)

Обработать запрсом через api:
![execute](/execute.png)


#### Запуск
srver/pocess-image

#### По скрипту
##### Ипорты
```pip install flask, get_swaggerui_blueprint```

**swagger.yaml** закинуть в папку static


in *pap.py*[8]
```
def DoSomething(fileImage):
    pass 
```
заменить функцию, на вызов core. 
отправляет **картинку** как файл и вовращает **json**, уже содержащий структуру
```
{
    "message": "string",
    "items": [
      {
        "signature": "string",
        "content": "string",
        "coordinates": [
          [
            0,
            0
          ]
        ]
      }
    ]
  }
```