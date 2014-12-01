import datetime

now = datetime.datetime.now()
with open('/home/rxs/workspace/github_repo/snack/linux/test.out', 'a') as f:
    f.write(str(now) + '\n')
