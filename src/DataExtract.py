from git import Repo
import shutil
import csv
import pandas as pd

from src.DataClean import DataClean

class DataExtract(DataClean):
    def __init__(self, repo_url, repo_name):
        super().__init__()
        self.__repo_base_path = "../res/"
        self.__dup_datafile = "../data/raw/dup_data.csv"
        self.__datafile = "../data/processed/data.csv"

        self.__repo_url = repo_url
        self.__repo_name = repo_name

        # Clone the repository if it does not exist
        try:
            self.__repo_name = self.__repo_base_path + repo_name
            self.project_repo = Repo(self.__repo_base_path + repo_name)
        except:
            print("Cloning repository to res directory")
            project_repo = Repo.clone_from(self.__repo_url, self.__repo_name)

    # Clones the repository
    def clone_repo(self):
        self.project_repo = Repo.clone_from(self.__repo_url, self.__repo_name)

    # Deletes the repository dir. The execution may fail because of Antivirus protection.
    def clean_repo(self):
        shutil.rmtree(self.__repo_name)

    # Filtering data and writing clean data
    def write_csv_data(self):
        csv_writer_obj = open(self.__dup_datafile, 'w', newline='\n', encoding='utf-8')
        csv_writer = csv.writer(csv_writer_obj)
        for d in self.project_repo.iter_commits():
            author_name = str(d.author.name)
            author_email = str(d.author.email)
            csv_row_data = [str(d.author.name), str(d.author.email)]
            if super()._validate_ascii(author_name) == True and super()._validate_email(author_email) == 0:
                    csv_writer.writerows([csv_row_data])

        # Removes Duplicates with the pandas
        # the pandas reads csv
        panda_datafile = pd.read_csv(self.__dup_datafile)

        # the pandas drops duplicates
        panda_datafile = panda_datafile.drop_duplicates()

        # the pandas writes clean data to another file
        panda_datafile.to_csv(self.__datafile, index=False)

        # Removes unnecessary the duplicate file, uncomment if needed
        #shutil.rmtree(self.__dup_datafile)

# For example: 
obj = DataExtract("https://github.com/gitpython-developers/GitPython.git", "gitproject")
obj.write_csv_data()
