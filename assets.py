import os

def assets(assets_folder: str, asset_filename: str):
    OUTPUT_PATH = os.path.dirname(__file__)
    ASSETS_PATH = os.path.join(OUTPUT_PATH, './assets/{}'.format(assets_folder))
    return os.path.join(ASSETS_PATH, './{}'.format(asset_filename))