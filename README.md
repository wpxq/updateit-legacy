# Package Manager Updater

![updateit](https://github.com/wpxq/updateit-legacy/blob/main/updateit.png)

---

CLI tool to update all package managers and check the latest update date 

---

### System Package Managers
| Package Managers |
| :--- |
| Pacman, Yay, Paru, Xbps, DNF, PKG, APT, Portage, Zypper, Nix, Apk, Winget, Scoop, Choco |

### External Package Managers
| Package Managers |
| :--- |
| Brew, Flatpak, Snap, PIP, NPM, PNPM, Cargo, Conda, Yarn, Bun, Rustup, Deno, Composer, Gems |

## Functions
### `--update`  
Updates all packages from all package managers

### `--latest`
Shows the latest update

### `--refresh`
Fetch new version from this github repo

### `--version`
Shows current version of updateit

## Requirements:
* Python 3.11 or higher
* `requests` library

## Setup
1. Clone this repo:
```bash
git clone https://github.com/wpxq/updateit
cd updateit
```
2. Run the provided installation bash script:
   ```bash
   chmod +x updateit_setup.sh
   ./updateit_setup.sh
   ```

## Troubleshooting (PATH issues)
if the command is not found, add this to your `.bashrc` (or `.zshrc`):
```bash
export PATH="$HOME/.local/bin:$PATH"
```
### Then save and run: ```source .bashrc``` (or `source .zshrc`)
