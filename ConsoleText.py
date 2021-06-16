from PIL import Image, ImageDraw, ImageFont
import numpy

class ConsoleText:
    def __init__(self) -> None:
        self.queue = []
    
    def text(self, text, x=0, y=0, fields=1.3):
        self.queue.append(
            {"data":text, "x":x, "y":y, "fields": fields}
        )
    
    def load_font(self, font, size=15):
        self.font = ImageFont.truetype(font, size)
    
    def render(self, item):       
        self.base = Image.new('RGBA', (round(self.font.size/2)*len(item["data"]), round(self.font.size*item["fields"])), color = 'white')
        self.txt = Image.new('RGBA', self.base.size, (255,255,255,0))
        self.draw = ImageDraw.Draw(self.txt)
        self.draw.text( (item["x"],item["y"]), item["data"], font=self.font, fill=(0,0,0,255))
        return Image.alpha_composite(self.base, self.txt)
        
    def show(self):
        self.out.show()

    def display(self, spaces=' ', fill='*'):
        
        for item in self.queue:
            
            self.out = self.render(item)

            data = numpy.array(self.out).flatten()
            count = 0
            pixels_per_row = round(self.font.size/2)*len(item["data"])*4

            for index in range(len(data)):
                if count % (pixels_per_row) == 0:
                    print('\n')

                if (data[index] == 255):
                    print(spaces, end='')

                else:
                    print(fill, end='')

                count += 1


cl = ConsoleText()

cl.load_font('./fonts/font.ttf', size=15)

cl.text('hello!')
cl.text('World!', y=-5,fields=0.8)

cl.display()

# cl.show()





