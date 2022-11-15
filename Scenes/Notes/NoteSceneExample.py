from Data import params as scenes_nums
from Data.ScenesData.Notes.NoteWork import NoteWork
from Models.SceneParamsExample import SceneParams
from Scenes.SceneExample import SceneExample
import Data.MessegesTexts as texts


class NoteSceneExample(SceneExample):
    """Базовый класс сцены заметок."""

    notes: NoteWork = None

    def __init__(self):
        """Инициализирует экземпляр класса."""
        self.SCENE_NUM = scenes_nums.NOTE_SCENE_EXAMPLE_NUM

    def parse_data(self, data):
        if data is not None:
            self.SetNote(data)

    def SetNote(self, notes: NoteWork):
        self.notes = notes

    def start_work(self, params: SceneParams) -> None:
        """
        Метод работы сцены.
        :param params: Параметры сцены.
        """
        self.wright_message(params.USER_UID, texts.ERROR_TEXT + f"{self.SCENE_NUM}")
