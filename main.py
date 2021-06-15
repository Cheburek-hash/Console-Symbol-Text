from PIL import Image, ImageDraw, ImageFont
import numpy

class ConsoleText:
    def text(self, text, x=0, y=0, fields=1.3):
        self.text = text
        self.base = Image.new('RGBA', (round(self.font.size/2)*len(self.text), round(self.font.size*fields)), color = 'white')
        self.txt = Image.new('RGBA', self.base.size, (255,255,255,0))
        self.draw = ImageDraw.Draw(self.txt)
        self.draw.text( (x,y), text, font=self.font, fill=(0,0,0,255))
    
    def load_font(self, font, size=15):
        self.font = ImageFont.truetype(font, size)
    
    def render(self):
        self.out = Image.alpha_composite(self.base, self.txt)

    def show(self):
        self.out.show()

    def display(self, spaces=' ', fill='*'):
        data = numpy.array(self.out).flatten()
        count = 0
        pixels_per_row = round(self.font.size/2)*len(self.text)*4

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

cl.render()

# cl.show()

cl.display()







