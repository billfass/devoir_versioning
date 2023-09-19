# Bile Fassinou, Master 2 DIT promotion avril 23

import os
from pathlib import Path
import shutil

class Structure:
    def __init__(self, project_root):
        self.project_root = project_root

    def method_2(self):
        Path(self.project_root+"/data/cleaned").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/data/raw").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/docs").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/models").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/notebooks").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/reports").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/src").mkdir(parents=True, exist_ok=True)

        self.edit_files()
    
    def edit_files(self):       
        with open(os.path.join(self.project_root, 'LICENSE'), 'w') as f:
            f.write("Mettez ici votre licence ou les termes de distribution du projet.")

        with open(os.path.join(self.project_root, 'Makefile'), 'w') as f:
            f.write("# Mettez ici les commandes make utiles pour votre projet.")

        with open(os.path.join(self.project_root, 'notebooks', 'main.ipynb'), 'w') as f:
            f.write("import numpy as np")

        with open(os.path.join(self.project_root, 'README.md'), 'w') as f:
            f.write(readme)

        with open(os.path.join(self.project_root, 'requirements.txt'), 'w') as f:
            f.write("# Liste des dépendances de votre projet\n\nPackage1==1.0\nPackage2==2.3.1\n")

        with open(os.path.join(self.project_root, 'src', 'utils.py'), 'w') as f:
            f.write("# my utils")

        with open(os.path.join(self.project_root, 'src', 'process.py'), 'w') as f:
            f.write("# my process")

        with open(os.path.join(self.project_root, 'src', 'train.py'), 'w') as f:
            f.write("# my train")


        with open(os.path.join(self.project_root, 'docs', 'docs.txt'), 'w') as f:
            f.write("hello world")

        with open(os.path.join(self.project_root, 'models', 'mymodel.ipynb'), 'w') as f:
            f.write("import numpy as np")

        with open(os.path.join(self.project_root, 'reports', 'report.log'), 'w') as f:
            f.write("hello world")

        with open(os.path.join(self.project_root, 'Makefile'), 'w') as f:
            f.write("# Mettez ici les commandes make utiles pour votre projet.")

        with open(os.path.join(self.project_root, 'requirements.txt'), 'w') as f:
            f.write("# Liste des dépendances de votre projet\n\nPackage1==1.0\nPackage2==2.3.1\n")



        

        
