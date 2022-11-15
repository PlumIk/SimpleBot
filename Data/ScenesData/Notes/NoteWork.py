class NoteWork:
    """Класс для работы с заметками."""

    __notes: list
    """Список заметок."""

    __uid: int
    """Идентификатор пользователя"""

    def __init__(self, uid: int):
        """Инициализирует экземпляр класса"""

        self.__notes = ["first", "Second"]
        self.__uid = uid

    def AddNote(self, note_text: str):
        self.__notes.append(note_text)

    def GetNotes(self) -> list:
        ret = list()
        for i in range(len(self.__notes)):
            ret.append(f"{i + 1})" + self.__notes[i])
        return ret

    def DeleteNote(self, num: int):
        num -= 1
        if 0 <= num < len(self.__notes):
            self.__notes.pop(num)
