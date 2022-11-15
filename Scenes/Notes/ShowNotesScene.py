from Data import params as scenes_nums
from Data.ScenesData.Notes.NoteWork import NoteWork
from Models.SceneParamsExample import SceneParams
from Scenes.Notes.NoteSceneExample import NoteSceneExample
from Scenes.Notes.NotesAnswerWaitScene import NotesAnswerWaitScene
from Scenes.SceneExample import SceneExample
import Data.MessegesTexts as texts


class ShowNotesScene(NoteSceneExample):
    """Сцена показа всех заметок"""

    def __init__(self):
        """Инициализирует экземпляр класса."""
        super().__init__()
        self.SCENE_NUM = scenes_nums.ADD_NOTE_SCENE_NUM

    def start_work(self,  params: SceneParams) -> None:
        """
        Метод работы сцены.
        :param params: Параметры сцены.
        """
        if self.notes is None:
            self.notes = NoteWork(params.USER_UID)
        for one in self.notes.GetNotes():
            self.wright_message(params.USER_UID, one)
        self.wright_message(params.USER_UID, texts.SHOW_NOTE_TEXT)
        params.SOME_DATA = self.notes
        params.NEXT_SCENE_NUM = scenes_nums.NOTE_WAIT_SCENE_NUM
