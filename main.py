import os
import pathlib
from shutil import copytree


def find_folder(start_path, folder_name):
    excluded_dirs = ['Windows', 'ProgramData', 'AMD', 'boot', 'DRIVERS', 'PerfLogs', 'WinPE_amd64', 'XboxGames']

    for root, dirs, _ in os.walk(start_path):
        dirs[:] = [d for d in dirs if d not in excluded_dirs]

        for directory in dirs:
            if folder_name in directory:
                return pathlib.Path(root) / directory
    return None


root_path = pathlib.Path('C:/')
target_folder_name = 'client_1165'

client_folder = find_folder(root_path, target_folder_name)

if client_folder:
    print(f"Folder found at: {client_folder}")

    script_directory = pathlib.Path(__file__).parent
    addon_list = ['assets\\pfQuest', 'assets\\pfQuest-turtle', 'assets\\TWThreat', 'assets\\ShaguDPS',
                  'assets\\AtlasLoot', 'assets\\Cartographer', 'assets\\SortBags', 'assets\\Cleanup']

    for addon in addon_list:
        folder_to_copy = script_directory / pathlib.Path(addon)

        if folder_to_copy.exists() and folder_to_copy.is_dir():
            destination = client_folder / 'Interface' / 'AddOns' / pathlib.Path(addon).name
            destination.mkdir(parents=True, exist_ok=True)
            copytree(str(folder_to_copy), str(destination), dirs_exist_ok=True)
            print(f"Copied '{folder_to_copy}' to '{destination}'")
        else:
            print(f"Directory '{folder_to_copy}' not found.")
else:
    print(f"Folder containing '{target_folder_name}' not found.")
