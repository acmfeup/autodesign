# Autodesign

The internal team's app that promises to facilitate the launch of marketing strategies, helping to create marketing material for social media.

# Documentation

* [App Instructions](#App-Instructions)
  * [Importing an image](#Importing-an-image)
  * [Adding layers](#Adding-Layers)
  * [Editing layers](#Editing-Layers)
  * [Adding Custom Fonts](#Adding-Custom-Fonts)
  * [Shortcuts](#Shortcuts)
* [Dependencies](#Dependencies)

---

## App Instructions

### Importing an image

The first window that shows up allows the user to import an image, which will be used as the base image.

<p align="center">
    <img src="https://github.com/acmfeup/autodesign/blob/d91195baeaeab79c0b95b95128644bd174aea51c/Resources/Documentation/Import.gif" />
</p>


### Adding Layers

You can add a new layer by clicking either the "Add text" or the "Add image" button. 

The first one opens up a new window where you can specify the text you want to add and also choose a font ([you can also add custom fonts]()). When clicking "Apply" The preview image changes and a new text layer is added:

<p align="center">
    <img src="https://github.com/acmfeup/autodesign/blob/d91195baeaeab79c0b95b95128644bd174aea51c/Resources/Documentation/AddText.gif"/>
</p>

If you choose to add an image, a file dialog will open and you can choose an image to load onto a layer:

<p align="center">
    <img src="https://github.com/acmfeup/autodesign/blob/d91195baeaeab79c0b95b95128644bd174aea51c/Resources/Documentation/OpenImage.gif"/>
</p>

### Editing Layers

The list widget enables you to change the order of the layers by dragging them or to edit a layer by double clicking it. If you choose to edit a layer, a new window will open where you can change your initial options.

<p align="center">
    <img src="https://github.com/acmfeup/autodesign/blob/d91195baeaeab79c0b95b95128644bd174aea51c/Resources/Documentation/ChangeLayer.gif"/>
</p>

<p align="center">
    <img src="https://github.com/acmfeup/autodesign/blob/d91195baeaeab79c0b95b95128644bd174aea51c/Resources/Documentation/Drag.gif"/>
</p>

You can also delete a layer:

<p align="center">
    <img src="https://github.com/acmfeup/autodesign/blob/d91195baeaeab79c0b95b95128644bd174aea51c/Resources/Documentation/DeleteLayer.gif"/>
</p>


### Adding Custom Fonts

You can add a font in .ttf format to the "Custom fonts" folder. Then you can select your font in the app, just like the other fonts.


### Shortcuts

There is currently one shortcut in the app. You can press 'F' to toggle full screen

<p align="center">
    <img src="https://github.com/acmfeup/autodesign/blob/37ced62f6a68989d33178c543fba91c34b5449b0/Resources/Documentation/Zoom.gif"/>
</p>


### Saving an image

You can choose a location to save your image with the "Save Image" option

<p align="center">
    <img src="https://github.com/acmfeup/autodesign/blob/d91195baeaeab79c0b95b95128644bd174aea51c/Resources/Documentation/Save.gif"/>
</p>


---


## Dependencies

In order to run the source code, you need to do:

```pip install PyQt6```

```pip install Pillow```
