```text
Description:
CTF{}
```
# Разведка и решение
Открываем pcap файл и смотрим какие объекты мы можем импортировать.
```text
File -> Export Objects -> HTTP
```

Видим один объект qr.png :
![](../../images/tb_png_stealer.png)

Экспортируем объект и видим, что это QR-код. Прочитаем содержимое в bash.
```bash
zbarimg qr.png
```

Вывод:
```text
QR-Code:CTF{can_you_see_images?}
```

# Flag
```text
CTF{can_you_see_images?}
```