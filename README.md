s # To Run Successfully, Follow These Steps

## 1. install the required modules

```
pip install -r requirements.txt
```

## 2. modify information to your own

- **demo.py - line 29-34**
- `meet_url` : change it to yout meeting room url
- `mail_address`, `password` : fill with your google account
- `target` : the key words that you should react, you can add multiple words in it
- `outputmessage` : message that you want to send if key words were detected

![](image/README/1652602893946.png)

## 3. run demo.py

```
python3 demo.py
```

- if it doesnt work, try running with your own way

# Appendix

## chrome driver doesnt work?

- maybe your os or version isnt different to mine
- go [download point](https://chromedriver.chromium.org/downloads) and replace the `chromedriver.exe` to the new one

## another problem

- if you occur any error please raise an issuse on this github repository and let me know

### current bug or problem

1. sometimes it would miss some button and fail to run completely
   - *current solution* - **just run again**
2. save the author's poor english!
   - *current solution* - **report grammer error in this tutorial**
3. if you have any solution or innovative way to improve this repository
   - *current solution* - **raise an issuse and let me know**

---

