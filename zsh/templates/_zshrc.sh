# ~/.zshrc

# Find and set branch name var if in git repository.
function git_branch_name()
{
  branch=$(git symbolic-ref HEAD 2> /dev/null | awk 'BEGIN{FS="/"} {print $NF}')
  if [[ $branch == "" ]];
  then
    :
  else
    echo ' ('$branch')'
  fi
}

# Enable substitution in the prompt.
setopt prompt_subst

# Config for prompt. PS1 synonym.
prompt='%F{114}%~%f %D{%b-%d-%y} [%T]$(git_branch_name) $ '

# Setting LS colors
export LSCOLORS=ExFxBxDxCxegedabagacad
alias ls='ls -GFh'

# Created by `pipx` on 2021-07-14 16:35:36
export PATH="$PATH:/Users/jomsox/.local/bin"

# Created by `pipx` on 2021-07-14 16:35:36
export PATH="$PATH:/Users/jomsox/Library/Python/3.9/bin"

export JAVA_HOME="/usr/bin/java"

alias t='tree . -I "__pycache__|venv|__init__.py"'
alias monday='~/Repos/timesheet-generator/monday.sh'

