import configparser
import os

path_file = os.path.abspath(os.path.dirname(__file__))
config_file = configparser.ConfigParser()
config_file_path = os.path.join(path_file, 'config.ini')
config_file.read(config_file_path)

short_db_folder = config_file.get('DB', 'DB_FOLDER')
short_db_path = config_file.get('DB', 'DB_FILE')
DB_PATH = os.path.join(path_file, short_db_folder, short_db_path)
