import os
# from datasets import load_dataset
PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).split('/')[0]

db_root = os.environ.get("DATA_PATH", "/home/khlee01/dataset")

#db_names = {'PASCALContext': 'PASCALContext', 'NYUD_MT': "sayakpaul/nyu_depth_v2"}
db_names = {'NYUD_MT': 'NYUD_MT'}

db_paths = {}
for database, db_pa in db_names.items():
    db_paths[database] = os.path.join(db_root, db_pa)

# db_objects = {}
# for key, hf_name in db_names.items():
#     db_objects[key] = load_dataset(hf_name, split='train')
