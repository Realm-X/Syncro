import os
def get_startup_folder_path():
    startup_path = os.path.join(os.environ['APPDATA'], r"Microsoft\Windows\Start Menu\Programs\Startup")
    
    return startup_path
