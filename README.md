# Quiz App (Geography quiz)
A Quiz app that we built for questioning users on geology quiz

Try out demo [here](http://geoquiz-revuc.herokuapp.com/?fbclid=IwAR3SM85OOrKub25GHhKvaljLK7hmw7O0HMwNkXclK4BXrayl1rOUTadeqx8)

## Setup
Activate virtual environment (venv) in project
For Mac/Linux
```bash
. source/env/activate
```

For Windows(maybe, check official document)
```bash
.\venv\Scripts\activate
```

Use pip package manager to install all dependcies that have been stored in requirements.txt
```bash
pip install -r requirements.txt
```

## Usage (Start development server)
In the directory, run:
```bash
python3 app.py
```
And navigate to the URL stated on the terminal window

## Steps by steps in development
1. Always develop when in virtual environment first.
Run commands above to get into virtual env, signal with (venv) prefix in the terminal

2. Pull the latest changes on repository before working on your change
```bash
$ git pull
```

3. Create a new, seperate branch on your local machine before making changes.

* Check what branch you're on
```bash
$ git branch
```

* Create new branch
```bash
$ git checkout -b [name_of_your_new_branch]
```

* Navigate to your branch
```bash
$ git checkout [name_of_your_new_branch]
```

* When you're done, push your changes to github
```bash
$ git push
```

* Delete your local branch if you don't do anything else on your local
```bash
$ git branch -d [name_of_your_new_branch]
```

* Go to remote repository and make a pull request to merge into the final source code. Remember: **There must be 2 reviewers for the PR to be merged. And don't push to master branch directly**

## Contributors

This project is an effort of 4 members:

* [Bao Huynh](https://github.com/baohuynhlam)
* [Triet Pham](https://github.com/chrispham0502)
* [Thanh Nguyen](https://github.com/nhanthanh-bot)
* [Giang Ta](https://github.com/gianghta)
