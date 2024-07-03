# Autodesign

The internal team's app that promises to facilitate the launch of marketing strategies, helping to create marketing material for social media.

# Documentation

* [App Instructions]()
  * [Importing an image]()
  * [Adding layers]()
  * [Editing layers]()
  * [Shortcuts]()
* [Dependencies]()

---

## App Instructions

### Importing an image

The first window that shows up allows the user to import an image, which will be used as the base image.


### Adding layers

You can add a new layer by clicking either the "Add text" or the "Add image" button. 

The first one opens up a new window where you can specify the text you want to add and also choose a font ([you can also add custom fonts]()). When clicking "Apply" The preview image changes and a new text layer is added:

<p align="center">
    <img src="Documentation/Save.gif" width="600" height="350"/>
</p>

If you choose to add an image, a file dialog will open and you can choose an image to load onto a layer:

<p align="center">
    <img src="Documentation/Save.gif" width="600" height="350"/>
</p>

### Editing layers

The list widget enables you to change the order of the layers by dragging them or to edit a layer by double clicking it. If you choose to edit a layer, a new window will open where you can change your initial options.
You can also delete a layer:

<p align="center">
    <img src="Documentation/Save.gif" width="600" height="350"/>
</p>

### Shortcuts

There is currently one shortcut in the app. You can press 'F' to toggle full screen

<p align="center">
    <img src="Documentation/Zoom.gif" width="600" height="350"/>
</p>


### Saving an image

You can choose a location to save your image with the "Save Image" option

<p align="center">
    <img src="Documentation/Save.gif" width="600" height="350"/>
</p>


---


## Dependencies

In order to run the source code, you need to do:

```pip install PyQt6```

```pip install Pillow```
