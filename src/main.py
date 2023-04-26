import random
import js
from pyodide.ffi.wrappers import add_event_listener

COLORS = [
  'cyan',
  'plum',
  'blueviolet',
  'teal',
  'saddlebrown',
  'lime',
  'crimson',
  'gold'
  ]

def show_legend():
  js.document.getElementById('div-legend').style.opacity = 1
  js.document.getElementById('div-legend').style.visibility = 'visible'
  js.document.getElementById('div-legend').style.zIndex = 1

def hide_legend():
  js.document.getElementById('div-legend').style.opacity = 0
  js.document.getElementById('div-legend').style.visibility = 'hidden'
  js.document.getElementById('div-legend').style.zIndex = -1


class Element:
  
  def __init__(self, i):
    self.id = i
    self.color = random.choice(COLORS)
    self.guessed = False


class Code:

  def __init__(self):
    self.elements = list()
    for i in range(4):
      self.elements.append(Element(i))


class Button:
  
  def __init__(self, row, i):
    self.id = str(row) + str(i + 1)
    self.pressed = False
    self.guessed = False
    self.in_code = False
    self.colors = iter(COLORS)
    js.document.getElementById(self.id).className = 'active'
    js.document.getElementById(self.id).disabled = False
    
  def change_color(self):
    self.pressed = True
    try:
      self.color = next(self.colors)
      js.document.getElementById(self.id).style.backgroundColor = self.color
    except StopIteration:
      self.colors = iter(COLORS)
      self.change_color()
    

class Row:
  
  def __init__(self, code, n):
    self.id = n
    self.code = code
    self.buttons = list()
    for i in range(4):
      self.buttons.append(Button(self.id, i))
  
  def guess(self):
    if all([b.pressed for b in self.buttons]):
      for n, button in enumerate(self.buttons):
        if button.color == self.code.elements[n].color:
          self.code.elements[n].guessed = True
          button.guessed = True
          js.document.getElementById(button.id).className = 'guessed'
      new_code = [e.color for e in self.code.elements if not e.guessed]
      for n, button in enumerate(self.buttons):
        if button.guessed:
          pass
        else:
          if button.color in new_code:
            button.in_code = True
            js.document.getElementById(button.id).className = 'in-code'
      for n, button in enumerate(self.buttons):
        if not(button.guessed or button.in_code):
          js.document.getElementById(button.id).className = 'out-code'
      game.move += 1
      game.play()
    else:
      pass
  

class Game:
  
  def __init__(self):
    self.code = Code()
    self.move = 0
  
  def play(self):
    if self.move < 10:
      self.row = Row(self.code, self.move)


game = Game()
game.play()