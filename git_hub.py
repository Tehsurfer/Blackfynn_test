#git_hub.py is used to update all github file for the git projec: 'ABI_test'
# from here Netlify builds the webpage to display at https://inspiring-turing-db6fbf.netlify.com/
import base64
from github import Github
from github import InputGitTreeElement


class git_hub:
    def __init__(self):
        pass

    def update(self):
            user = "Tehsurfer"
            password = "*********************************"
            g = Github(user,password)
            repo = g.get_user().get_repo('ABI_test_site')
            file_list = [
                'data.js',
            ]

            file_names = [
                'data.js',
            ]

            commit_message = 'python update'
            master_ref = repo.get_git_ref('heads/master')
            master_sha = master_ref.object.sha
            base_tree = repo.get_git_tree(master_sha)
            element_list = list()
            for i, entry in enumerate(file_list):
                with open(entry) as input_file:
                    data = input_file.read()
                if entry.endswith('.png'):
                    data = base64.b64encode(data)
                element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
                element_list.append(element)
            tree = repo.create_git_tree(element_list, base_tree)
            parent = repo.get_git_commit(master_sha)
            commit = repo.create_git_commit(commit_message, tree, [parent])
            master_ref.edit(commit.sha)
