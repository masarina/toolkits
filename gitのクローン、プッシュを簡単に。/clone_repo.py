import os
import subprocess
import pickle

# メールアドレスやIDを設定
git_user = "your_name"
git_email = "your_email.com"

# Gitの設定を反映
subprocess.run(["git", "config", "--global", "user.name", git_user])
subprocess.run(["git", "config", "--global", "user.email", git_email])

# リポジトリのURLを入力
repo_url = input("リポジトリのSSH URLを入力してください (例: git@github.com:user/repo.git): ")

# クローン先のディレクトリ名を決定（リポジトリ名を利用）
repo_name = os.path.basename(repo_url).replace(".git", "")
if not os.path.exists(repo_name):
    os.mkdir(repo_name)

# リポジトリ名とURLをpickleで保存
with open('repo_info.pkl', 'wb') as f:
    pickle.dump({'repo_name': repo_name, 'repo_url': repo_url}, f)

# SSH認証でのクローンを実行
subprocess.run(["git", "clone", repo_url, repo_name])

print(f"リポジトリが {repo_name} にクローンされました。")
