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

Create a new directory for the **kima** analysis.
You can do this with the `kima-template` if you have _pykima_ installed

```
kima-template RunThisDirectory
```

or by hand

```
mkdir RunThisDirectory
```

Now you need to (create and) edit a `kima_setup.cpp` file inside
RunThisDirectory, as well as an `OPTIONS` file.

Add your data file inside the folder (the same one referenced in the
`kima_setup.cpp`).

Do a pull request, after installing [this tool](https://github.com/jd/git-pull-request)

```
( pip install git-pull-request )
git pull-request
```

That's it, GH will now run **kima** on your files.