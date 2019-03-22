# Bash Tools Kit

## db tool

This utility allows you to **export** a collection data from one of the RIGS environments; `staging` | `production`.

Also allows you to **import** the previous generated json data to a local database.

### Setup 

Once you download the repository, create a symlink to the command inside your local bins path:

```
$ ln -s __path_of_repo__/db /usr/local/bin/db
```

Then open your `~/bash_profile` and export the following env vars:

```
export RIGS_DB_BAKS=__path_to_store_jsons__
export RIGS_BINS_DOCS_PATH=__path_of_repo__/docs
```

### Usage:

**Export**: 

`db --export -h production -d business -c user -f users.json`
`db --export -h production -d business -c order -f orders.json`

**Import**

`db --import -h local -d business -c user -f users.json`
`db --import -h local -d business -c order -f orders.json`