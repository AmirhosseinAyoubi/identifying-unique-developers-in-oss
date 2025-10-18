from git import Repo
import shutil
import csv
import pandas as pd
import os
from DataClean import DataClean

class DataExtract(DataClean):
    def __init__(self, repo_urls):
        super().__init__()

        # Project base directory
        self.__base_dir = os.path.dirname(os.path.abspath(__file__))
        self.__project_root = os.path.dirname(self.__base_dir)

        # Data folder paths to which repos are cloned and developer data formatted
        # General data folder
        self.__data_dir = os.path.join(self.__project_root, "data")
        # Folder for all cloned repos
        self.__cloned_repo_dir = os.path.join(self.__data_dir, "cloned_repos")
        #Folder for raw developer data
        self.__raw_data_dir = os.path.join(self.__data_dir, "raw")
        #Folder for processed developmer data
        self.__processed_data_dir = os.path.join(self.__data_dir, "processed")

        # Create directories if they don't exist
        os.makedirs(self.__cloned_repo_dir, exist_ok=True)
        os.makedirs(self.__raw_data_dir, exist_ok=True)
        os.makedirs(self.__processed_data_dir, exist_ok=True)

        # Accept multiple repository URLs
        # See if there is only one repo to be cloned
        if isinstance(repo_urls, str):
            self.repo_urls = [repo_urls]
         # See if there are multiple repos to be cloned
        elif isinstance(repo_urls, list):
            self.repo_urls = repo_urls
        else:
            raise ValueError("repo_urls not a list of strings or a string")

    # Clones all repositories in the list
    def clone_repos(self, repo_url):
        # Get name of the repo (to be cloned) for later use
        repo_name = os.path.basename(repo_url).replace(".git", "")
        # Get full path of the repo to be cloned
        repo_path = os.path.join(self.__cloned_repo_dir, repo_name)

        # Delete existing repo if there is one
        if os.path.exists(repo_path):
            shutil.rmtree(repo_path)

        # Clone new repo version
        print(f"Cloning repo from {repo_url} to {repo_path}")
        return Repo.clone_from(repo_url, repo_path)

    # Deletes the repository dir. The execution may fail because of Antivirus protection.
    def clean_repo(self, repo_path):
        try:
            shutil.rmtree(repo_path)
            print(f"Repository {repo_path} removed")
        except Exception:
            print(f"Failed to remove {repo_path} repository")

    # Filtering data and writing clean data
    def write_csv_data(self):
        for repo_url in self.repo_urls:
            repo_name = os.path.basename(repo_url).replace(".git", "")
            dup_datafile = os.path.join(self.__raw_data_dir, f"{repo_name}_dup.csv")
            clean_datafile = os.path.join(self.__processed_data_dir, f"{repo_name}_clean.csv")

            # Clone repo if not exists
            repo = self.clone_repos(repo_url)

            print(f"Get repo {repo_name} commit data")

            # Collect commit data
            with open(dup_datafile, 'w', newline='\n', encoding='utf-8') as csv_writer_obj:
                csv_writer = csv.writer(csv_writer_obj)
                for d in repo.iter_commits():
                    author_name = str(d.author.name)
                    author_email = str(d.author.email)
                    csv_row_data = [author_name, author_email]

                    if super()._validate_ascii(author_name) and super()._validate_email(author_email) == 0:
                        csv_writer.writerows([csv_row_data])

            # Use pandas to remove duplicates
            panda_datafile = pd.read_csv(dup_datafile)
            panda_datafile = panda_datafile.drop_duplicates()
            panda_datafile.to_csv(clean_datafile, index=False)

            print(f"Repo data processed to {clean_datafile}")

repos_to_clone = ["https://github.com/gitpython-developers/GitPython.git"]

obj = DataExtract(repos_to_clone)
obj.write_csv_data()
