# 🎨 PhotoGIMP

**PhotoGIMP** is a free, community-driven patch that transforms GIMP into a layout that feels familiar to Adobe Photoshop users.

---

## ⚙ How to Install

### ⚡ Automated Installation (Linux / macOS)

If you are on Linux or macOS, you can use the automated installer script:

1. Clone or download the repository.
2. Open your terminal and navigate to the project directory.
3. Make sure GIMP is completely closed.
4. Run the installer:
   ```bash
   ./install.sh
   ```
   *Note: You can run `./install.sh --dry-run` to preview the changes without installing anything.*

---

### 🐧 Flatpak (Linux)

#### Backup (optional)

If you want to keep your current GIMP settings, back them up first:

```bash
cp -r ~/.config/GIMP/3.0 ~/GIMP-3.0-backup
```

#### Install

1. Make sure you already have GIMP installed [from Flathub](https://flathub.org/apps/org.gimp.GIMP).
2. **Open GIMP once, then close it** — this creates the config folders that PhotoGIMP needs.
3. Download the latest release:
   👉 **[Download PhotoGIMP for Linux (.zip)](https://github.com/Diolinux/PhotoGIMP/releases/download/3.0/PhotoGIMP-linux.zip)**
4. Extract the `.zip` file **into your home folder** (`~`).
   - This will place files into `~/.config` and `~/.local`, which are hidden folders.
   - To see hidden folders in your file manager, press <kbd>Ctrl</kbd> + <kbd>H</kbd>.
   - When prompted about existing files, choose **"Replace"** or **"Overwrite"**.
5. Open GIMP — you should see the new PhotoGIMP layout! 🎉

<details>
<summary><strong>💡 Using a non-Flatpak GIMP?</strong></summary>

If you installed GIMP from your distro's package manager (apt, dnf, pacman, etc.) instead of Flatpak, the config folder is in the same location (`~/.config/GIMP/3.0`), so the steps above still work. Just make sure you have GIMP version 3.0 or newer.
</details>

---

### 🍎 macOS

#### Backup (optional)

If you want to keep your current GIMP settings, back them up first:

1. Open Finder.
2. Press <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>G</kbd> and go to `~/Library/Application Support/GIMP`.
3. Copy the entire `GIMP` folder to a safe location (e.g., your Desktop).

#### Install

1. Make sure you have [GIMP installed from the official website](https://www.gimp.org/downloads/).
2. **Open GIMP once, then close it** — this creates the config folders that PhotoGIMP needs.
3. Download the latest release:
   👉 **[Download PhotoGIMP for macOS (.zip)](https://github.com/Diolinux/PhotoGIMP/releases/download/3.0/PhotoGIMP.zip)**
4. Extract the contents of `PhotoGIMP.zip` to any folder (e.g., your Desktop).
5. Open the extracted folder and **copy the `3.0` folder**.
6. Open Finder, press <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>G</kbd> to open "Go to Folder".
7. Type `~/Library/Application Support/GIMP` and press <kbd>Enter</kbd>.
8. If you see a `2.10` folder from a previous installation, **delete it** to avoid conflicts.
9. **Paste** the `3.0` folder inside the GIMP folder.
10. When prompted about existing files, select **"Replace"** or **"Merge"**.
11. Open GIMP — you should see the new PhotoGIMP layout! 🎉

---

## 🎹 Keyboard Shortcuts Compatibility

> Shortcuts follow [Adobe Photoshop's official documentation](https://helpx.adobe.com/photoshop/using/default-keyboard-shortcuts.html) (Windows version).
>
> **Legend:** ✅ Matches Photoshop · ⚠️ Different key · ❌ Not mapped by PhotoGIMP

### Tools

| Action | Photoshop | PhotoGIMP | Status |
|---|---|---|---|
| Move | `V` | `V` | ✅ |
| Rectangular Marquee | `M` | `M` | ✅ |
| Elliptical Marquee | `Shift+M` | `Shift+M` | ✅ |
| Lasso | `L` | `L` | ✅ |
| Magic Wand / Quick Selection | `W` | `W` | ✅ |
| Crop | `C` | `C` | ✅ |
| Eyedropper | `I` | `I` | ✅ |
| Healing Brush | `J` | `J` | ✅ |
| Brush | `B` | `B` | ✅ |
| Clone Stamp | `S` | `S` | ✅ |
| Eraser | `E` | `E` | ✅ |
| Gradient | `G` | `G` | ✅ |
| Paint Bucket | `Shift+G` | `Shift+G` | ✅ |
| Dodge / Burn | `O` | `O` | ✅ |
| Smudge | `Shift+R` ¹ | `R` | ⚠️ |
| Blur / Sharpen | `Shift+R` ¹ | `Shift+R` | ⚠️ |
| Text | `T` | `T` | ✅ |
| Pen | `P` | `P` | ✅ |
| Path / Direct Selection | `A` | `A` | ✅ |
| Hand | `H` | — ² | ❌ |
| Zoom | `Z` | `Z` | ✅ |
| Default Colors | `D` | `D` | ✅ |
| Swap Colors | `X` | `X` | ✅ |
| Quick Mask Toggle | `Q` | `Q` | ✅ |
| Full Screen | `F` | `F` | ✅ |

¹ In modern Photoshop, `R` is Rotate View. Smudge and Blur/Sharpen are accessed via `Shift+R` cycling within the group.
² GIMP has no Hand tool. Use `Space+move` to pan (no click needed — works differently from Photoshop's `Space+click+drag`).

### Editing & Fill

| Action | Photoshop | PhotoGIMP | Status |
|---|---|---|---|
| Fill with Foreground | `Alt+Backspace` | `Alt+Backspace` | ✅ |
| Fill with Background | `Ctrl+Backspace` | `Ctrl+Backspace` | ✅ |
| Free Transform | `Ctrl+T` | `Ctrl+T` | ✅ |
| Scale | _(within transform)_ | `Shift+T` | ⚠️ |

### Layers

| Action | Photoshop | PhotoGIMP | Status |
|---|---|---|---|
| Duplicate Layer | `Ctrl+J` | `Ctrl+J` | ✅ |
| Merge Down | `Ctrl+E` | `Ctrl+E` | ✅ |
| New Layer Group | `Ctrl+G` | `Ctrl+G` | ✅ |
| Ungroup / Merge Group | `Ctrl+Shift+G` | `Ctrl+Shift+G` | ⚠️ ³ |
| Layer Opacity 10–90% | `1`–`9` | `1`–`9` | ✅ |
| Layer Opacity 100% | `0` | `0` | ✅ |
| Alpha to Selection | _Ctrl+click thumbnail_ | `Ctrl+Alt+A` | ⚠️ ⁴ |

³ In Photoshop `Ctrl+Shift+G` dissolves the group keeping layers separate. In GIMP it merges the group into a single layer.
⁴ GIMP does not support Ctrl+click on the layer thumbnail. `Ctrl+Alt+A` is the keyboard equivalent.

### Selection

| Action | Photoshop | PhotoGIMP | Status |
|---|---|---|---|
| Deselect | `Ctrl+D` | `Ctrl+D` | ✅ |

### View & Zoom

| Action | Photoshop | PhotoGIMP | Status |
|---|---|---|---|
| Zoom In | `Ctrl+=` | `Ctrl+=` | ✅ |
| Zoom Out | `Ctrl+-` | `Ctrl+-` | ✅ |
| Fit on Screen | `Ctrl+0` | `Ctrl+0` | ✅ |

### Image & Canvas

| Action | Photoshop | PhotoGIMP | Status |
|---|---|---|---|
| Image Size | `Ctrl+Alt+I` | `Ctrl+Alt+I` | ✅ |
| Canvas Size | `Ctrl+Alt+C` | `Ctrl+Alt+C` | ✅ |

### Brush

| Action | Photoshop | PhotoGIMP | Status |
|---|---|---|---|
| Decrease brush size | `[` | `[` | ✅ |
| Increase brush size | `]` | `]` | ✅ |
| Decrease brush hardness | `{` | `{` | ✅ |
| Increase brush hardness | `}` | `}` | ✅ |
