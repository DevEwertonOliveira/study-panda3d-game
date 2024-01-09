from panda3d.core import loadPrcFile
loadPrcFile("config/config.prc")

from direct.showbase.ShowBase import ShowBase

class MyGame(ShowBase):
  def __init__(self):
    super().__init__()

    # only disables the default camera control
    self.disableMouse()

    box = self.loader.loadModel("models/box")
    box.setPos(0,10,0)
    box.reparentTo(self.render)

    panda = self.loader.loadModel("models/panda")
    panda.setPos(-2,10,0)
    panda.setScale(0.2,0.2,0.2)
    panda.reparentTo(self.render)

game = MyGame()
game.run()