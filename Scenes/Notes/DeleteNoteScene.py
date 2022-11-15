from Data import params as scenes_nums
from Data.ScenesData.Notes.NoteWork import NoteWork
from Models.SceneParamsExample import SceneParams
from Scenes.Notes.NoteSceneExample import NoteSceneExample
from Scenes.Notes.ShowNotesScene import ShowNotesScene
import Data.MessegesTexts as texts


class DeleteNoteScene(NoteSceneExample):
    """Сцена создания заметки"""

    def __init__(self):
        """Инициализирует экземпляр класса."""
        super().__init__()
        self.SCENE_NUM = scenes_nums.SHOW_NOTES_SCENE_NUM

    def start_work(self, params: SceneParams) -> None:
        """
        Метод работы сцены.
        :param params: Параметры сцены.
        """
        if self.notes is None:
            self.SetNote(NoteWork(params.USER_UID))
        if params.USER_MESSAGE.isnumeric():
            self.notes.DeleteNote(int(params.USER_MESSAGE))
            params.SOME_DATA = self.notes
            params.NEXT_SCENE_NUM = scenes_nums.SHOW_NOTES_SCENE_NUM
            params.SetTrigger()
