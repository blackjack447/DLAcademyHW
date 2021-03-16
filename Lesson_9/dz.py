'''
«Есть некоторый общий класс родитель Tag, который хранит в себе какой-то HTML тег (например: <tag></tag>).
От Tag наследуются еще четыре класса Image, Input, Text (т. е <p></p>), Link (т. е <a></a>).
С использованием указанных паттернов реализовать следующее поведение:
Должна быть возможность создать необходимый тег, явно его не создавая, т. е не через img = Image(),
 а через фабричный метод или фабрику, например factory.create_tag(name).»

'''

class Image:
    def __init__(self, name):
        self.name = '<img>'

    def __str__(self):
        return f'{self.name}'


class Input:
    def __init__(self, name):
        self.name = '<input></input>'

    def __str__(self):
        return f'{self.name}'


class Text:
    def __init__(self, name):
        self.name = '<p></p>'

    def __str__(self):
        return f'{self.name}'

class Link:
    def __init__(self, name):
        self.name = '<a></a>'

    def __str__(self):
        return f'{self.name}'


class Factory:
    def create_tag(name):
        if name == 'Image':
            tag = Image(name)
            return tag
        elif name == 'Input':
            tag = Input(name)
            return tag
        elif name == 'Text':
            tag = Text(name)
            return tag
        elif name == 'Link':
            tag = Link(name)
            return tag


tag = Factory.create_tag('Image')
print(tag)
tag = Factory.create_tag('Input')
print(tag)
tag = Factory.create_tag('Text')
print(tag)
tag = Factory.create_tag('Link')
print(tag)