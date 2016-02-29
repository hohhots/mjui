#Run initPackages.sh first to install required packages in ubuntu.

from __future__ import with_statement
from fabric.api import env, local, run, lcd, cd, sudo
import os
from fabric.contrib.files import sed

env.hosts = ['pi@192.168.3.254:22']

srcDir = 'src'
libDir = 'lib'

localLibDir = srcDir + '/' + libDir
cssSandPaperDir = 'cssSandPaper'

gitIgnoreGlobal = 'gitignoreGlobal'
gitAlias = [ 'user.name  brgd', 'user.email hohhots@gmail.com', 'push.default matching',
             'branch.autosetuprebase always', 'core.editor \'emacs -fs\'', 'color.ui true',
             'color.status auto', 'color.branch auto', 'alias.co checkout',
             'alias.ci commit', 'alias.st status', 'alias.xfetch \'fetch origin\'',
             'alias.xdiff \'diff origin master\'', 'alias.xmerge \'merge origin master\'',
             'alias.xpull \'pull origin master\'', 'alias.xpush \'push origin master\'',
             'alias.br branch', 'alias.type \'cat-file -t\'', 'alias.dump \'cat-file -p\'',
             'alias.hist \'log --pretty=format:%h-%ad-|-%s%d-[%an] --graph --date=short\'',
             'core.excludesfile \'~/.' + gitIgnoreGlobal + '\'' ]

devTools = [ 'brackets','git' ]

libDir = 'lib'
dojoSubDirs = [ 'dojo','dojox','dijit','util','docs','demos' ]

dojoGit = 'https://github.com/dojo/'
cssSandPaperGit = 'https://github.com/zoltan-dulac/'

def localGitConfig():
    for alias in gitAlias:
        local('git config --global ' + alias)
    hd = os.path.expanduser("~") + '/.' + gitIgnoreGlobal
    if os.path.exists(hd):
    	local('rm ' + hd)
    local('cp -r ' + gitIgnoreGlobal + ' ' + hd) #copy gitignoreGlobal to user direcroty

def localPullAll():
    local('git pull --all')

def localMjuiPull():
    localPullAll()

def localPull(sdir, ddir):
    a = libDir + '/' + ddir
    if not os.path.exists(a):
        local('git clone ' + sdir + ddir + '.git ' + a)
    else:
        with lcd(a):
            print bcolors.OKGREEN + "Directory - " + a + bcolors.ENDC
            localPullAll()    

def localDojoPull():
    for dir in dojoSubDirs:
        localPull(dojoGit, dir)

def localCssSandPaperPull():
    localPull(cssSandPaperGit, cssSandPaperDir)
        
def gitPull():
    localMjuiPull()
    localDojoPull()
    localCssSandPaperPull()
    
    
def setup(): #setup mjui project
    localGitConfig()
    gitPull()

def localPush():
    local('git push') # runs the command on the local environment
    
def piPull():
    with cd('/home/pi/myProject/mjui'):
        run('git pull') # runs the command on the remote environment
        sudo('initPackages.sh')
        run('fab gitPull')
    
def done():
    #push to github from local
    localPush()

    #pull from github in pi
    piPull()
    
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'