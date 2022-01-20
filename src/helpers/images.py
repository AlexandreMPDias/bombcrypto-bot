class Images:
    def __init__(self, images) -> None:
        self.__images = images

    def get(self, name: str):
        if(name not in self.__images):
            raise Exception(f"Image [{name}] not found")
        return self.__images[name]
