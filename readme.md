# PyWeb

-----------------


Sometimes you want to access stuff in a web browser that you have locally on your computer, such as a draft copy of your blog, an offline cache of Wikipedia, or whatever else. *PyWeb* makes that easy.

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

**Usage:**
```
pyweb --help
usage: pyweb [-h] [--port PORT] [--www-root WWW_ROOT] [--log-path LOG_PATH]

optional arguments:
  -h, --help           show this help message and exit
  --port PORT          TCP port to listen on.
  --www-root WWW_ROOT  WWW root path to serve from.
  --log-path LOG_PATH  Directory to write logfiles to.
```

**Defaults:**

`WWW_ROOT` defaults to `~/.pyweb/var/www`
`LOG_PATH` defaults to `~/.pyweb/var/log`
`PORT` defauls to `8080`


Test your configuration:

```
$ pyweb --port <your port> --www-root /path/to/content/root --log-dir /path/to/log/dir
```

Assuming content loads in your browser, you can set pyweb to run at log in. On a Mac, edit `pyweb.plist` to make sense for you, and copy it to `~/Library/LaunchAgents/`.

On Linux, you can probably have it run as a cron job or similar.

*PyWeb* doesn't daemonize because daemonizing is deprecated under `launchd`. If you need it to daemonize, you can probably use the [daemon(1)](http://www.libslack.org/daemon/) command.

### Adding content

There's a command-line utility to add content into your `WWW_ROOT`.

**Usage:**
```
$ pyweb-add-content --help
usage: pyweb-add-content [-h] [--www-root WWW_ROOT] [--log-path LOG_PATH]
                         content_src_dir content_dst_dir

positional arguments:
  content_src_dir      Source directory containing content to be intalled.
  content_dst_dir      Name of directory under <WWW-ROOT> for content to be
                       located.

optional arguments:
  -h, --help           show this help message and exit
  --www-root WWW_ROOT  WWW root path to install to.
  --log-path LOG_PATH  Directory to write logfiles to.
```

The default values are the same as for `pyweb`.

**Example:**

```
$ pyweb-add-content ./python-3.7.3-docs-html python/python-3.7.3-docs-html
Installing ./python-3.7.3-docs-html
Logging to /Users/zach/.pyweb/var/log/pyweb-installer.log
Installation complete.
```

### Questions

**Q:** You know you can just use `python -m SimpleHTTPServer`, right?  
**A:** Yes.

**Q:** Having a webserver running 24/7 out of your home directory is a terrible idea.  
**A:** That's not actually a question, but I'll address it anyway. *Is* it a terrible idea? I honestly don't know, but I think as long as it only binds to `localhost` it's probably okay. If it's not and you can show me, I'd like that. I'll learn something in the process.

**Q:** Why do you need to serve content to yourself out of your home directory?  
**A:** It's probably just me, but I have a variety of stuff cached offline that I'd like to view in a web browser, such as [Python documentation](https://docs.python.org/3/download.html), and I'd like to have it available all the time without thinking about it, even when I'm away from the internet.
