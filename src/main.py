import random
import js

COLORS = [
  'white',
  'orange',
  'red',
  'pink',
  'blueviolet',
  'blue',
  'green',
  'black'
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


class Code:

  def __init__(self):
    self.elements = list()
    for i in range(4):
      self.elements.append(Element(i))


class Game:
  
  def play(self):
    for n in range(10):
      self.n = n
      self.code = Code()


Game().play()