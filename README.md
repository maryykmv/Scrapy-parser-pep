# Асинхронный парсер PEP
«Асинхронный парсер PEP.»

## Оглавление
1. [Описание](#описание)
2. [Стек технологий](#стек-технологий)
3. [Как запустить проект](#как-запустить-проект)
4. [Автор проекта](#автор-проекта)


## Описание
Задача: создать парсер документов PEP на базе фреймворка Scrapy.

Парсер должен выводить собранную информацию в два файла .csv:
1. В первый файл нужно вывести список всех PEP: номер, название и статус.
2. Второй файл должен содержать сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество). В последней строке этого файла в колонке «Статус» должно стоять слово Total, а в колонке «Количество» — общее количество всех документов.


___
![pythonversion](https://img.shields.io/badge/python-%3E%3D3.9-blue)

## Стек технологий
- проект написан на Python
- фреймворк Scrapy
- система контроля версий - git


## Как запустить проект

- Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:wildcat3333/scrapy_parser_pep.git
```

- Переходим в директорию проекта
```
cd scrapy_parser_pep
```

- Создаем и активируем виртуальное окружение
```
python3 -m venv venv
source venv/bin/activate
```

- Обновляем менеджер пакетов pip
```
pip install --upgrade pip
```

- Устанавливаем зависимости из файла requirements.txt.
```
pip install -r requirements.txt
```

- Запускаем парсер
```
scrapy crawl pep
```


## Автор проекта
_[Мария Константинова](https://github.com/wildcat3333)_, python-developer
