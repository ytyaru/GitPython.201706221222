import git
import os.path

# http://gitpython.readthedocs.io/en/stable/tutorial.html
my_repo = git.repo.base.Repo(path=os.path.abspath(os.path.dirname(__file__)))
print(my_repo.config_reader()) # 使用方法不明
with my_repo.config_writer(): pass

print(my_repo.is_dirty()) # 意味不明。たぶん最新commitと現状ディレクトリとの間に差分があるか否か？
print(my_repo.untracked_files) # github管理されていないファイル一覧と思われる

#with open('repo.tar', 'wb') as f:
#    my_repo.archive(f) # ValueError: Reference at 'refs/heads/master' does not exist

print(my_repo.working_tree_dir)
print(my_repo.git_dir)

print(my_repo.head.ref) # master
# print(my_repo.heads.master) # AttributeError: 'IterableList' object has no attribute 'master'
for head in my_repo.heads: print(head.ref)
#print(my_repo.refs.master) # AttributeError: 'IterableList' object has no attribute 'master'
for tag in my_repo.tags: print(tag)
for ref in my_repo.refs: print(ref.master)

print('active_branch:', my_repo.active_branch)
print('commit:', my_repo.commit)
#print('commit.message:', my_repo.commit.message)

#print(my_repo.submodules)
#print(my_repo.ls_files())
