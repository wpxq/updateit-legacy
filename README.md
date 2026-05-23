# Package Manager Updater

![updateit](https://github.com/wpxq/updateit/blob/old_updateit/updateit.png)

---

CLI tool to update all package managers and check the latest update date 

---

## Functions

### `--update`  
Updates all packages from All Package Managers

### System Package Managers
| Package Managers |
| :--- |
| Pacman |
| Yay |
| Paru |
| Xbps |
| DNF |
| PKG |
| APT |
| Portage |
| Zypper |
| Nix |
| Apk |

### External Package Managers
| Package Managers |
| :--- |
| Brew |
| Flatpak |
| Snap |
| PIP |
| NPM |
| PNPM |
| Cargo |
| Conda |
| Yarn |
| Bun |
| Rustup |
| Deno |
| Composer |
| Gems |

### `--latest`
Shows the latest update

### `--refresh`
Fetch new version from this github repo

## if there are any problems with the path:
##### type in .bashrc => export PATH="$HOME/.local/bin:$PATH" => save & type => source .bashrc

### `--version`
Shows current version of updateit

## Requirements:
* Python 3.11 or higher
* `requests` library

## Setup
1. Clone this repo
2. Run the provided installation bash script:
   ```bash
   chmod +x updateit_setup.sh
   ./updateit_setup.sh
   ```
