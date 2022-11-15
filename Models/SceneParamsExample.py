from Data import params as scenes_nums

class SceneParams:
    """Класс с параметрами для сцены."""

    USER_MESSAGE: str
    """Строка с сообщением от пользльзователя"""

    USER_UID: int
    """Идентификатор пользователя"""

    NEXT_SCENE_NUM = scenes_nums.HELLO_SCENE_NUM
    """Номер слудующей сцены."""

    SOME_DATA = None
    """Данные, которые нужно передать в следующую сцену"""

    __need_trigger = False
    """Надо ли показывать следующую сцену"""

    def SetTrigger(self):
        """Устонавливает, надо ли показывать следующую сцену."""
        self.__need_trigger = True

    def GetTrigger(self):
        """Получает значение, надо ли показывать следующую сцену"""
        if self.__need_trigger:
            self.__need_trigger = False
            return True
        return False
