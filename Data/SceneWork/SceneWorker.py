from Data import params as scenes_nums
from Scenes.HelloAnswerWaitScene import HelloAnswerWaitScene
from Scenes.HelloScene import HelloScene
from Scenes.Notes.AddNoteScene import AddNoteScene
from Scenes.Notes.DeleteNoteScene import DeleteNoteScene
from Scenes.Notes.NotesAnswerWaitScene import NotesAnswerWaitScene
from Scenes.Notes.ShowNotesScene import ShowNotesScene
from Scenes.SceneExample import SceneExample

"""class SceneWorker:
    __scenes: dict

    def __init__(self):
        self.__scenes = {}
        self.AddScene(scenes_nums.HELLO_SCENE_NUM, HelloScene)
        self.AddScene(scenes_nums.HELLO_WAIT_SCENE, HelloAnswerWaitScene)
        self.AddScene(scenes_nums.SHOW_NOTES_SCENE_NUM, ShowNotesScene)

    def AddScene(self, num: int, scene):
        self.__scenes.update({num: scene})

    def create_scene(self, num: int) -> SceneExample:
       
        Создаёт сцену на осонове её номера.
        :param num: Номер сцены.
        :return: Созданная сцена.
       
        if self.__scenes.get(num) is not None:
            return self.__scenes[num].__init__(None)
        else:
            return self.__scenes[scenes_nums.DEFAULT_SCENE_NUM]
"""


def create_scene(num: int) -> SceneExample:
    """
        Создаёт сцену на осонове её номера.
        :param num: Номер сцены.
        :return: Созданная сцена.
    """
    if num == scenes_nums.HELLO_WAIT_SCENE:
        return HelloAnswerWaitScene()
    elif num == scenes_nums.SHOW_NOTES_SCENE_NUM:
        return ShowNotesScene()
    elif num == scenes_nums.ADD_NOTE_SCENE_NUM:
        return AddNoteScene()
    elif num == scenes_nums.NOTE_WAIT_SCENE_NUM:
        return NotesAnswerWaitScene()
    elif num == scenes_nums.NOTE_DELETE_SCENE_NUM:
        return DeleteNoteScene()
    else:
        return HelloScene()
