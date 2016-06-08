# GIT GROUP

The problem this script solves is nicely described at
"Multiple working folders with single GIT repository":http://finik.net/2010/10/24/multiple-working-folders-with-single-git-repository/

The solution is more or less a copy of that.

## Installation

Add the _bin_ directory to your path, or perhaps use basher:

``` bash
basher install PeterHancock/git-group
```

## Usage

To create a git group

``` bash
git group git@github.com:$user/$project.git
```

To create a new working copy $dev

``` bash
git group-add $dev
```
