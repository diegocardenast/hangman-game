<p align="center">
  <img width="200" height="200" src="https://github.com/diegocardenast/hangman-game/blob/main/assets/images/hangman-game.png" alt="HangmanIcon">
</p>

# Hangman - The Game

Hangman is a game where the player needs to save the person to be hanged by finding the correct word. The player has a certain amount of opportunities, and if the player does not find out the answer, then the player will lose the game. For every wrongly guessed word, a life or trial in the game is lost and a “hanging-man” begins to appear, piece by piece. The aim is to solve the puzzle and guess the correct word(s)/phrase before the hangman dies.

--- 

## User Stories

- As a **user** I want to **understand the game rules** so that I can **play the game correctly**
- As a **user** I want to **have the options menu available** so that I can **restart the game anytime**
- As a **user** I want to **select the level of difficulty** so that I can **challenge myself with shorter or larger words**
- As a **user** I want to **be able to guess a letter from the game word** so that I can **try several times before it is game over**
- As a **user** I want to **be able to watch the letters that were selected** so that I can **avoid repeating letters**
- As a **user** I want to **be able to watch the hangman image and the number of left tries** so that I can **be more cautious with the following letters selection**

--- 

## Flowchart
<p align="center">
  <img src="https://github.com/diegocardenast/hangman-game/blob/main/assets/images/hangman-game-flowchart.png" alt="Hangman-flowchart">
</p>

  - Online version of the game flowchart can be found inside [Lucidchart (click here)](https://lucid.app/lucidchart/34de17b9-709a-49c4-8d79-44810d102faf/edit?viewport_loc=-776%2C-16%2C3245%2C1531%2C0_0&invitationId=inv_5ed7c721-b21a-4564-a0eb-f4a495f0d7b6)

--- 

## Features

### Am I Responsive View
![AmIResponsiveView](https://github.com/diegocardenast/)

### Implemented Features

__Index__

  - Initial area of the game. 

![Index](https://github.com/diegocardenast/)

__In-game Options__

  - You might have always the possibility to change difficulty level or restart the game. 

![InGameOptions](https://github.com/diegocardenast/)

__Instructions__

  - Instructions of the game
![Instructions](https://github.com/diegocardenast/)

__Difficulty selection__

  - The player can select among 3 levels of difficulty, which will make the words longer and harder to guess
![Difficulty](https://github.com/diegocardenast/)

__Hangman image__

  - The player will know how many tries he has left if a mistake is made.
![HangmanImage](https://github.com/diegocardenast/)


### Features Left to Implement
- NA

--- 

## Testing

### Validator Testing 
- Python
  - No errors were returned when passing through the official [pep8ci validator](https://pep8ci.herokuapp.com/)  

<p align="center">
  <img src="https://github.com/diegocardenast/hangman-game/blob/main/assets/images/code-pep8ci-validation.png" alt="code-pep8ci-validation">
</p>

### Manual Testing

**TEST** | **ACTION** | **EXPECTATION** | **RESULT** 
----------|----------|----------|----------
Input - User name - Invalid data	| Entered in : blank space, return key, symbols, numbers	| app informs user of invalid data & prompts the user to try again | Works as expected
Input - User name - Valid data	| Entered in : characters in scope | app proceeds to next function | Works as expected 


### Unfixed Bugs

- NA

--- 

## Deployment 

- The game code is stored in a GitHub repository and was deployed in the Heroku app. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

  When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

The live link can be found [HERE]( )

--- 

## Credits

### Content 

- Good/Best practice on the readme were shared by Lauren-Nicole Popich in her [mentoring](https://github.com/CluelessBiker/mentoring/tree/main) GitHub repositry
- User Stories and tasks creation was implemented following this [publication](https://boosthigh.com/software-requirements-specification/)
- The use of GitHub to collaborate and apply good practices was implemented following this [Slack post](https://code-institute-room.slack.com/archives/C05UQAPDNCT/p1697457705802579) and this [GitHub post](https://github.com/auxfuse/hackathon-git-labs/blob/main/basic.md)
- Use of [Lucidchart](https://lucid.app/lucidchart/34de17b9-709a-49c4-8d79-44810d102faf/edit?viewport_loc=-854%2C-32%2C3328%2C1570%2C0_0&invitationId=inv_5ed7c721-b21a-4564-a0eb-f4a495f0d7b6) to create the game flowchart
- Inspirational tutorial and use of code created by Aminah Mardiyyah Rufai and published in [medium.com](https://mardiyyah.medium.com/a-simple-hangman-learnpythonthroughprojects-series-10-fedda58741b)
- Inspirational tutorial and use of code created by SAI ASHISH KONCHADA and published in [makeuseof.com](https://www.makeuseof.com/python-game-hangman-create/)
- Filtering wordlist depending on diffculty level created by Komal Gupta and published in [favtutor.com](https://favtutor.com/blogs/filter-list-python)
- System exit article created by Shittu Olumide and published in [freecodecamp.org](https://www.freecodecamp.org/news/python-exit-how-to-use-an-exit-function-in-python-to-stop-a-program/)


### Media

- The icons along the web app were taken from [Font Awesome](https://fontawesome.com/)
- The use of the intro icons was provided by [Flaticon](https://www.flaticon.com/free-icons/hangman)
- The wordslist was taken from SAI ASHISH KONCHADA [GitHub repository](https://github.com/makeuseofcode/Hangman-Game/blob/main/hangman_wordlist.txt)


Thank You!

Diego Cárdenas
