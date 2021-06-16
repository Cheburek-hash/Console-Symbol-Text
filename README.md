# Описание работы
Данный иструмент позволяет выводить символьный текст в консоль.


____


## Использование
```PYTHON
ct = ConsoleText()                        #create object

ct.load_font('./fonts/font.ttf', size=15) #load any font

ct.text('hello!')
ct.text('World!', y=-5,fields=0.8)        #load your text

ct.display()                              #display your text at console

```
