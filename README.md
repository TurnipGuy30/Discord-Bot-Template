# Discord Bot Template

## Setup

### Local
If running from your computer:
1. Clone this Repository.
2. Create a file called `.env` in the root folder, with `main.py` and the other files.
The `.env` file should look like this:
```
DISCORD_TOKEN = <token>
```
Replace `<token>` with your Discord Bot Token.

Once that's done, run `main.py`. You should see a log that says "_User_ has connected to Discord"; this means your Bot user is online!

### Online
If running online:
1. Go to [Replit.com](https://replit.com) and log in.
2. Create a new Replit and edit the name and description.
3. Clone this Repository and add all the files to the Replit's library.
4. Make an environment variable called `DISCORD_TOKEN` with your Discord Bot Token inside.
5. If you want to have the Bot run after the tab is closed, set `Always On` to true in the Replit settings.
7. Click the big `Run` button at the top. After the Python libraries download, you should see a message in the log that says "_User_ has connected to Discord". If your Bot user appears online and you turned on `Always On`, you  may now safely close the tab.

If it doesn't work, make sure the `.replit` file looks like this:
```
run="python main.py"
language="python3"
onBoot="echo Booting up!"

[packager]
ignoredPaths=[".git"]
```

If everything went smoothly, congratulations! But if you need more help, please create an Issue or Discussion and I'll try to get back to you.

### Thanks for using my guide!
