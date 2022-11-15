from Data import params as scenes_nums
from Models.SceneParamsExample import SceneParams
from Scenes.SceneExample import SceneExample
import Data.MessegesTexts as texts


class HelloScene(SceneExample):
    """Сцена приветствия."""

    def __init__(self):
        """Инициализирует экземпляр класса."""
        self.SCENE_NUM = scenes_nums.HELLO_SCENE_NUM
        self.LAST_VALID_SCENE = self.SCENE_NUM

    def start_work(self,  params: SceneParams) -> None:
        """
        Метод работы сцены.
        :param params: Параметры сцены.
        """
        self.wright_message(params.USER_UID, texts.HELLO_TEXT)
        self.wright_message(params.USER_UID, texts.START_TEXT)
        params.NEXT_SCENE_NUM = scenes_nums.HELLO_WAIT_SCENE
