# Meme Generator Discord Bot

This repository contains a Discord bot that enables users to create custom memes by adding text to images. The bot offers a variety of templates to choose from and the option to upload personal images for meme generation. The generated memes can then be shared and enjoyed within the Discord server.

## Prerequisites

Before utilizing the bot, make sure you have the following dependencies installed:

- Python 3.x
- Discord.py library (`pip install discord.py`)
- Pillow library (`pip install Pillow`)

## Getting Started

1. Clone this repository to your local machine.
2. Create a `token.txt` file in the same directory as your code and place your Discord bot token inside.
3. Customize the `Templates` dictionary found in `storage.py` by adding or modifying meme templates.
4. Execute the main script by using the command `python main.py`.

## Usage

1. Invite the bot to your Discord server.
2. Type `!help` in any text channel to access information regarding available commands.

### Commands

- `!image`: Upload an image and follow the prompts to incorporate text onto it.
- `!templates`: View the assortment of available meme templates.
- `!choose [template_name]`: Choose a meme template from the provided options.
- `!textup [upper_text]`: Append upper text to the selected image.
- `!textdown [lower_text]`: Append lower text to the chosen image.
- `!meme`: Generate the final meme with the added text.
- `!Print my memes`: Retrieve and display all memes created by you.

## Files and Modules

- `main.py`: Encompasses the primary bot logic and event handlers.
- `pillow.py`: Defines functions for creating memes utilizing the Pillow library.
- `storage.py`: Houses classes and data structures for storing meme-related data.

## Contributing

Contributions are encouraged! If you have any ideas or improvements, don't hesitate to fork this repository, make your enhancements, and create a pull request.
