# -*- coding: utf-8 -*-
"""Exercise-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_wMnrWljMMCurLGgEQBt4KZYAljf9uN3

# Упражнение 2 - списки и индексы

Упражнение, чтобы помочь вам лучше понять списки в Python и отработать изменения в файлах с помощью Git. Вы также познакомитесь с синтаксисом Markdown.

## Заметки об упражнении

- Ячейки кода на Python, где вы должны вносить изменения. Вы должны удалить этот текст и заменить его своим решением, чтобы выполнить задание.

    ```Python

    # Ваш код здесь
    raise NotImplementedError()
    
    ```
    
- Ячейки разметки Markdown, где вы должны вносить изменения, содержат поясняющий текст

    ```text
    
    Ваш ответ здесь
    ```
    
- Некоторые из ячеек в этом блокнок Jupyter – «только для чтения», и вы не можете их редактировать.
- Некоторые из ячеек с кодом содержат тесты. Если эти тесты не проходят (то есть вы видите сообщение об ошибке), вы знаете, что с вашим кодом все еще что-то не так.

### Советы по выполнению упражнения

- Используйте **в точности** те же имена переменных, что и в инструкциях, потому что ваши ответы будут автоматически оценены, и тесты, которые оценивают ваши ответы, зависят от того же форматирования или именования переменных, что и в инструкциях.

- **Пожалуйста не**:

    - **Изменяйте имена файлов**. Сделайте все свое редактирование в файле `Exercise-2.ipynb` (этом файле).
    - **Копируйте/вставляйте ячейки в этом блокноте**. Мы используем автоматизированную систему оценки, которая не будет работать, если есть копии кодовых ячеек.
    - **Изменяйте типы ячеек**. Вы можете добавить ячейки, но изменение типов ячеек для существующих ячеек (например, c кода на Markdown) также приведет к выходу из строя автоматизированной проверки.

## Соглашение об использовании ИИ

**Введите свое имя в ячейку ниже** чтобы подтвердить, что вы следовали [принципам курса об использовании инструментов ИИ](https://geo-python-2024.readthedocs.io/ru/latest/course-info/ai-tools.html) и понимаете, что использование инструментов ИИ считается обманом.

Полина К.

## Задача 1 - Создание и изменение списков

Ваша первая задача - создать список [метеорологических станций](http://meteomaps.ru/meteostation_codes.html) и их индексов.
Затем вы добавите еще несколько станций в свои списки и, отсортируете списки по возрастанию индекса станции.
Вы можете найти список станций и их индексы ниже.

| Название станции        | Индекс                  |
| ----------------------- | :---------------------: |
| Чаунская Бухта          | 25150                   |
| Туймазы                 | 28712                   |
| Конги                   | 32059                   |
| Тырка                   | 30526                   |
| Алакуртти               | 22301                   |

### Критерии успешного решения задачи

- Создание двух списков для названий станций и их индексов
- Добавление второго набора станций и индексов в ваши списки
- Сортировка списков в соответствии с инструкциями
- Коммит каждого изменения последовательно, используя Git, и Push изменений в Gitfliс

### Часть 1 - Создание списков

В ячейке ниже создайте два списка:

- `station_names` должен содержать названия станций в порядке, которые они приведены в таблице выше
- `station_indexes` должен содержать метеорологические индексы станций, в указанном выше порядке
"""

# Создайте списки ниже
station_names = ["Jan Mayen", "Grahuken", "Hornsund", "Ny-Alesund I", "Edgeoya",]
station_indexes = [1001, 1002, 1003, 1004, 1006,]

"""Давайте теперь проверим, что списки содержат ожидаемые значения."""

# Это тестовая ячейка, которая проверяет, что длина списка верна
# Запуск этой ячейки не должен производить никаких ошибок
assert len(station_names) == 5, 'Список station_names должен иметь 5 пунктов.'
assert len(station_indexes) == 5, 'Список station_indexes должен иметь 5 пунктов.'

