from Data import params as scenes_nums
from Data.ScenesData.Notes.NoteWork import NoteWork
from Models.SceneParamsExample import SceneParams
from Scenes.Notes.NoteSceneExample import NoteSceneExample
import Data.MessegesTexts as texts


class NotesAnswerWaitScene(NoteSceneExample):
    """Сцена ожидания ответа после показа"""

    def __init__(self):
        """Инициализирует экземпляр класса."""
        super().__init__()
        self.SCENE_NUM = scenes_nums.NOTE_WAIT_SCENE_NUM

    def start_work(self, params: SceneParams) -> None:
        """
        Метод работы сцены.
        :param params: Параметры сцены.
        """
        if self.notes is None:
            self.SetNote(NoteWork(params.USER_UID))
        if params.USER_MESSAGE.isnumeric():
            if int(params.USER_MESSAGE) == 1:
                params.NEXT_SCENE_NUM = scenes_nums.DEFAULT_SCENE_NUM
                params.SetTrigger()
            elif int(params.USER_MESSAGE) == 2:
                self.wright_message(params.USER_UID, texts.DELETE_NOTE_TEXT)
                params.NEXT_SCENE_NUM = scenes_nums.NOTE_DELETE_SCENE_NUM
                params.SOME_DATA = self.notes
        else:
            self.wright_message(params.USER_UID, "Не понял")
