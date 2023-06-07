# Scrapy Parse Pep

## Описание проекта

Парсинг сайта [документов PEP](https://peps.python.org/) на базе фреймворка Scrappy и сохранение данных в .csv файл.  
Парсер выводит собранную информацию в два файла .csv:  
1. Вывод списка всех PEP: номер, название и статус  
2. Сводка по статусам PEP - сколько найдено документов в каждом статусе(статус, количество).  

## Установка и использование

**[Скопировать репозиторий](https://github.com/petrovi-4/scrapy_parser_pep.git)**

```
git clone https://github.com/petrovi-4/scrapy_parser_pep.git
```  
 **Установить и активировать виртуальное окружение:**  

```
python3 -m venv venv  
source venv/bin/activate  
python - pip install --upgrade pip
```
**Установить зависимости из файла requirements.txt:**  

```
pip install -r requirements.txt
```
## Запуск парсера

Для сбора информации запустить парсер:

```
scrapy crawl pep
```

#### Автор: [petrovi-4](https://github.com/petrovi-4)

![GitHub User's stars](https://img.shields.io/github/stars/petrovi-4?label=Stars&style=social)
![licence](https://img.shields.io/badge/licence-GPL--3.0-green)
