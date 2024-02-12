from Models.item import Item
from utils.logger import Logger


logger = Logger.get_logger(__name__)


class SampleService():
    __lists = {}
    def __init__(self) :
        self = self
    
    # @staticmethod
    # def getInstance():
    #     """Static Access Method"""
    #     if SampleService.__lists is {}:
    #         SampleService()
    #     return SampleService.__lists 

    def getAllTasks(self):
        return self.__lists
    
    
    def updateTask(self, task_id: int, item: Item):
        if task_id not in self.__lists:
            return None
        self.__lists[task_id] = item
        return self.__lists[task_id]
    
    def insertTask(self, task:Item):
        self.__lists[task.id] = task
        print(self.__lists)
        return self.__lists[task.id]
    
    def deleteTask(self, task_id: int):
        if task_id not in self.__lists:
            return None
        self.__lists.pop(task_id)
        return self.__lists


    