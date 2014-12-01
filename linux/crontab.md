## 例行性工作安排

### 管理权限

* /etc/cron.allow 中列的用户可以使用crontab
* 如果cron.allow 不存在，/etc/cron.deny 中列的用户不能使用crontab

### 添加cron 任务

* 列出cron任务：`crontab -l`
* 删除cron任务：`crontab -r`
* 添加/编辑cron任务：`crontab -e`
* 任务格式: `minute hour day month week command`
* hour: 0-23, week: 0-6

e.g.,

* `* * * * * test` : 每天每分钟都执行*test*命令
* `5 * * * * test` : 每个小时零5分钟时执行*test*命令
* `*/2 * * * * test` : 每两分钟执行*test*命令
* `0,30 18-23 * * * test` : 每天18:00~23:00 之间的整点、半点执行*test*
* `10 1 * * 6,0 test` : 每周六、日的1:10 执行*test*
