from git import Repo

repo_dir = '/home/rafael/sources/remote-config'

def has_to_pull():
	repo = Repo(repo_dir)
	commits_behind = sum(1 for c in repo.iter_commits('master..origin/master'))
	if(commits_behind > 0):
		return True
	
	return False

if __name__ == '__main__':
	print(has_to_pull())