# Это тестовая ячейка, которая проверяет, что первый элемент в списках верен
# Запуск этой ячейки не должен производить никаких ошибок
assert station_names[0] == 'Чаунская Бухта', 'The first item in the station_names list should be "Чаунская Бухта"'
assert station_indexes[0] == 25150, 'The first item in the station_indexes list should be 25150'

"""### Часть 2 - Изменение списков

Давайте теперь добавим еще несколько станций в наши списки.
Станции, которые нужно добавить, показаны в таблице ниже.

| Название станции        | Индекс                  |
| ----------------------- | :---------------------: |
| Тадебяяха               | 20964                   |
| Териберка               | 22028                   |
| Краснодар Пашковская    | 34929                   |

В ячейке ниже вы должны добавить станции и индексы в существующие списки `station_names` и `station_indexes` в порядке, в котором они перечислены выше.
"""

# Ниже добавьте станции со второй таблицы в списки

station_names.append("Тадебяяха")
station_names.append("Териберка")
station_names.append("Краснодар Пашковская")

station_indexes.append(20964)
station_indexes.append(22028)
station_indexes.append(34929)
raise NotImplementedError()

"""Теперь мы можем проверить, содержат ли модифицированные списки ожидаемые значения."""

# Это тестовая ячейка, которая проверяет, что длина списка верна
# Запуск этой ячейки не должен производить никаких ошибок
assert len(station_names) == 8, 'Список station_names должен иметь 8 элементов.'
assert len(station_indexes) == 8, 'Список station_indexes должен иметь 8 элементов.'

# Это тестовая ячейка, которая проверяет, что последний элемент в списках верен
# Запуск этой ячейки не должен производить никаких ошибок
assert station_names[-1] == 'Краснодар Пашковская', 'Последний элемент в списке station_names должен быть "Краснодар Пашковская"'
assert station_indexes[-1] == 34929, 'Последний элемент в списке station_indexes должен быть 34929'

"""### Часть 3 - Сортировка списков

Наконец, мы можем взять наши списки и отсортировать их. Цель здесь состоит в том, чтобы сделать два отсортированных списка:

- Список `station_names` должен быть отсортирован, чтобы станции были в алфавитном порядке
- Список `station_indexes` должен быть отсортирован так, чтобы самый *большой* индекс был первым в списке
"""

# Ниже сортируйте списки как указано
# station_names.sort()
print(station_names)
station_indexes.sort(reverse = True)
print(station_indexes)

"""Давайте теперь проверим, что первое значение в каждом отсортированном списке является правильным."""

# Это тестовая ячейка, которая проверяет, что последний элемент в списках верен
# Запуск этой ячейки не должен производить никаких ошибок
assert station_names[0] == 'Алакуртти', 'Первый элемент в списке station_names должен быть "Алакуртти"'
assert station_indexes[0] == 34929, 'Первый элемент в списке station_indexes должен быть 34929'

"""### Часть 4 - Понимание кода

Глядя на списки, используемые в проблеме 1, в чем может быть проблема с тем, как мы их сортировали?
Пожалуйста, ответьте кратко в ячейке ниже.

При сортировке название индекса не соответсвует названию станции

### Часть 5 - Python + Google (необязательно)

Python имеет функцию под названием `zip()`, которая может быть полезна для решения проблемы, упомянутой в части 4.
Вы можете немного погуглить и посмотреть как использовать функцию `zip()`.
Это необязательная задача.

**ПРИМЕЧАНИЕ**: Если вы планируете пропустить эту задачу, обязательно удалите линию `raise NotimplementError()` в ячейке ниже, чтобы у вас не было никаких ошибок, когда мы запускаем ноутбук.
"""

station_names = ["Jan Mayen", "Grahuken", "Hornsund", "Ny-Alesund I", "Edgeoya",]
station_indexes = [1001, 1002, 1003, 1004, 1006,]

station_names.append("Тадебяяха")
station_names.append("Териберка")
station_names.append("Краснодар Пашковская")

station_indexes.append(20964)
station_indexes.append(22028)
station_indexes.append(34929)

station_tuple = zip(station_names, station_indexes)
station_names.sort()
station_indexes.sort()
station_indexes.reverse()

