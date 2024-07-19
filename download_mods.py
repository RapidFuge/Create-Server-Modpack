import os
import toml
import urllib.request
import shutil
import requests

CURSEFORGE_API_KEY = os.getenv('CURSEFORGE_API_KEY')

def download_mod(url, download_path):
    urllib.request.urlretrieve(url, download_path)

def get_curseforge_download_url(project_id, file_id):
    headers = {
        'x-api-key': CURSEFORGE_API_KEY
    }
    url = f'https://api.curseforge.com/v1/mods/{project_id}/files/{file_id}/download-url'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['data']

mods_folder = 'mods'
client_folder = os.path.join(mods_folder, 'client')
server_folder = os.path.join(mods_folder, 'server')

# Create directories if they do not exist
os.makedirs(client_folder, exist_ok=True)
os.makedirs(server_folder, exist_ok=True)

# Iterate through each .toml file in the mods folder
for filename in os.listdir(mods_folder):
    if filename.endswith('.toml'):
        filepath = os.path.join(mods_folder, filename)
        with open(filepath, 'r') as f:
            mod_info = toml.load(f)
        
        mod_name = mod_info['name']
        mod_filename = mod_info['filename']
        mod_side = mod_info['side']
        download_info = mod_info['download']
        
        download_path = os.path.join(mods_folder, mod_filename)

        if download_info.get('mode') == 'metadata:curseforge':
            project_id = mod_info['update']['curseforge']['project-id']
            file_id = mod_info['update']['curseforge']['file-id']
            download_url = get_curseforge_download_url(project_id, file_id)
        else:
            download_url = download_info['url']
        
        # Download the mod file
        download_mod(download_url, download_path)
        
        # Categorize the mod based on 'side'
        if mod_side == 'client' or mod_side == 'both':
            shutil.copy(download_path, os.path.join(client_folder, mod_filename))
        
        if mod_side == 'server' or mod_side == 'both':
            shutil.copy(download_path, os.path.join(server_folder, mod_filename))
