## Решение ДЗ №4 по теме "django, django rest framework". TODO API. 

---
### Задание:  

Продолжение предыдущего дз, на закрепление понимания django rest framework. Нужно дополнить управление задачами с помощью rest api с использованием drf.  

Ожидаются методы для управления задачами:  

*    GET /api/tasks - получть список всех задач.
*    GET /api/tasks/{id} - получть одну конкретную задачу.
*    POST /api/tasks - создать задачу.
*    PUT (или PATCH) /api/tasks/{id} - отредактировать существующую задачу.
*    DELETE /api/tasks/{id} - удалить одну задачу.

При этом обязательно:  

*    Использовать фильтрацию для поиска задачи по заголовку (запрос GET может быть дополнен query-параметром ?title=...).
*    Использовать фильтрацию для поиска активных\неактривных задач (запрос GET может быть дополнен query-параметром ?is_active=...).
*    Должна быть пагинация при GET-запросе (любая).
*    Должна быть возможность упорядочить результат GET - запроса (запрос GET может быть дополнен query-параметром ?ordering=...).

---
  
### Инструкция по запуску:
1. Установить пакеты `"pip install -r requirements.txt"`
2. Запуск из корня программы: `python3 manage.py runserver`
3. Приложение принимает запросы по адресу `http://127.0.0.1:8000/api/tasks`  
---
  
### Решение:  
##### Структура API:  

`GET на http://127.0.0.1:8000/api/tasks/` - получить список всех задач;  
`GET на http://127.0.0.1:8000/api/tasks/{id}/` - получить конкретную задачу;  
`POST на http://127.0.0.1:8000/api/tasks/` - создать задачу. Обязательное поле для заполнения - "name";  
`PUT на http://127.0.0.1:8000/api/tasks/{id}/` - редактировать задачу. Обязательных полей нет;  
`DELETE на http://127.0.0.1:8000/api/tasks/{id}/` - удалить задачу;  

`GET на http://127.0.0.1:8000/api/tasks?title={name}` - фильтрация задач по полю "name";  
`GET на http://127.0.0.1:8000/api/tasks?is_active={false/true}` - фильтрация задач по полю "status";  
`GET на http://127.0.0.1:8000/api/tasks/?page=2` - работает пагинация;  
`GET на http://127.0.0.1:8000/api/tasks/?ordering={...}` - работает группировка по любому из полей (id, name, status, slug ...);  

---
  
##### Структура DB:  
Вся информация сохраняется в `sqlite3` в таблицу вида:  
```python
Table nouts {
    status = models.BooleanField(default=False, help_text="Статус выполнения")
    name = models.CharField(max_length=64, verbose_name="Задача")
    slug = models.SlugField(null=False, unique=True, blank=True, db_index=True, verbose_name="URL Post")    
    date_complite = models.DateTimeField(auto_now=False, null=True, blank=True, default=None)
    date_create = models.DateTimeField(auto_now_add=True)
}
```  
Код отформатирован средствами `BLACK`.  
