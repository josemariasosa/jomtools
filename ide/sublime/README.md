# Sublime

## 1. Sublime Setup

### Installing Sublime

The first thing you need to do is to download Sublime from the [web site](https://www.sublimetext.com/).

### Set up Sublime in the Terminal for Mac

Following the steps listed by the article [Launch Sublime Text 2 or 3 from the Mac OSX Terminal](https://ashleynolan.co.uk/blog/launching-sublime-from-the-terminal).

Type the following commands in the terminal.

For **Sublime Text 2**:

```bash
open /Applications/Sublime\ Text\ 2.app/Contents/SharedSupport/bin/subl
```

For **Sublime Text 3**:

```bash
open /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl
```

The used command should open up the editor when you type it into the Terminal. If that worked, you're good to go.

Now, you need to create a symlink called `sublime` which links the subl CLI to a folder where your system usually looks to execute these binaries. For further information about **symlinks**, go to the [Bash Documentation](https://github.com/josemariasosa/jomtools/tree/master/bash#how-to-create-and-use-symbolic-links). To do this, type in:

For **Sublime Text 2**:

```bash
ln -s /Applications/Sublime\ Text\ 2.app/Contents/SharedSupport/bin/subl /usr/local/bin/sublime
```

For **Sublime Text 3**:

```bash
ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/sublime
```

The final thing you need to do, is to check that your system profile is looking in the right place to see the symlink you have just created.

Enter the following command into your Terminal:

```bash
nano ~/.bash_profile
```

This should open up your profile in a text editor. What you’re looking for is a line towards the top of the file that starts with `export PATH=`. Your `PATH` contains all the directories that will be checked for executable binaries when you type a command into your Terminal. Since we created a symlink in the `/usr/local/bin` folder, we want to make sure that that folder is being checked too.

From the [bash profile template](https://github.com/josemariasosa/jomtools/blob/master/bash/template/bash_profile.sh), make sure the `PATH` is exported.

```bash
# Setting PATH for Sublime 3
export PATH=/usr/local/bin:$PATH
export PATH
```

Finally, if you did have to add `/usr/local/bin` to your `PATH`, run the following command before continuing:

```bash
source ~/.bash_profile
```

This will reload your `.bash_profile` with the newly added directory in your `PATH`.

In your Terminal, the following commands should now work:

1. `sublime .` – opens the current directory in Sublime.
2. `sublime filename` – opens a file where filename is the file to be opened.
3. `sublime foldername` – opens a folder where foldername is the folder to be opened.

