# Git Teamwork

## Virtual environment setup
1. Clone a repository from gitlab.com to your local computer:
 ```bash
1. git clone git@gitlab.com:DawidO/wsb-to-page-object-python.git 
```
2. Create and activate virtual environment:
```bash
2. venv-install.bat
```
3. Install all dependencies:
```bash
3. pip install -r requirements.txt

```
## Using branches in git
1. Create a new branch and switch to it:
```bash
1. git checkout -b branch-name
```
Branch naming convention:

<img src="https://deepsource.io/images/blog/git-branch-naming-conventions/branch-naming-example.png" alt="MarineGEO circle logo" style="height: 100px; width:500px;"/>

Issue id can be found in issues/boards in Gitlab

<img src="https://about.gitlab.com/images/blogimages/connect-milestone.png" alt="MarineGEO circle logo" style="height: 200px; width:500px;"/>

2. Pushing changes to Gitlab

    When you are ready to add your code:
```commandline
git add --all
git commit -m "commit message"
git push -u origin branch-name
```
 To update a local repository from the corresponding remote repository:

```commandline
git pull origin master
```

3. Creating merge requests

    GitLab prompts you with a direct link for creating a merge request

```commandline
remote: To create a merge request for branch-name visit:
remote:   https://gitlab.com/DawidO/.... 
```
4. Update your local project

After successful merging switch to master branch:

````commandline
git checkout master
````
To update local copy with the latest changes:
```commandline
git pull
```

5. Delete old branch

```commandline
git branch -D branch-name
```