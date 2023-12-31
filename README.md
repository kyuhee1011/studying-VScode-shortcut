# studying-VScode-shortcut

This app is a quiz app that helps a player memorize the most common keyboard shortcuts to use on the Visual Studio code smoothly with all other programming.

## Features

Studying VScode shortcut key consist of 5 tables

- Player
- Question
- Quiz
- quiz_question
- layer_question_track

## Database Relationship Diagram

![git hub code](https://github.com/kyuhee1011/studying-VScode-shortcut/blob/main/assets/cli%20diagram.png)

## prerequisites

Python 3.8.13

## Installing/ Getting Started.

Clone this repository and then install pipenv install.

```ubuntu
git@github.com:kyuhee1011/studying-VScode-shortcut.git
```

Or

![git hub code](https://github.com/kyuhee1011/studying-VScode-shortcut/blob/main/assets/git%20clone%20image.jpg)

```ubuntu
pipenv install
```

Run pipenv shell and then change to correct directory to play.

```ubuntu
pipenv shell
```

```ubuntu
cd lib/db
```

## Quick Start

Run python3 seed.py to seed the database before steps below.

1. Run python3 cli.py to login or add yourself.

   ![git hub code](https://github.com/kyuhee1011/studying-VScode-shortcut/blob/main/assets/start%20quiz%20.jpg)

2. Enter datas in database to start the game.

   ![git hub code](https://github.com/kyuhee1011/studying-VScode-shortcut/blob/main/assets/start%20quiz%202.jpg)
   ![git hub code](https://github.com/kyuhee1011/studying-VScode-shortcut/blob/main/assets/start%20quiz%203.jpg)

3. Start the Quiz

   ![git hub code](https://github.com/kyuhee1011/studying-VScode-shortcut/blob/main/assets/start%20quiz%204.jpg)

4. Question will be asked and nswer should be all lowercase including space and '+'
   How do you open/learn more about Visual Studio Shortcuts?
   answer="ctrl + k ctrl + s"

   ![git hub code](https://github.com/kyuhee1011/studying-VScode-shortcut/blob/main/assets/start%20quiz%205.jpg)

   press 'n' to continue and press 'any key' to exit.

   ![git hub code](https://github.com/kyuhee1011/studying-VScode-shortcut/blob/main/assets/start%20quiz%206.jpg)

5. View all questions will show all the questions are in database.

   ![git hub code](https://github.com/kyuhee1011/studying-VScode-shortcut/blob/main/assets/view%20all%20question.jpg)

6. My Score will show the player with highest point and current point for the current player.

   ![git hub code](https://github.com/kyuhee1011/studying-VScode-shortcut/blob/main/assets/show%20score.jpg)

7. Remove me will remove player and you can start it from the beginning adding with new username.

   ![git hub code](https://github.com/kyuhee1011/studying-VScode-shortcut/blob/main/assets/remove%20me.jpg)

Enjoy

## Video

https://youtu.be/x9eEgx4IHyM

## License

MIT
