# text-adventure-game
A Text Adventure Game called Neighbourhood Crossing

# Set-up:
  - Download git.
  - Download VS Code (or any editor of your choice).
  - Download and install Python.
  - Add Python extension in VS Code.

# Clone the project to local machine:
  - Open the terminal in your laptopn.
  - Type git -v to check git version (just to check that git is installed).
  - While you're at it also check Python's installed (python3 --version).
  - cd into the directory you want to store the project in.
  - Once in the right directory, type "git clone https://github.com/vnguyen14/text-adventure-game.git" (don't include the quotes).
  - Type "ls" to check that the project folder is successfully cloned (should see text-adventure-game folder).
  - cd into text-adventure-game (type "cd text-adventure-game").
  - Type "code ." to open up the project in VS Code.

# Add, commit and push new changes:
  - Type "git checkout -b name-of-your-new-branch" to move to a new branch if you are in "main" or "production". NEVER EVER work in main or production. The branch name cannot include space or special characters. It's recommended to seperate words with a dash (ex: git checkout -b add-flower-store-room).
  - Once in your new branch, ALWAYS type "git pull origin main" to pull all new changes everyone else has made from main into your new branch BEFORE you start making changes to avoid merge conflicts later. If there are merge conflicts later on in your merge request, you will have to spend extra time to work with me to resolve it to make sure your code and everyone else's code are safe.
  - Make all you changes, start coding, all that jaaz.
  - Type "git status" every once in a while to check all the changes you made.
  - Once done, type "git add ." to add all your changes from local to remote.
    (No sign is good sign, or you can type "git status" again to make sure no changes have not been added. Git will tell you with a very clear message.)
  - Type <git commit -m "Your commit message - just say what you did here"> to commit your changes (do not include the  <> sign, but DO include the quotes for your message in the command).
    If you get the error "Author identity unknown..." the first time you commit, just follow Git's instructions on what to do and you'll be fine. If Git tells you to run something, run it and provide your credentials, you should be good to go!
  - Again, no sign is good sign. Type "git push origin < your-branch-name >" to push your changes to remote (do not include the quotes and <> in the command).

# Create a merge request (MR):
  - Once done pushing your changes, go to Github website.
  - You will likely see a banner at the top saying “your-branch-name had recent pushes some seconds ago” and a “Compare & pull request” green button. Click on that button.
  - Add a title and description of what changes you are trying to merge into main.
  - You’ll need an approval from another team member to be able to merge to main. So send us the link to your merge/pull request to get approval.
  - After being approved, hit the “Confirm Merge” green button.
  - Done! This mean your code is merged into the main branch.

# Rules when working locally and pushing to remote:
Once you've safely opened the project in VS Code and ready to start coding, PLEASE pay attention to these things beforehand:

  - We have 2 very important branches: the main branch which is the default branch where you all merge your code into, and the production branch which is the final version of the game which I will be maintaining. You all should not have any reason to be interacting with "production", if you have to do something with it you're probably doing something wrong, please let me know why and we'll figure something out.
    Again, please DO NOT interact with "production" wihtout my notice. Thank you!
  - NEVER work directly in the main or production branch. If you do and Git doesn't let you commit or push (I put a restriction on this), or checkout to another branch because you have new changes that need to be commit before changing branch, you'll have to be responsible for the possibility of losing your new code. I won't let any incident of accidentally coding over a hundred lines of code spreading in multiple files slide and let you push diredctly in main, you'll have to figure out how to deal with that and make a new branch for your new code, then create a MR as per usual. 
  - So, always, the very first thing you need to do before coding anything, is to always check which branch you are currently in. To do that, just look at the left corner of your VS Code window, where there is a blue button and next to it, is a fork looking icon with the name of the current branch you are in right next to the fork. If it says "main" or "production", immediately do a git checkout to a new branch.
  - DO NOT name any of your new branch as "main" or "master". Git also won't allow branches with same name anyway.
  - DO NOT leave any console log for debug purposed in your code before commit.
