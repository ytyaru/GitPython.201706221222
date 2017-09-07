import git
import os.path
my_repo = git.repo.base.Repo(path=os.path.abspath(os.path.dirname(__file__)))

# GitPythonには`git add -n .`に該当するコマンドがない
# https://stackoverflow.com/questions/31540449/how-to-check-if-a-git-repo-has-uncommitted-changes-using-python

df = my_repo.index.diff(None)
print(df)
for a in df: print(a)
#print(dir(df))
#print(df.change_type)

#print(my_repo.git.status())
print(my_repo.untracked_files) # github管理されていないファイル一覧と思われる

# https://github.com/gitpython-developers/GitPython/issues/292
# A: 未登録や変更があったファイルをadd対象にする
# n: addを実行しない。addしたときの出力を返す
#my_repo.git.add(n=True, A=True) 
#my_repo.git.add(A=True)

print(my_repo.git.status())
#print(my_repo.git.log())

