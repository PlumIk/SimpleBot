from Data import params as scenes_nums
import Data.MessegesTexts as texts
from Models.SceneParamsExample import SceneParams
from VkMessenger.VkMessengerMain import VkMessengerMain


class SceneExample:
    """Базовый класс сцены."""

    SCENE_NUM: int = scenes_nums.EXAMPLE_NUM
    """Номер данной сцены."""

    LAST_VALID_SCENE: int = scenes_nums.DEFAULT_SCENE_NUM
    """Номер последней сцены, которую можно безопасно загрузить."""

    VkMessenger: VkMessengerMain = VkMessengerMain()
    """Экземпляр объекта для связи с ВК."""

    def start_work(self, params: SceneParams) -> None:
        """
        Метод работы сцены.
        :param params: Параметры сцены.
        """
        self.wright_message(params.USER_UID, texts.ERROR_TEXT + f"{self.SCENE_NUM}")

    def parse_data(self, data):
        pass

    def wright_message(self, uid: int, message: str) -> None:
        """
        Отправляет запрос на отправку сообщения пользователю.
        :param uid: ID пользователя.
        :param message: Сообщение для пользователя.
        """
        self.VkMessenger.write_msg(uid, message)

