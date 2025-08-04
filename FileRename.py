import os
import re
from datetime import datetime

start_dir = r'H:\VIDEO PREDSTAVITVE'  # <- Sem nastaviš testno mapo
log_file = 'seznam_rename.txt'
dry_run = False  # Nastavi na False za dejanski zagon
test_single_folder_only = False  # Obdelaj samo eno mapo, brez podmap

def extract_date_from_name(text):
    patterns = [
        r'(\d{4})[-.](\d{2})[-.](\d{2})',    # YYYY-MM-DD
        r'(\d{1,2})[.](\d{1,2})[.](\d{4})',  # DD.MM.YYYY
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            try:
                if len(match.group(1)) == 4:
                    yyyy, mm, dd = match.groups()
                else:
                    dd, mm, yyyy = match.groups()
                return f"{int(dd):02d}-{int(mm):02d}-{yyyy}"
            except:
                return None
    return None

def extract_date_from_metadata(path):
    try:
        ts = os.path.getmtime(path)
        dt = datetime.fromtimestamp(ts)
        return dt.strftime("%d-%m-%Y")
    except:
        return None

def generate_new_name(old_path, date_str):
    zzz = "ZZZ"
    lang = "LANG"
    
    base = os.path.basename(old_path)
    name, ext = os.path.splitext(base)
    
    name_part = re.sub(r'\d{4}[-.]\d{2}[-.]\d{2}', '', name)
    name_part = re.sub(r'\d{1,2}[.]\d{1,2}[.]\d{4}', '', name_part)
    name_part = re.sub(r'\s+', '_', name_part.strip())

    if os.path.isfile(old_path):
        return f"{date_str}_{zzz}_{lang}_{name_part}{ext}"
    else:
        return f"{date_str}_{zzz}_{lang}_{name_part}"

def resolve_conflict(path):
    base, ext = os.path.splitext(path)
    counter = 1
    new_path = path
    while os.path.exists(new_path):
        new_path = f"{base}_{counter}{ext}"
        counter += 1
    return new_path

# Glavna zanka
with open(log_file, 'w', encoding='utf-8') as log:
    if test_single_folder_only:
        try:
            items = os.listdir(start_dir)
        except Exception as e:
            print(f"[NAPAKA] Ne morem prebrati mape: {start_dir} -> {str(e)}")
            exit()

        paths = [os.path.join(start_dir, item) for item in items]
    else:
        paths = []
        for root, dirs, files in os.walk(start_dir, topdown=False):
            paths.extend([os.path.join(root, name) for name in files + dirs])

    for old_path in paths:
        date_str = extract_date_from_name(os.path.basename(old_path)) or extract_date_from_metadata(old_path)
        if not date_str:
            msg = f"{old_path} -> [NAPAKA: Ni datuma]"
            print(msg)
            log.write(msg + "\n")
            continue

        new_name = generate_new_name(old_path, date_str)
        new_path = os.path.join(os.path.dirname(old_path), new_name)

        if old_path == new_path:
            continue

        if os.path.exists(new_path):
            new_path = resolve_conflict(new_path)

        try:
            # Preveri dostop
            if os.path.isfile(old_path):
                with open(old_path, 'rb'):
                    pass
            elif os.path.isdir(old_path):
                os.listdir(old_path)

            if dry_run:
                msg = f"[SIMULACIJA] {old_path} -> {new_path}"
                print(msg)
                log.write(msg + "\n")
            else:
                os.rename(old_path, new_path)
                msg = f"{old_path} -> {new_path}"
                print(msg)
                log.write(msg + "\n")

        except Exception as e:
            msg = f"[NAPAKA PRI PREIMENOVANJU] {old_path} -> {str(e)}"
            print(msg)
            log.write(f"{old_path} -> [NAPAKA PRI PREIMENOVANJU: {str(e)}]\n")

print(f"[INFO] Končano. {'Simulacija' if dry_run else 'Preimenovanje'} izvedeno. Log v '{log_file}'.")
