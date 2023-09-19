# Bile Fassinou, Master 2 DIT promotion avril 23
from structure import CreateStructure
from mygit import Gitinitiate

if __name__ == '__main__':

    project_root = '/home/urban/Documents/DITMaster2/DEVOIR/BRANCHES/main' 

    folder = CreateStructure.Structure(project_root)

    folders.method_1()

    strucutres = ['main']

    myDict = {
        'main': project_root,
    }

    for repository, url in myDict.items():
        repo_path = url
        repo_url = 'https://github.com/billfass/devoir_versioning.git'
        branch_name = repository
        commit_message = f'commit pour la première branche dénommée {branch_name}'
        username = 'billfass'
        token = 'votre_token'

        myGit = Gitinitiate.Gitinit(repo_path, repo_url, commit_message, branch_name, username, token)
        myGit.compute()
    

    
