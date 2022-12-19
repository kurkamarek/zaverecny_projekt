# Ročníkový projekt | ChatApp
#### Webová chatovací aplikace využívající framework Django

## Cíle:
- Instalace modulů a virtuálního prostředí &check;
- vytvořit základ aplikace (models.py, urls.py, views.py atd.) &check;
- vytvořit základní design webové stránky (pravděpodobně využiju bootstrap nebo tailwindcss) &check;
- vytvořit registrační a přihlašovací formulář &check;
- zařídit funkčnost registrace a přihlášení včetně chybových hlášek &check;
- zařídit funkčnost odhlášení &check;
- vytvořit appku pro místnosti &check;
- vytvořit super uživatele &check;
- zobrazení seznamu s jednotlivými místnostmi &check;
- zobrazení detailu jednotlivých místností &check;
- možnost připojit se do chatu &check;
- funkční odesílání zpráv &check;
- ukládání zpráv
- dockerizovat aplikaci

## Zdroje:
- https://youtu.be/SF1k_Twr9cg
- https://docs.djangoproject.com/en/4.1/intro/tutorial01/
- https://blog.logrocket.com/dockerizing-django-app/
- https://pipenv-fork.readthedocs.io/en/latest/basics.html

## Chyby:
- během připojení do chatu následující chyba: Uncaught TypeError: Cannot read properties of null (reading 'textContent')<br/>
odkazující na řádek 41 v room.html <br/>
const roomName = JSON.parse(document.getElementById('json-roomname').textContent); &#10004; OPRAVENO
- při odesílání zprávy následující chyba: Exception inside application: disconnect() takes 1 positional argument but 2 were given
