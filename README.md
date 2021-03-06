# Batch Attachment Add-in for ArcMap
The Batch Attachment add-in allows a user to attach attachment(s) to selected features (even in multiple layers) automatically. The add-in includes a toolbar with a button. It's been tested for ArcGIS 10.3, using a File Geodatabase so far, further testing is required.

## How it works
The Toolbar button accepts the selected features, and prompts you for a list of files.  After executing the button runs a script from a toolbox (both included in the add-in) which creates a temporary csv for each layer's selected features. The csv has a field for each selected OBJECTID, and the assets path. The AddAttachment tool is then run using the csv file, which then adds the attachments to the layer (Layers must already have attachments enabled). The csv file is then deleted

The temporary csv is built as follows
```
OBJECTID, ASSET
177,      C:/Path/To/Asset1.png
177,      C:/Path/To/Asset2.png
178,      C:/Path/To/Asset1.png
ETC...
```
# How to Use This Add-in
## How to build the add-in Package.
The add-in can be built using the **makeaddin.py** python script.  If you wish to build the add-in in a different version of ArcGIS, you can open up the **config.xml** file,  and change:
`<Target name="Desktop" version="10.3" />`
to the corresponding version. *__I have not tested this, I am just assuming it would work__*

## Use the Add-in
The __*.esriaddin__ file can be opened from the file explorer to install the add-in.  To install it manually, you can do so from ESRI Arcmap in *Customize>Customize Mode>Add From File...* and select the esriaddin file.  It seems you must restart ArcMap to be sure of the changes.  Then you can add the toolbar to ArcMap via *Customize>Customize Mode>Toolbar Tab* and check the *"Batch Attach Toolbar"*

## Troubleshooting
If the toolbar doesn't show up, or the button changes to "Missing", there is something wrong with import. Try restarting Arcmap. If that doesn't work, uninstall the add-in from the add-in manager (*Customize>Add-in Manager*), and try to reinstall using *Customize>Customize Mode>Toolbar Tab*. Before you do, open the python console in arcmap (*Geoprocessing>Python*) which will display any error messages (such as version issues).

## Use with different ArcGIS Versions
To build this add-in for different ArcGIS versions, so far all I've needed to do was to change the version variable in the __config.xml__ file.  This can be done with a simple text editor, changing the target tag:

```
<Target name="Desktop" version="10.3" />
```
to
```
<Target name="Desktop" version="[ARCGIS VERSION NUMBER HERE]" />
```

Some versions seem to be backwards compatible with other versions, but not all (The original wizard sets this value to 10.1. Trying to load the project into 10.3 caused an error, which I solved by changing the version to 10.3. I've also installed it successfully on a 10.2.1 server using a version of 10.1, (for some reason 10.2 did not work for 10.2.1). Seems it's a bit picky, but is a simple thing to test out. The __*.esriaddin__ file is actually just a zip file, so you can actually open it with a zip editor and change the version in the config.xml file manually without needing to rebuild.

Different versions will be kept in the bin folder, if you wish to try them out.


