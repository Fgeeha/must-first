# Proxy + Google Chrome (yandex browser)

1. Ставим себе расширение [proxy-switchyomega](https://chromewebstore.google.com/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif?pli=1). 

Нажимаем на расширение справа вверху и переходим в Options, 
![Screenshot 01.png](img/Screenshot01.png)
![Screenshot 02.png](img/Screenshot02.png)

выбираем слева Proxy, 
![Screenshot03.png](img/Screenshot03.png)
далее настраиваем, я взял из 3X-UI (или данные, которые вам дали (Protocol + URL + PORT)), далее на замочек справа, там логин и пароль.
![Screenshot04.png](img/Screenshot04.png)

 Мы добавили, куда обращаться.
 
Теперь настроим правила маршрута. 

Идем в Auto Switch и пишем так: 

- Condition Type у всех Host Wildcard 

- Condition Details *.websiteAddress.com

- Profile выбираем тот, что заполняли выше у меня это proxy

И нажимаем слева Apply changes.

![Screenshot05.png](img/Screenshot05.png)


мой лист адресов:

- *.spotify.com

- *.2ip.ru

- *.openai.com

- *.chatgpt.com


| Sort | Condition Type | Condition Details   | Profile | Actions         |
|------|----------------|---------------------|---------|------------------|
| ⇅    | Host wildcard  | `*.spotify.com`     | proxy   | 🗑 📋 ⬇️         |
| ⇅    | Host wildcard  | `*.2ip.ru`          | proxy   | 🗑 📋 ⬇️         |
| ⇅    | Host wildcard  | `*.openai.com`      | proxy   | 🗑 📋 ⬇️         |
| ⇅    | Host wildcard  | `*.chatgpt.com`     | proxy   | 🗑 📋 ⬇️         |
| ⇅    | Host wildcard  | `*.youtube.com`     | proxy   | 🗑 📋 ⬇️         |
| ⇅    | Host wildcard  | `*.google.com`      | proxy   | 🗑 📋 ⬇️         |
| ⇅    | Host wildcard  | `*.grok.com`        | proxy   | 🗑 📋 ⬇️         |
|      |                | **Default**         | [Direct]| ⬆️              |


Теперь находим это расширение вверху в браузере и нажимаем на Auto Switch, и можно перейти на https://2ip.ru и проверить, что работает, и на https://www.reg.ru/web-tools/myip, чтобы проверить, что не использует на других сайтах.

![Screenshot06.png](img/Screenshot06.png)
