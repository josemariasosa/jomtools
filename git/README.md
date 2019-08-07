# Git

## 1. Git Setup

The complete tutorial belongs to Atlassian, and can be seen [here](https://www.atlassian.com/git/tutorials/install-git).

### Install Git on Mac OS X

The easiest way to install Git on a Mac is via the stand-alone installer:

1. Download the latest [Git for Mac installer](https://sourceforge.net/projects/git-osx-installer/files/).

2. Follow the prompts to install Git.

3. Open a terminal and verify the installation was successful by typing git --version:

```bash
$ git --version
git version 2.9.2
```

4. Configure your Git username and email using the following commands, replacing Emma's name with your own. These details will be associated with any commits that you create:

```bash
$ git config --global user.name "Emma Paris"
$ git config --global user.email "eparis@atlassian.com"
```

5. (Optional) To make Git remember your username and password when working with HTTPS repositories, configure the git-credential-osxkeychain helper.

### Install the git-credential-osxkeychain helper

Bitbucket supports pushing and pulling your Git repositories over both SSH and HTTPS. To work with a private repository over HTTPS, you must supply a username and password each time you push or pull. The git-credential-osxkeychain helper allows you to cache your username and password in the OSX keychain, so you don't have to retype it each time.

1. If you followed the MacPorts or Homebrew instructions above, the helper should already be installed. Otherwise you'll need to download and install it. Open a terminal window and check:

```bash
$ git credential-osxkeychain
usage: git credential-osxkeychain <get|store|erase>
```

If you receive a usage statement, skip to step 4. If the helper is not installed, go to step 2.

2. Use curl to download git-credential-osxkeychain (or [download it via your browser](http://github-media-downloads.s3.amazonaws.com/osx/git-credential-osxkeychain)) and move it to /usr/local/bin:

```bash
$ curl -O http://github-media-downloads.s3.amazonaws.com/osx/git-credential-osxkeychain
$ sudo mv git-credential-osxkeychain /usr/local/bin/
```

3. Make the file an executable:

```bash
$ chmod u+x /usr/local/bin/git-credential-osxkeychain
```

4. Configure git to use the osxkeychain credential helper.

```bash
$ git config --global credential.helper osxkeychain
```

The next time Git prompts you for a username and password, it will cache them in your keychain for future use.

## 2. Remote Repository

### Eliminate old remote and add a new one.

Remove and replace the remote repository.

```bash
$ git remote -v
$ git remote remove origin
$ git remote add origin git@bitbucket.org:rigsteam/comments_sanitizer.git
```