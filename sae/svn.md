## SAE use svn for code deployment

用户名/密码是SAE 安全邮箱和安全密码。

````
svn checkout https://svn.sinaapp.com/appname
cd appname/1
touch README.md
svn add README.md
svn commit -m"add README"
````

````
svn update
````


