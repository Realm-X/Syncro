import os
import shutil

def find_vbs_script(filename="startup.vbs"):


    drives = ['C:\\', 'D:\\']  

    for drive in drives:
        for root, dirs, files in os.walk(drive):
            if filename in files:
                vbs_path = os.path.join(root, filename)
                movevbstostart(vbs_path)
                return  
            
    

def movevbstostart(vbs_path):
    startup_folder = os.path.join(
        os.getenv('APPDATA'), 
        r"Microsoft\Windows\Start Menu\Programs\Startup"
    )
    
    shutil.move(vbs_path, startup_folder)
    
