import os
import sys
import subprocess
import shutil

PR_branch = os.environ['HEAD_BRANCH']
BASE_branch = os.environ['BASE_BRANCH']
BUILD_DIR = os.environ['SHIPPABLE_BUILD_DIR']


def new_directories():
    cmd = 'git --no-pager diff --name-only %s -- runs' % BASE_branch
    out = subprocess.check_output(cmd.split()).decode().strip()
    out = out.split('\n')[0]

    directory = os.path.dirname(out)
    # print('Found new directory "%s"' % directory, flush=True)

    return directory


def check_directory(directory):
    wd = os.getcwd()
    os.chdir(directory)

    if (not os.path.exists('OPTIONS') or not os.path.exists('kima_setup.cpp')):
        msg = 'One of "OPTIONS" or "kima_setup.cpp" is missing in your folder'
        raise ValueError(msg)

    kimadir = os.path.join(BUILD_DIR, 'kima')
    src = os.path.join(kimadir, 'pykima', 'template', 'Makefile')
    with open(src) as f:
        m = f.read().format(kimadir=kimadir)
    dst = 'Makefile'
    with open(dst, 'w') as f:
        f.write(m)

    os.chdir(wd)

def create_template(directory):
    wd = os.getcwd()
    os.chdir(directory)
    if os.path.exists('NEEDSTEMPLATE'):

        options_exists = False
        if os.path.exists('OPTIONS'):
            shutil.move('OPTIONS', 'OPTIONS.bak')
            options_exists = True

        os.system('kima-template')

        if options_exists:
            shutil.move('OPTIONS.bak', 'OPTIONS')

        os.remove('run')

    os.chdir(wd)


def run_kima(directory):
    wd = os.getcwd()
    os.chdir(directory)

    os.system('make')

    cmd = os.path.join(BUILD_DIR, 'run')
    os.system(cmd)

    cmd = 'jupyter nbconvert --to notebook %s/templates/report.ipynb --output-dir .' % BUILD_DIR
    os.system(cmd)
    cmd = 'jupyter nbconvert --to notebook --execute report.ipynb
    os.system(cmd)

    os.chdir(wd)


def push_results(directory):
    wd = os.getcwd()
    os.chdir(directory)

    os.system('git checkout %s' % PR_branch)
    os.system('git add report.ipynb')
    os.system('git commit -m "ran kima on PR files, hope it is ok... [ci skip]"')
    os.system('git push origin %s' % PR_branch)
    #
    # - git config user.email "joao.faria@astro.up.pt"
    # - git config user.name "João Faria"
    # - git config --global push.default simple
    # - git remote set-url origin git@github.com:j-faria/kima-them-all.git

    # - git add reports
    # - git commit -m "shippable output [ci skip]"
    # - git push
    #
    os.chdir(wd)


if __name__ == "__main__":
    directory = new_directories()
    
    if 'push' in sys.argv:
        push_results(directory)
    else:
        check_directory(directory)
        run_kima(directory)