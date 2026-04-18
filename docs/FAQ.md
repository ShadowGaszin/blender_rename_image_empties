# FAQ (Frequently Asked Questions)
## Questions Nobody Asked Yet, But Someone Will
### Q: Why would I ever need this?
A: If you ever used Image Empties for reference images, you've probably seen a list of objects named `Empty.001`, `Empty.002`, `Empty.003`, especially if you used a lot of images, and cried a little inside from trying to understand which `Empty` is which image. This add-on fixes that.
### Q: Does it work on regular empties?
A: No. Only empties with `Display Type = Image`. Regular empties don't have image data to pull names from.
### Q: What if my image is called `final_final_actually_final_v3.png`?
A: Then your empty will become `final_final_actually_final_v3` (or keep the `.png` if you check the box). The add-on doesn't judge your naming conventions, as your image only loads into the `.blend` file and already from there my add-on gets the image's name.
### Q: Will this delete my images?
A: It doesn't directly interact with images, only with the corresponding data-blocks (the way `.blend` files keep info about the images).
### Q: I clicked the button and nothing happened.
A: Did you select any Image Empties? The add-on only renames **selected** objects that are Image Empties. Try selecting one first.
### Q: Can I undo it?
A: Yes! Ctrl+Z or any other combination you use works just like with any other Blender operation.
### Q: I found a bug!
A: Please report it on [GitHub Issues link](https://github.com/ShadowGaszin/blender_rename_image_empties/issues) or contacting me via [e-mail](mailto:justshadowhedgehog@gmail.com)/[Telegram](https://t.me/half_phantom) (latter is most recommended, as I use it daily). Include:
- Blender version
- What you did
- What happened
- What you expected to happen
- (Optional) A screenshot or screen recording of the replication of how you got this
### Q: Who made this?
A: Gustaf Normann. Was mildly frustrated by the lack of such feature and decided, "If not me, then *who*?"
### Q: That's just useless
A: Whatever. You can't please everyone. If you don't find it of use, you can pass by. Someone else would appreciate the work.