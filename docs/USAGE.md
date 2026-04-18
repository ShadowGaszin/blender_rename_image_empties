# Usage Guide

## What are "Image Empties"?

Images, imported as empties, I call "Image Empties". They're very often used for references in modeling (when you use front and side views of a character/object you want to create directly in the Viewport).

## Step-by-Step

### Renaming a Single Empty
1. Select the Image Empty
2. Open the sidebar (`N`) OR click on `Object` menu
3. Click `Rename Image Empties`

### Renaming Multiple Empties
1. Shift-click to select multiple Image Empties (or, if you want all Empties, press `A`)
2. Use either the sidebar button or Object menu
3. All selected empties will be renamed at once (non-Image Empties and other types of .blend objects will be ignored)

### Keep Extension Option
- **Off (default):** `my_image.png` → `my_image`
- **On:** `my_image.png` → `my_image.png`

## Troubleshooting

| Problem            | Solution                                                                                                                                                                    |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nothing happens    | Make sure you have Image Empties selected, not regular empties or other object types                                                                                        |
| Wrong name appears | The add-on uses the **image data-block name**, not the filename on disk (most of the data-block names are just the same as file's name even after renaming the file anyway) |