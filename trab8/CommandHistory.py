class CommandHistory:
    def __init__(self):
        self.__history = [[]]

    def push(self, obj):
        if type(obj) == list:
            self.__history.append(obj)
        else:
            self.__history[len(self.__history)-1].append(obj)

    def pop(self):
        return self.__history.pop(-1)

    def isEmpty(self):
        return len(self.__history) == 0