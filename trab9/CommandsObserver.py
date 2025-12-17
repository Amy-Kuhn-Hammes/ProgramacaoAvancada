class CommandsObserver:

    def __init__(self):
        self.__next = []
        self.__wait = []

    def subinscribeWait(self, command):
        self.__wait.append(command)

    def subinscribeNext(self, command):
        self.__next.append(command)

    def notify(self, img):
        for i in self.__next:
            i.execute(img)
        self.__next = self.__wait
        self.__wait = []

    def setNext(self, l):
        self.__next = l

    def setWait(self, l):
        self.__wait = l