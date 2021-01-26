from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import TransparencyAttrib
from panda3d.core import TextNode
from panda3d.core import loadPrcFileData

from mapmanager import MapManager
from controller import Controller
from editor import Editor

# Настройка конфигурации приложения
# Заголовок окна
loadPrcFileData('', 'window-title My Minecraft')
# Отключение синхронизации
loadPrcFileData('', 'sync-video false')
# Включение отображения FPS
loadPrcFileData('', 'show-frame-rate-meter true')
# скрыть курсор мыши
loadPrcFileData('', 'cursor-hidden true')
# Установка размера окна
loadPrcFileData('', 'win-size 1000 750')
#loadPrcFileData('', 'win-size 1800 1000')


class Game(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # режим редактирования
        self.edit_mode = True

        # создаём менеджер карты
        self.map_manager = MapManager()

        # создаём контроллер мышки и клавиатуры
        self.controller = Controller()

        # создаём редактор
        self.editor = Editor(self.map_manager)


        # загрузка модели
        sky = loader.loadModel('sky/skybox')
        # перемещаем модель в рендер
        sky.reparentTo(render)
        # устанавливаем масштаб и позицию для модели
        sky.setScale(100)

        # загружаем картинку курсора
        self.pointer = OnscreenImage(image='target.png',
                                     pos=(0, 0, 0), scale=0.08)
        # устанавливаем прозрачность
        self.pointer.setTransparency(TransparencyAttrib.MAlpha)

        # имя файла для сохранения и загрузки карт
        self.file_name = "testmap.dat"

        # номер строки для текста на экране
        self.text_row=1

        # вывод на экран инструкций
        self.addInstructions("[Tab]: Edit/Game mode")
        self.addInstructions("Move mouse: Rotate camera")
        self.addInstructions("Left mouse button: Add block")
        self.addInstructions("Right mouse button: Remove block")
        self.addInstructions("[W]: Move Forward")
        self.addInstructions("[S]: Move Back")
        self.addInstructions("[A]: Move Left")
        self.addInstructions("[D]: Move Right")
        self.addInstructions("[E]: Move Up")
        self.addInstructions("[Q]: Move Down")
        self.addInstructions("[Space]: Jump")
        self.addInstructions("[F1]: Basic map")
        self.addInstructions("[F2]: Random map")
        self.addInstructions("[F3]: Save map")
        self.addInstructions("[F4]: Load map")
        self.addInstructions("[1-8]: Select color")
        self.addInstructions("Press ESC to exit")

        # элемент текста оповещений
        self.infoText = OnscreenText(text = '', scale = 0.06,
            fg=(1, 1, 1, 1), shadow=(0, 0, 0, 1), align=TextNode.ALeft,
            parent=base.a2dBottomLeft, pos = (0.08, 0.08))

        self.accept("f1", self.basicMap)
        self.accept("f2", self.generateRandomMap)
        self.accept("f3", self.saveMap)
        self.accept("f4", self.loadMap)

        self.accept("1", self.setColor, [(1,1,1,1), 'white'])
        self.accept("2", self.setColor, [(1,0.3,0.3,1), 'red'])
        self.accept("3", self.setColor, [(0.3,1,0.3,1), 'green'])
        self.accept("4", self.setColor, [(0.3,0.3,1,1), 'blue'])
        self.accept("5", self.setColor, [(1,1,0.3,0.5), 'yellow'])
        self.accept("6", self.setColor, [(0.3,1,1,0.5), 'aqua'])
        self.accept("7", self.setColor, [(1,0.3,1,0.5), 'purple'])
        self.accept("8", self.setColor, [None, 'random'])

        base.accept("tab", self.switchEditMode)

        self.setInfoText('')

        self.setColor(None, 'random')

        # генерируем случайный уровень
        self.generateRandomMap()

    def setInfoText(self, text):
        self.infoText.setText(text)
        if taskMgr.hasTaskNamed('clearText'):
            taskMgr.remove('clearText')
        taskMgr.doMethodLater(3, self.clearText, 'clearText')

    def basicMap(self):
        if not self.edit_mode:
            self.controller.setEditMode(self.edit_mode)
        self.map_manager.basicMap()
        self.setInfoText('Basic map generated')

    def generateRandomMap(self):
        if not self.edit_mode:
            self.controller.setEditMode(self.edit_mode)
        self.map_manager.generateRandomMap()
        self.setInfoText('Random map generated')

    def saveMap(self):
        self.map_manager.saveMap(self.file_name)
        self.setInfoText('Map saved to "'+self.file_name+'"')

    def loadMap(self):
        if not self.edit_mode:
            self.controller.setEditMode(self.edit_mode)
        self.map_manager.loadMap(self.file_name)
        self.setInfoText('Map loaded from "'+self.file_name+'"')

    def setColor(self, color, name):
        if self.edit_mode:
            self.map_manager.setColor(color)
            self.setInfoText('Set color - '+name)

    def switchEditMode(self):
        self.edit_mode = not self.edit_mode
        self.controller.setEditMode(self.edit_mode)
        self.editor.setEditMode(self.edit_mode)

        if self.edit_mode:
            self.pointer.setImage(image='target.png')
        else:
            self.pointer.setImage(image='target1.png')
        self.pointer.setTransparency(TransparencyAttrib.MAlpha)

    def addInstructions(self, msg):
        OnscreenText(text=msg, scale=0.05,
            fg=(1, 1, 1, 1), shadow=(0, 0, 0, 1), align=TextNode.ALeft,
            parent=base.a2dTopLeft, pos=(0.08, -self.text_row*0.055 - 0.04))
        self.text_row += 1

    def clearText(self, task):
        self.setInfoText('')


app = Game()
app.run()