import git
import os.path
my_repo = git.repo.base.Repo(path=os.path.abspath(os.path.dirname(__file__)))

print(my_repo.config_reader())
print(dir(git.config.GitConfigParser))
print(my_repo.config_reader().read())
# git config --local user.name {0}
#g = git.cmd.Git('/usr/bin/git')
#g.
#my_repo.git.config('--local username {0}'.format('ytyaru'))
#my_repo.git.config('--local username {0}'.format('ytyaru'))

