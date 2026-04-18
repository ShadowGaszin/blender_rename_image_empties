# Rename Image Empties

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

**A Blender add-on that quickly renames selected Image Empties to match their actual image files names.**


## A bitta background

I (like many other 3D artists) often use image references directly in the 3D Viewport, but sometimes when there's too many images the whole project gets bloated with `Empty.XXX` objects. It's always mildly frustrated me that there's no function to match the empties' names with the corresponding image files so… I went ahead and decided to make my own add-on/extension for that. I liked the final product so much I decided to share it with you, fellow artists. Feel free to share your thoughts and opinions and give me feedback (not "u MF whadda shit you did", but actual reviews and what to fix/improve)

## Features

- Rename multiple (all if needed) Image Empties at once
- Option to keep or remove file extensions (`.png`, `.jpg`, etc.)
- Fully undo-able (renamings are kept in the project's history like any other thing you do)

## Installation

1. Download the latest `.zip` from [Releases](https://github.com/ShadowGaszin/blender_rename_image_empties/releases)
2. Open Blender → **Edit** → **Preferences** → **Extensions** <sub>(4.1+)</sub>/**Add-ons** <sub>(2.80-4.1)</sub>
3. Click **Install** and select the `.zip` file
4. Check the add-on checkbox

## Usage

### Via Sidebar (N-panel)
1. Select one or more Image Empties in your scene
2. Open the sidebar with `N`
3. Go to the **Image Empties** tab
4. Toggle "Keep Extension" if desired
5. Click **Rename Image Empties**

### Via Object Menu
1. Select your Image Empties
2. Go to **Object** → click **Rename Image Empties**
3. Adjust the "Keep Extension" option in the F9 menu

## Feedback

Found a bug? Have an idea? **I want to hear it.**

- ✅ Constructive criticism, bug reports, feature requests
- ❌ "u MF whadda shit you did" — keep that energy elsewhere

Open an issue on GitHub or reach out directly via [e-mail](mailto:justshadowhedgehog@gmail.com)/[Telegram](https://t.me/half_phantom) (use also for contribution questions). Highly recommend Telegram, as I'm constantly online on it; check e-mails once a week.

## License

This add-on is released under the **GNU General Public License v3.0 or later**. See the [LICENSE](LICENSE) file for details.

## Credits

This add-on was created by me (Gustaf Normann) and released under the GPL-3.0-or-later license.

**You are free to:**
- Modify and redistribute this add-on
- Use it in commercial projects
- Include it in your own tools

**We politely ask (but do not require) that you:**
- Keep the original author's name in the credits
- Link back to the original repository if you share modifications (courtesy and all)

Because open source works best when we acknowledge each other's work.



***
**Good blendering y'all!**
All the best,
*Gustaf Normann, 2026*