"""## Задача 2 - Cредняя температура

В таблице ниже представлены [среднемесячные и годовые значения метеорологических параметров по данным за период 1991-2020 гг. по Санкт-Петербургу](http://www.meteo.nw.ru/articles/index.php?id=2).


| Month    | Temperature [°C] |
| ---------| :--------------: |
| Январь   | -4.8             |
| Февраль  | -5.0             |
| Март     | -1.0             |
| Апрель   | 5.2              |
| Май      | 11.5             |
| Июнь     | 16.1             |
| Июль     | 19.1             |
| Август   | 17.4             |
| Сентябрь | 12.4             |
| Октябрь  | 6.2              |
| Ноябрь   | 0.9              |
| Декабрь  | -2.5             |

В ячейке кода ниже напишите код Python, который позволит пользователям выбирать месяц и получать ежемесячную среднюю температуру на экране.
Например, ваш код должен отображать следующее за март:

```
Средняя температура в Санкт-Петербурге в марте составляет -1,0
```

### Критерии успешного выполнения задачи 2

- Ваш блокнот отображает ежемесячную температуру в выбранном месяце путем определения переменной `selected_month_index`. **Примечание**: Мы ожидаем, что вы будете использовать значение индекса для выбора месяца, а не имя месяца.
- Код работает для всех 12 месяцев в году.
- Код имеет комментарии
– Код добавлен в репозиторий
"""

# переменная для установки выбранного месяца
selected_month_index = input("Напиши название месяца ")

# два списка. Пожалуйста, не меняйте имена переменных!
months =["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
average_temp = [-4.8, -5.0, -1.0, 5.2, 11.5, 16.1, 19.1, 17.4, 12.4, 6.2, 0.9, -2.5]

# переменная для вывода строки на экран
print_statement = ("В СПБ средняя температура в " + str(months[int(selected_month_index)]) + " составляет " + str(average_temp[int(selected_month_index)]))

# Вывод результата на экран
print(print_statement)

"""### Дополнительные тесты для проблемы 2"""

# Оба списка имеют длину 12
assert len(months) == 12, 'Неправильная длина!'
assert len(average_temp) == 12, 'Неправильная длина!'

# Переменные months и average_temp являются списками
assert isinstance(months, list), 'Переменная months не является списком'
assert isinstance(average_temp, list), 'Переменная average_temp не является списком'

"""## Задача 3 - практика использования Markdown

Последняя задача в этом упражнении - ответить на вопросы и добавить изображение в этот блокнот, используя Markdown. **ПРИМЕЧАНИЕ**: Вы можете прочесть о [форматировании текста Markdown здесь](https://help.github.com/articles/basic-writing-and-formatting-syntax/).

### Критерии успешного выполнения

- Есть ответы на три вопроса ниже
- Есть изображение любимого животного с использованием Markdown

### Часть 1

Используйте Markdown, чтобы ответить на три вопроса ниже.

- Что нового вы изучили в этом уроке?
- Что было непонятно?
- Что бы вы поменяли или улучшили?
    
*Пожалуйста, используйте список Markdown при ответе на эти вопросы.*

Ваш ответ здесь

*   Я узнала как работать с индексами и списками
*   Очен6ь долго не могла понять как работать с упражнением 2, пока не открыла его в google colab
*  Хотелось бы видеть наглядные примеры как выполнять задания, потому что без них сложнее понять смысл задания и что от меня требуется)

### Часть 2 - добавление изображения

Добавьте изображение животного, которое вам нравится, вместе с короткой подписью.

Вы можете добавить изображение, используя URL-адрес, или загрузив изображение в ваш репозиторий и связав файл изображения с этим блокнотом.

Вы можете искать картинки на [Wikimedia Commons](https://commons.wikimedia.org/wiki/Main_Page) или [Pixabay](https://pixabay.com/), или загрузите свои собственные изображения животных.

https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Pembroke_Welsh_Corgi_in_Grass.jpg/640px-Pembroke_Welsh_Corgi_in_Grass.jpg
"""