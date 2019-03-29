# PyWeb
-------
Sometimes you want to access stuff in a web browser that you have locally on your computer, such as a draft copy of your blog or an offline cache of Wikipedia, or whatever else. *PyWeb* makes that easy.

*PyWeb* is intentionally limited and was designed with the following considerations:

- Content directory is live while the server is running, which is probably while you're logged in.
	- Files copied there are available instantaneously
- *Only* bind to `127.0.0.1`, because you shouldn't be serving a website out of your home directory to the world.
	- If you *do* want to do that, this isn't the web server for you
- Starts when you log in and runs in the background, so you don't have to think about it.
- Very few configurable parameters:
	- Root directory for web content
	- Log path
	- TCP Port to listen on

If you want to run this from macOS, there's a launchd plist to edit and copy to `~/Library/LaunchAgents`.

### Installing

```
$ git clone https://github.com/zcutlip/pyweb.git
$ cd pyweb
$ pip3 install --user .
$ mkdir /path/to/content/root /path/to/log/dir
```

### Running

Test your configuration:

```
$ pyweb --port <your port> --www-root /path/to/content/root --log-dir /path/to/log/dir
```

If content loads in your browser, you can set pyweb to run at log in. On a Mac, edit `pyweb.plist` to make sense for you, and copy it to `~/Library/LaunchAgents/`

On Linux, you can probably have it run as a cron job or similar.

PyWeb doesn't daemonize because daemonizing is deprecated under `launchd`. If you need it to daemonize, you can probably use the [daemon(1)](http://www.libslack.org/daemon/) command.


