#!/usr/bin/env python
# github.com/wpxq
__version__ = "2.2.0"
from pathlib import Path
import datetime, os, re
import shutil, sys
import stat, requests as r

log_path = Path.home() / ".local/share/updateit/latest.log"
log_path.parent.mkdir(parents=True, exist_ok=True)

def read_last():
    if log_path.exists():
        return log_path.read_text().strip()
    return None

def write_log():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_path.write_text(now + "\n")
    return now

def has_cmd(cmd):
    return shutil.which(cmd) is not None

pkg_managers = [
    # System Package Managers [Main]
    ("Pacman", "sudo pacman -Syu --noconfirm"),
    ("Yay", "yay -Syu --noconfirm"),
    ("Paru", "paru -Syu --noconfirm"),
    ("Xbps", "sudo xbps-install -u xbps && sudo xbps-install -Su -y"),
    ("DNF", "sudo dnf upgrade -y"),
    ("PKG", "sudo pkg update && sudo pkg upgrade -y"),
    ("APT", "sudo apt update && sudo apt upgrade -y"),
    ("Portage", "sudo emerge --sync && sudo emerge -uDN @world"),
    ("Zypper", "sudo zypper refresh && sudo zypper update -y"),
    ("Nix", "nix-channel --update && nix-env -u"),
    ("Apk", "sudo apk update && sudo apk upgrade"),
    
    # External Package Managers [Secondary]
    ("Brew", "brew update && brew upgrade"),
    ("Flatpak", "flatpak update -y"),
    ("Snap", "sudo snap refresh"),
    ("Pip", "python3 -m pip install --upgrade pip && pip list --outdated --format=freeze | cut -d = -f 1 | xargs -n1 pip install -U"),
    ("Npm", "npm update -g"),
    ("Pnpm", "pnpm add -g pnpm && pnpm update -g"),
    ("Cargo", "cargo install-update -a"),
    ("Conda", "conda update --all -y"),
    ("Yarn", "yarn global upgrade"),
    ("Bun", "bun upgrade"),
    ("Rustup", "rustup update"),
    ("Deno", "deno upgrade"),
    ("Composer", "composer self-update"),
    ("Gems", "gem update --system"),
]

def clear():
    os.system("clear")

def show_log():
    last = read_last()
    if last:
        print(f"Last update: {last}")
    else:
        print("No update logged")

def get_latest_ver():
    try:
        url = "https://raw.githubusercontent.com/wpxq/updateit/refs/heads/main/updateit.py"
        resp = r.get(url, timeout=5)
        if resp.status_code == 200:
            match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', resp.text)
            if match:
                return match.group(1)
    except Exception as e:
        pass
    return __version__

def refresh():
    url = "https://raw.githubusercontent.com/wpxq/updateit/refs/heads/main/updateit.py"
    resp = r.get(url)
    if resp.status_code == 200:
        with open("updateit.py", "wb") as f:
            f.write(resp.content)
        print("Succesfully fetch update")
    else:
        print("Failed to fetch update")
        return
    updateit_f = "updateit.py"
    updateit_alias = "updateit"
    target = Path.home() / ".local" / "bin"
    target.mkdir(parents=True, exist_ok=True)
    st = os.stat(updateit_f)
    os.chmod(updateit_f, st.st_mode | stat.S_IEXEC)
    shutil.copy(updateit_f, target / updateit_alias)
    print(f"{updateit_f} refreshed")

def updateit():
    start = write_log()
    print(f"[{start}] Starting update...")
    latest_ver = get_latest_ver()
    if list(map(int, latest_ver.split('.'))) > list(map(int, __version__.split('.'))):
        print(f"New version of updateit is available! [{latest_ver}]")
        ans = input("Do you want to update updateit? (y/n): ").strip().lower()
        if ans == "y":
            print("Updating updateit...")
            refresh()
            print("updateit updated to latest version")
    ans_pkg = input("Do you want to proceed with updating packages? (y/n): ").strip().lower()
    if ans_pkg != "y":
        print(f"[{start}] Update cancelled by user")
        return
    
    print(f"[{start}] Proceeding with package managers...")

    for name, cmd in pkg_managers:
        if has_cmd(cmd.split()[0]):
            print(f"[{start}] Updating {name}...")
            os.system(cmd)
            clear()
        else:
            print(f"[{start}] Skipping {name}: package manager is not installed")

def show_ver():
    print(f"Version: [{__version__}]")

if len(sys.argv) !=2:
    commands = """
updateit [--update] Updates all packages from All Package Managers
updateit [--latest] Shows the latest update
updateit [--refresh] Fetch new version from this github repo
updateit [--version] Shows current version of updateit
"""
    print(commands)
    sys.exit(1)
arg = sys.argv[1]

if arg == "--help":
    commands = """
updateit [--update] Updates all packages from All Package Managers
updateit [--latest] Shows the latest update
updateit [--refresh] Fetch new version from this github repo
updateit [--version] Shows current version of updateit
"""
    print(commands)
    sys.exit(1)

elif arg == "--update":
    updateit()
elif arg == "--latest":
    show_log()
elif arg == "--refresh":
    refresh()
elif arg == "--version":
    show_ver()
else:
    print("Unknown arg, try --help")
    sys.exit(1)
