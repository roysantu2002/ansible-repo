from github import Github

#github generated access token
access_token = ""

# # using an access token
# g = Github(access_token)

#login with access token
login  = Github(access_token)

#get the user
user  = login.get_user()

#get all repositories
my_repos = user.get_repos()

#create repository
new_repo = user.repo('roysantu2002/ansible-repo')
#create new file
new_repo.create_file("New-File.txt", "new commit", "Data Inside the File")

# for repository  in my_repos:
#     print(repository)
# repo = g.get_repo('https://github.com/roysantu2002/ansible-repo')
# all_files = []
# contents = repo.get_contents("")
# print(contents)


# Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# To initiate new Git repo in the mentioned directory
# repository = g('https://github.com:roysantu2002/ansible-repo.git')
#
#
# # repo = git.Repo('https://github.com:roysantu2002/ansible-repo.git')
#
# print(repository.git.status())