from __future__ import with_statement
from fabric.api import env, local, run, lcd, cd, sudo
import os
from fabric.contrib.files import sed

env.hosts = ['pi@192.168.3.254:22']

srcDir = 'src'
libDir = 'lib'

localLibDir = srcDir + '/' + libDir

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

tools = ['brackets']

def installTools():
    for tool in tools:

        local('sudo apt-get install ' + tool)

def localGitConfig():
    for alias in gitAlias:
        local('git config --global ' + alias)
    hd = os.path.expanduser("~") + '/.' + gitIgnoreGlobal
    if os.path.exists(hd):
    	local('rm ' + hd)
    local('cp -r ' + gitIgnoreGlobal + ' ' + hd) #copy gitignoreGlobal to user direcroty

def gitPull():
    localGitConfig()
    
def setup(): #setup mjui project
    installTools()
    gitPull()
    
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'