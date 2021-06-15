# Описание работы
Данный иструмент позволяет выводить символьный текст в консоль.


____


## Использование
```PYTHON
ct = ConsoleText()                        #create object

ct.load_font('./fonts/font.ttf', size=15) #load any font

ct.text('hello!')                         #load your text

ct.render()                               #render your text

ct.display()                              #display your text at console

```
