import os
import re

def get_nx_version_key(folder_name):
    """
    Extracts a sortable key from the NX folder name.
    """
    version_str = folder_name[2:]
    if '_' in version_str:
        version_str = version_str.split('_')[0]
    try:
        parts = [int(p) for p in version_str.split('.')]
        return tuple(parts)
    except ValueError:
        match = re.match(r'^(\d+)', version_str)
        if match:
            return (int(match.group(1)),)
        return (999999, folder_name)

def get_vs_version_map():
    return {
        '7.0': 'Visual Studio .NET 2002',
        '7.1': 'Visual Studio .NET 2003',
        '8.0': 'Visual Studio 2005',
        '9.0': 'Visual Studio 2008',
        '10.0': 'Visual Studio 2010',
        '11.0': 'Visual Studio 2012',
        '12.0': 'Visual Studio 2013',
        '14.0': 'Visual Studio 2015',
        '15.0': 'Visual Studio 2017',
        '16.0': 'Visual Studio 2019',
        '17.0': 'Visual Studio 2022'
    }

def find_vs_version_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # Look for Wizard=VsWizard.VsWizardEngine.X.X
            match = re.search(r'Wizard\s*=\s*VsWizard\.VsWizardEngine\.(\d+\.\d+)', content)
            if match:
                return match.group(1)
    except Exception:
        pass
    return None

def get_vs_info_for_nx(nx_path):
    # Potential paths to check
    # 1. UGOPEN/vs_files/VC/vcprojects/*.vsz (Newer versions)
    # 2. UGOPEN/vc7_files/vcprojects/*.vsz (Older versions like NX4)
    
    ugopen_path = os.path.join(nx_path, 'UGOPEN')
    if not os.path.exists(ugopen_path):
        return None

    search_paths = [
        os.path.join(ugopen_path, 'vs_files', 'VC', 'vcprojects'),
        os.path.join(ugopen_path, 'vc7_files', 'vcprojects'),
        # Add more if needed, e.g. sometimes just vs_files/vcprojects?
        os.path.join(ugopen_path, 'vs_files', 'vcprojects') 
    ]

    for search_path in search_paths:
        if os.path.exists(search_path):
            for file in os.listdir(search_path):
                if file.lower().endswith('.vsz'):
                    full_path = os.path.join(search_path, file)
                    version = find_vs_version_in_file(full_path)
                    if version:
                        return version
    return None

def main():
    root_dir = os.getcwd()
    nx_folders = []
    
    # Identify NX folders
    for item in os.listdir(root_dir):
        if os.path.isdir(item) and item.upper().startswith('NX'):
            nx_folders.append(item)
    
    nx_folders.sort(key=get_nx_version_key)
    
    vs_map = get_vs_version_map()
    
    print(f"{'NX Version':<40} | {'VS Internal Ver':<15} | {'VS Version Mapping'}")
    print("-" * 85)
    
    for folder in nx_folders:
        full_path = os.path.join(root_dir, folder)
        internal_ver = get_vs_info_for_nx(full_path)
        
        if internal_ver:
            mapped_ver = vs_map.get(internal_ver, 'Unknown')
            print(f"{folder:<40} | {internal_ver:<15} | {mapped_ver}")
        else:
            # Try to handle sub-folders like NX6/NX6_32 if main folder fails
            # But usually UGOPEN is at top level or we need to dig deeper?
            # Let's check if there are sub-NX folders inside
            found_in_sub = False
            for sub in os.listdir(full_path):
                sub_path = os.path.join(full_path, sub)
                if os.path.isdir(sub_path) and sub.upper().startswith('NX'):
                    internal_ver = get_vs_info_for_nx(sub_path)
                    if internal_ver:
                        mapped_ver = vs_map.get(internal_ver, 'Unknown')
                        print(f"{folder + '/' + sub:<40} | {internal_ver:<15} | {mapped_ver}")
                        found_in_sub = True
                        break # Assume same for all subs
            
            if not found_in_sub:
                print(f"{folder:<40} | {'Not Found':<15} | {'-'}")

if __name__ == "__main__":
    main()
