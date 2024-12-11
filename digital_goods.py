from abc import ABC, abstractmethod


ACTION_GAME = 'action game'
PUZZLE_GAME = 'puzzle game'
ROCK_MUSIC = 'rock music'
JAZZ_MUSIC = 'jazz music'


class DigitalGoods(ABC): # interface for game and music classes
    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def download(self):
        pass

    @abstractmethod
    def play(self):
        pass


class ActionGame(DigitalGoods):  # concreate product
    def get_details(self):
        print('Action game')

    def download(self):
        print('The game is loading')

    def play(self):
        print('Play', end='\n\n')


class PuzzleGame(DigitalGoods):  # concreate product
    def get_details(self):
        print('Puzzle game')

    def download(self):
        print('The game is loading')

    def play(self):
        print('Play', end='\n\n')


class RockMusic(DigitalGoods):  # concreate product
    def get_details(self):
        print('RockMusic')

    def download(self):
        print('The music is loading')

    def play(self):
        print('Playing rock music', end='\n\n')


class JazzMusic(DigitalGoods):   # concreate product
    def get_details(self):
        print('JazzMusic')

    def download(self):
        print('The music is loading')

    def play(self):
        print('Playing jazz music', end='\n\n')


class AbstractFactory(ABC):  # abstract factory
    @abstractmethod
    def crete_music(self, music: str):
        pass

    @abstractmethod
    def create_game(self, game: str):
        pass


class DigitalProductFactory(AbstractFactory):  # concreate factory
    def crete_music(self, music: str):
        if music == JAZZ_MUSIC:
            return JazzMusic()
        elif music == ROCK_MUSIC:
            return RockMusic()
        else:
            raise ValueError("We don't have such music in our online store")

    def create_game(self, game: str):
        if game == ACTION_GAME:
            return ActionGame()
        elif game == PUZZLE_GAME:
            return PuzzleGame()
        else:
            raise ValueError('There is no such game in our online store')


def main(fabric, music: str, game: str):  # Realization
    if isinstance(fabric, DigitalProductFactory):
        your_music = fabric.crete_music(music)
        your_game = fabric.create_game(game)
        your_music.get_details()
        your_music.download()
        your_music.play()
        your_game.get_details()
        your_game.download()
        your_game.play()
    else:
        raise ValueError('Not a specific value')


if __name__ == '__main__':
    factory = DigitalProductFactory()
    main(factory, 'rock music', 'action game')














