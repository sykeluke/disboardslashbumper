[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
# About:
Discord Auto Bumper (Slash Commands) for Disboard made with Discum & Discord.py.
Automatically sends slash commands in a channel every 2 hours (With a bit of random delay to not get detected).
Use at your own risk. Selfbots are against Discords ToS and can get your account banned.
# How To Get Started.
# 1.
Click the Deploy to Heroku button. (do not add to pipeline while deploying)
# 2.
Go to your application `Settings` -> Click Reveal Config Vars -> Make a Variable named `token` (no caps) with the value as your Discord Token. (click [here](https://www.youtube.com/watch?v=YEgFvgg7ZPI) for a tutorial on how to get it) -> Make a Variable named `guild_id` (no caps) with the guild id of the server you want the bot to send commands to -> Make a Variable named `channel_id` (no caps) with the channel id of the channel you want the bot to send commands to.
# 3.
Go to the `Resources` page on your application -> Click the `Pencil Icon` -> Turn the button on. (turns the bumper on)
# Additional Info
Click the `More` button in Heroku then click `View logs` for more information about the bumper, including when it sends a command. To turn off the bumper just turn off the button in step `3`.
