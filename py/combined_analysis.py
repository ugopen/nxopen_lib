# -*- coding: utf-8 -*-
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

def get_nx_series(folder_name):
    """
    Determines the NX Series for versions > NX12.
    Returns the series string (e.g., "NX2007 Series") or None.
    """
    match = re.match(r'^NX(\d+)', folder_name.upper())
    if not match:
        return None
    
    try:
        ver = int(match.group(1))
    except ValueError:
        return None
    
    # Only applies to versions > 12 (Continuous Release started at 1847)
    if ver <= 12:
        return None
        
    # Series start versions sorted ascending
    series_starts = [
        1847, 1872, 1899, 
        1926, 1953, 1980, 
        2007, 
        2206, 2212, 
        2306, 2312, 
        2406, 2412
    ]
    
    current_series = None
    for start in series_starts:
        if ver >= start:
            current_series = start
        else:
            break
            
    if current_series:
        return f"NX{current_series} Series"
    return None

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
            match = re.search(r'Wizard\s*=\s*VsWizard\.VsWizardEngine\.(\d+\.\d+)', content)
            if match:
                return match.group(1)
    except Exception:
        pass
    return None

def get_vs_info_for_nx(nx_path):
    ugopen_path = os.path.join(nx_path, 'UGOPEN')
    
    # Check if UGOPEN exists directly
    if os.path.exists(ugopen_path):
        search_paths = [
            os.path.join(ugopen_path, 'vs_files', 'VC', 'vcprojects'),
            os.path.join(ugopen_path, 'vc7_files', 'vcprojects'),
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
                            
    # Fallback: Check subdirectories (e.g. NX6/NX6_32)
    for item in os.listdir(nx_path):
        sub_path = os.path.join(nx_path, item)
        if os.path.isdir(sub_path) and item.upper().startswith('NX'):
            # Recursive check one level deep
            ugopen_sub = os.path.join(sub_path, 'UGOPEN')
            if os.path.exists(ugopen_sub):
                search_paths = [
                    os.path.join(ugopen_sub, 'vs_files', 'VC', 'vcprojects'),
                    os.path.join(ugopen_sub, 'vc7_files', 'vcprojects'),
                    os.path.join(ugopen_sub, 'vs_files', 'vcprojects')
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

def find_lib_files(directory):
    """
    Recursively finds all .lib files in the given directory.
    Returns a set of unique lowercase filenames.
    """
    unique_libs = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.lib'):
                unique_libs.add(file.lower())
    return unique_libs

def main():
    root_dir = os.getcwd()
    nx_folders = []
    
    # Identify NX folders
    for item in os.listdir(root_dir):
        if os.path.isdir(item) and item.upper().startswith('NX'):
            nx_folders.append(item)
    
    nx_folders.sort(key=get_nx_version_key)
    
    vs_map = get_vs_version_map()
    
    # Data collection
    data = []
    prev_libs = set()
    
    for i, folder in enumerate(nx_folders):
        full_path = os.path.join(root_dir, folder)
        
        # 1. Get VS Version
        internal_ver = get_vs_info_for_nx(full_path)
        vs_name = vs_map.get(internal_ver, '-') if internal_ver else '-'
        display_internal_ver = internal_ver if internal_ver else "-"
        
        if internal_ver is None:
             # Manual override for known newer versions if desired, or leave as '-'
             if 'NX24' in folder:
                 vs_name = "Visual Studio 2022 (Est.)"
        
        # 2. Get Libs
        curr_libs = find_lib_files(full_path)
        lib_count = len(curr_libs)
        
        # 3. Calculate Changes
        if i == 0:
            added_count = len(curr_libs)
            removed_count = 0
            
            added_str = f"{added_count} (Base)"
            removed_str = "-"
            
            added_names = ",".join(sorted(curr_libs)) if curr_libs else "-"
            removed_names = "-"
        else:
            added_set = curr_libs - prev_libs
            removed_set = prev_libs - curr_libs
            
            added_count = len(added_set)
            removed_count = len(removed_set)
            
            added_str = f"+{added_count}" if added_count > 0 else "0"
            removed_str = f"-{removed_count}" if removed_count > 0 else "0"
            
            added_names = ",".join(sorted(added_set)) if added_set else "-"
            removed_names = ",".join(sorted(removed_set)) if removed_set else "-"
        
        # 4. Determine Display Name (Series)
        series = get_nx_series(folder)
        
        # Logic:
        # If series is detected (meaning > NX12), format the folder name to be comma-separated
        # instead of underscore-separated.
        # The user requested: "According to 'Series' column, merge 'NX Version' column content into one line, separated by ','"
        
        if series:
            # Replace underscores with comma+space
            formatted_folder = folder.replace('_', ', ')
            display_folder = formatted_folder
        else:
            display_folder = folder

        data.append({
            'folder': display_folder,
            'internal_ver': display_internal_ver,
            'vs_ver': vs_name,
            'lib_count': lib_count,
            'added': added_str,
            'removed': removed_str,
            'added_names': added_names,
            'removed_names': removed_names
        })
        
        prev_libs = curr_libs

    # Generate Markdown Content
    md_lines = []
    md_lines.append("# NX Version Lib Analysis")
    md_lines.append("")
    md_lines.append("| NX Version | VS Internal Ver | VS Version | Added Files | Removed Files |")
    md_lines.append("| :--- | :--- | :--- | :--- | :--- |")
    
    for row in data:
        # Escape pipes in filenames if any (unlikely but good practice)
        added_files = row['added_names'].replace("|", "\\|")
        removed_files = row['removed_names'].replace("|", "\\|")
        
        line = f"| {row['folder']} | {row['internal_ver']} | {row['vs_ver']} | {added_files} | {removed_files} |"
        md_lines.append(line)
        
    # Write to file
    output_file = "NX_Lib_Analysis.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
        
    print(f"Analysis saved to {output_file}")

if __name__ == "__main__":
    main()
