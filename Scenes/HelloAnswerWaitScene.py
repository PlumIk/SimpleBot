from Data import params as scenes_nums
from Models.SceneParamsExample import SceneParams
from Scenes.Notes.AddNoteScene import AddNoteScene
from Scenes.Notes.ShowNotesScene import ShowNotesScene
from Scenes.SceneExample import SceneExample
import Data.MessegesTexts as texts


class HelloAnswerWaitScene(SceneExample):
    """Сцена ожидания ответа на стартовый ответ бота"""

    def __init__(self):
        """Инициализирует экземпляр класса."""
        self.SCENE_NUM = scenes_nums.HELLO_WAIT_SCENE
        self.LAST_VALID_SCENE = scenes_nums.DEFAULT_SCENE_NUM

    def start_work(self, params: SceneParams) -> None:
        """
        Метод работы сцены.
        :param params: Параметры сцены.
        """
        if params.USER_MESSAGE.isnumeric():
            if int(params.USER_MESSAGE) == 1:
                self.wright_message(params.USER_UID, texts.ADD_NOTE_TEXT)
                params.NEXT_SCENE_NUM = scenes_nums.ADD_NOTE_SCENE_NUM
            elif int(params.USER_MESSAGE) == 2:
                ShowNotesScene().start_work(params)
        else:
            self.wright_message(params.USER_UID, "Не понял")
