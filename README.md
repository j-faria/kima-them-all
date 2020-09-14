# kima-them-all

[![status](https://api.shippable.com/projects/5cadbabcdaf54c0007d257f6/badge?branch=master)]()


## Steps

First, clone this repository

```
git clone https://github.com/j-faria/kima-them-all.git
cd kima-them-all
```

Then, checkout a new branch from master (change "mybranch" to whatever you want):

```
git checkout -b mybranch --track origin/master
```

This will checkout a new branch called myownbranch that is a copy of master. Using the --track option makes sure that the upstream source branch is written in your .git/config file. This will allow git-pull-request to know to which branch send the pull-request.