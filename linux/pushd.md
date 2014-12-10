## 更高效地在linux 切换目录

先说一下简单的 `cd -` : 用于在最近的两个目录切换，类似电视遥控器的**回看**.

### pushd, popd, dirs: 利用stack 方式管理目录

* `pushd <dir>` 切换到<dir>，同时将<dir>压入stack
* `pushd` 不带参数，回到前一个目录，把栈顶两个目录交换
* `popd` 弹出栈顶目录，退回到前一个目录
* `dirs` 按序列出当前栈中的目录
* `pushd +<n>` <n>是一个数字，切换到stack 的第n 个目录，并把该目录以**循环方式**移到栈顶。栈顶目录为第0个。
* `dirs -v` 列出栈中目录，带序号
* `popd +<n>` 把栈中第n 个目录移除
* `pushd -n <dir>`: 加*-n* 参数，只影响堆栈而不切换目录
* `dirs -c` 清空stack, 当前目录不受影响

默认清空下，当前目录作为栈顶（即stack 有一个元素），此时不能使用 `popd`.

### ubuntu 终端路径太长

看着不爽，修改 ~/.bashrc

将*~/.bashrc* 中*PS1* 的值修改，比如我的是：

```
if [ "$color_prompt" = yes ]; then
PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ '
else
PS1='${debian_chroot:+($debian_chroot)}\u:\W\$ '
fi
```

```
case "$TERM" in
xterm*|rxvt*)
PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \W\a\]$PS1"
```

只需将其中的小写*\w* 改为大写*\W*  (上面的已经改好了)

其他： \u 显示username，\h 显示hostname
