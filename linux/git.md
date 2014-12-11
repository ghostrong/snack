### how to use git

**used to check git help:**  `git help <command>`

e.g., `git help checkout`

**Remember three concepts: working dir  ->  index stage  -> HEAD**

* edit a file, we are in **working dir**
* add the changes to **index stage**
* after commit, it's the **HEAD**

**init a new repo**

```
$ mkdir <repo>
$ cd repo
$ git init
```

**clone a repo**

```
$ git clone <addr>
```

**add changes**

```
$ git add <filename>
$ git commit -m"<message>"
```

or

```
$ git commit -am"<message>"
```

**check the changes**

```
$ git diff <filename>  # do this before add
$ git diff HEAD <filename> # do this before commit
```

*If it's a new file(first created), then must do "git add <filename>"*

**add remote server**

```
$ git remote add origin <addr>
$ git remote -v  # check the current remote value
```

**change remote server**

```
$ git remote set-url origin <addr>
```

```
$ git remote rm origin
$ git remote add <addr>
```

**create a new branch**

```
$ git branch <branch>  # create a new branch (no switch)
$ git checkout -b <branch>  # create and switch to a new branch
$ git branch  # show the current work branch
$ git checkout <branch>  # change the work branch
$ git merge <branch>  # merge the branch
$ git branch -d <branch>  # delete a work branch
$ git branch -D <branch>  # force delete a branch (before merge)
```

If found conflicts after merge, we need fix the conflicts mannually.

**push to remote**

```
$ git push origin master   # push to master branch
$ git push origin <branch>  # push to any <branch>
$ git push origin <branch>:<remote_branch_name>  # a new name in remote server
$ git push origin :<remote_branch_name>  # delete the remote branch
```

**pull**

```
$ git pull  # update the local repo
```

**undo the changes**

```
$ git checkout -- <filename>   # do this before add
$ git reset HEAD <filename>   # do this before commit (after add), then also need do "git checkout -- <filename>"
```

**go back to earlier version**

```
$ git reset --hard HEAD^  #  back to last version
$ git log  #  check every commit info, you can find commit_id here
$ git reset --hard <commit_id>  # back to the specified version
```


