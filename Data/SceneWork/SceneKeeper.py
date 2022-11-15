from Data import params
from Data.SceneWork.SceneWorker import create_scene
from Scenes.SceneExample import SceneExample


class SceneLoader:
    """Класс харнящий в себе сцены всех пользователей в данный момент ."""

    __scenesNum: dict
    __scenesExample: dict

    def __init_me(self):
        """Инициализация параметров."""
        self.__scenesNum = {}
        self.__scenesExample = {}

    def __new__(cls):
        """Инициализирует экземпляр класса типа Singleton."""
        if not hasattr(cls, 'instance'):
            cls.instance = super(SceneLoader, cls).__new__(cls)
            cls.__init_me(cls)
        return cls.instance

    def set_scene_num(self, uid: int, num: int, data) -> None:
        """
        Устанавливает сцену для пользователя.
        :param uid: ID пользователя.
        :param num: Номер сцены.
        """
        if num <= 0:
            num = params.DEFAULT_SCENE_NUM
        self.__scenesNum[uid] = num
        self.__scenesExample[uid] = create_scene(num)
        self.__scenesExample[uid].parse_data(data)

    def find_scene(self, uid: int) -> SceneExample:
        """
        Создаёт или достаёт сцену.
        :param uid: ID пользователя.
        """
        if self.__scenesExample.get(uid) is None:
            if self.__scenesNum.get(uid) is None:
                self.__scenesExample[uid] = create_scene(params.DEFAULT_SCENE_NUM)
            else:
                self.__scenesExample[uid] = create_scene(self.__scenesExample[uid])
        self.__scenesNum[uid] = self.__scenesExample[uid].LAST_VALID_SCENE

        return self.__scenesExample[uid]
