# Head $tart - Financial Storyline Game

## Overview

**Head $tart** is an interactive financial simulation game designed to teach players financial literacy through the lens of real-life decisions. Starting from the age of 18 and progressing to retirement, players navigate through career choices, investments, and unpredictable life events that affect their net worth and quality of life. By making critical financial decisions, players learn how their choices impact their long-term financial stability and success.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [How to Play](#how-to-play)
4. [Controls](#controls)
5. [Roadmap](#roadmap)
6. [Technologies](#technologies)
7. [Documentation](#documentation)
8. [Key Functions](#key-functions)
9. [Progression](#progression)
10. [Contributors](#contributors)
11. [License](#license)

## Introduction

Head $tart simulates a player’s financial journey from age 18 to retirement. Players are presented with real-life decisions regarding career paths, investments, and unexpected life events. Every choice made impacts the player's net worth and the trajectory of their life. The goal is to retire with the highest possible financial security and wealth.

## Features

- **Career Paths**: Choose from various careers with differing salary levels, risks, and growth potential.
- **Investment Options**: Invest in stocks, real estate, or savings accounts to grow wealth over time.
- **Random Life Events**: Navigate through unpredictable events like economic downturns, promotions, or emergencies.
- **Decision-Based Gameplay**: Every decision made affects the player's financial situation and life course.
- **Interactive UI**: Text-based interface for immersive storytelling and decision-making.

## How to Play

1. **Start the Game**: Begin your journey at age 18 and make your first financial and career decisions.
2. **Make Key Decisions**: Throughout your life, you’ll make choices regarding jobs, investments, savings, and expenses.
3. **Handle Life Events**: Unexpected life events will occur, which can either help or hinder your financial progress.
4. **Reach Retirement**: Your goal is to retire with the highest net worth and financial security, achieved through strategic decisions and planning.

## Controls

- **Follow Prompts**: The game will display prompts on the screen. Make your choice based on the options provided.
- **Input Values**: Enter numerical values for investments, savings, or other decisions when requested.
- **Help Menu**: Type `'help'` at any point to access the help menu for guidance.
- **Exit the Game**: Type `'stop'` at any time to exit the game and end your session.

## Roadmap

### Planned Future Updates:
- **Enhanced UI**: Improving the interface with better formatting and user experience.
- **More Career Paths and Scenarios**: Adding new career paths and financial scenarios to increase replayability.
- **Advanced Economic Simulations**: Incorporating inflation, market fluctuations, and economic conditions to simulate real-world complexities.

## Technologies

- **Python**: The primary programming language used for the game logic.
- **Colorama**: Provides colored text for enhanced visual feedback and formatting.
- **Random**: Used to simulate random life events and financial occurrences, adding unpredictability to the game.

## Documentation

The game’s logic is written in Python, using randomization to simulate unpredictable life events and decisions. This keeps the game dynamic and ensures no two playthroughs are exactly the same.

### Key Functions:
- **`age18_25()`**: This function handles the player's decisions and life impacts between the ages of 18 and 25. It sets the foundation for the player’s career, investments, and early life choices.
- **`financial_decisions()`**: This is the core function that processes financial and career decisions throughout the game. It includes career choices, investment options, and impacts of life events.
- **`get_choice()`**: A helper function that prompts the player to make a decision and ensures valid input. This is used to gather responses and drive the decision-making process.

## Progression

Players begin their journey at age 18, with decisions about education, career paths, and finances. Over time, they will face different life milestones every five years, where they must make new financial decisions. The game continues until retirement, at which point the player’s wealth and financial security are evaluated.

## Contributors

This project is open for contributions! If you would like to contribute, please fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.

---

Feel free to adjust the roadmap, technologies, and specific functions depending on future developments and any additional details about the game!
