from vk_api.longpoll import VkEventType
from Data.SceneWork.SceneKeeper import SceneLoader
from Models.SceneParamsExample import SceneParams
from VkMessenger.VkMessengerMain import VkMessengerMain

if __name__ == "__main__":
    ''' Инициализирует программу '''
    vk = VkMessengerMain()
    scenes = SceneLoader()
    for event in vk.get_long_pool().listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                params = SceneParams()
                params.USER_MESSAGE = event.text
                params.USER_UID = event.user_id
                scenes.find_scene(params.USER_UID).start_work(params)
                scenes.set_scene_num(params.USER_UID, params.NEXT_SCENE_NUM, params.SOME_DATA)
                while params.GetTrigger():
                    scenes.find_scene(params.USER_UID).start_work(params)
                    scenes.set_scene_num(params.USER_UID, params.NEXT_SCENE_NUM, params.SOME_DATA)
