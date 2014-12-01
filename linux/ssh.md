## first use

`ssh-keygen`

You can find the folder *.ssh* in your home path.

## login

`ssh [user@]hostname`

## login without typing password

* create the file *.ssh/authorized_keys* on remote server (if not exist)
* `chmod 644 .ssh/authorized_keys` on remote server (if first use)
* copy the content of *.ssh/id_rsa.pub* on your local machine, paste it to *.ssh/authorized_keys* of remote server

Now you can login to the remote server without typing the passwd.
