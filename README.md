# kima-them-all

![kima-them-all](.img/kima-them-all.png)

This repository is an experiment in using GitHub actions to run
[**kima**](https://github.com/j-faria/kima) jobs.  
The idea is simple. Everyone can submit a pull request to the repository. The PR
should add a new directory containing a **kima** project (basically a
`kima_setup.cpp` and `OPTIONS` files together with some data). A GitHub action
is triggered to run **kima** on the new folder and produce a report.


**Important Notes**

- the repository is public, as is all the data submitted in a pull request
- there are some limits on the time a job can take (a few hours)


<br>

---

### Step-by-step


First, clone this repository

```
git clone https://github.com/j-faria/kima-them-all.git
cd kima-them-all
```

Then, checkout a new branch from master  
→ change "mybranch" to whatever you want, typically the name of a star or some
project identifier

```
git checkout -b mybranch --track origin/master
```

Create a new directory for the **kima** analysis.
You can do this with the `kima-template` script if you have _pykima_ installed

```
kima-template RunThisDirectory
```

or by hand

```
mkdir RunThisDirectory
```

Now you need to (create or) edit a `kima_setup.cpp` file inside
RunThisDirectory, as well as an `OPTIONS` file.
More information can be found in **kima**'s documentation 
[here](https://github.com/j-faria/kima/wiki/Getting-started) and 
[here](https://github.com/j-faria/kima/wiki/Changing-OPTIONS).

Add your data file inside the folder (the same one referenced in the
`kima_setup.cpp`).

Do a pull request, e.g. after installing [this
tool](https://github.com/jd/git-pull-request)

```
( pip install git-pull-request )
git pull-request
```

That's it, GitHub will now run **kima** on your files.
