from git import Repo

repo_dir = '/home/rafael/sources/remote-config'

def has_to_fetch():
	repo = Repo(repo_dir)
	commits_behind = sum(1 for c in repo.iter_commits('master..origin/master'))
	if(commits_behind > 0):
		return True
	
	return False

def fetch():
	repo = Repo(repo_dir)
	remote = git.remote.Remote(repo, 'origin')
	remote.fetch()

if __name__ == '__main__':
	if(has_to_fetch()):
		print('FETCH')
		fetch()
	else:
		print('NOTHING')