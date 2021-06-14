from direct.showbase.ShowBase import ShowBase

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model = loader.loadModel('models/environment')
        self.model.reparentTo(render)
        self.model.setScale(0.1)
        self.model.setPos(-2, 25, -3)

game = Game()
game.run()
