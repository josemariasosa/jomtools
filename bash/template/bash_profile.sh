# Global Variables
export REVER_SETTINGS=$HOME/.rever/credentials
alias deply='/Users/josemaria/Maria/Repositories/jomtools/python/tools/deply/deply.sh'

# Setting Visual Git Branch
function parse_git_branch {
  echo -n $(branch_color) && git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/' -e 's/^/ փ /'
}
function parse_git_branch_length {
  git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/' | wc -c
}
function parse_pwd_length {
  pwd|wc -c|tr -d ' '
}
function parse_pwd {
  pwd
}
function prompt_command {
    # get branch string length
    branchLength=$(parse_git_branch_length)
    let "branchLength=$branchLength"
    pwdLength=$(parse_pwd_length)
    let "pwdLength=$pwdLength"
    # create a $fill of all screen width minus the time string and a space: AAANNNDDDD git branch
    let fillsize=${COLUMNS}-11-$branchLength-pwdLength
    fill=""
    while [ "$fillsize" -gt "0" ]
    do
        fill="-${fill}" # fill with underscores to work on
        let fillsize=${fillsize}-1
    done
}
PROMPT_COMMAND=prompt_command
function branch_color {
    if [[ $(git branch --no-color 2> /dev/null | sed -e '/^[^*]/d') == *master* ]]
    then
      echo -e '\033[00m\033[0;31m'
    else
      echo -e '\033[00m\033[0;32m'
    fi
}
# Reset color for command output
# (this one is invoked every time before a command is executed):
trap 'echo -ne "\033[00m"' DEBUG
# Git completion
if [ -f $(brew --prefix)/etc/bash_completion ]; then
    . $(brew --prefix)/etc/bash_completion
fi
fill="-"
reset_style='\[\033[00m\]'
status_style=$reset_style'\[\033[0;37m\]'
prompt_style=$reset_style
command_style=$reset_style'\[\033[0;33m\]'
# Prompt variable:
PS1='\n\[\e[0;34m\]$(parse_pwd)'"$status_style"' $fill$(parse_git_branch)'"$status_style"' \t\n'"$prompt_style"'\[\e[1;34m\]>\[\e[m\]'"$command_style "
capture() {
    sudo dtrace -p "$1" -qn '
        syscall::write*:entry
        /pid == $target && arg0 == 1/ {
            printf("%s", copyinstr(arg1, arg2));
        }
    '
}

# Setting LS colors
export LSCOLORS=ExFxBxDxCxegedabagacad
alias ls='ls -GFh'

# Setting PATH for Sublime 3
export PATH=/usr/local/bin:$PATH
export PATH

# Setting PATH for Python 3.7
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.7/bin:${PATH}"
export PATH
