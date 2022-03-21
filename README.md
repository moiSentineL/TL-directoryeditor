# TLauncher Directory Editor

 The .properties Directory Editor for Portable TLauncher made by moiSentineL [here](https://www.reddit.com/r/TLAUNCHER/comments/tjc9r6/tlauncher_on_usb_final/).
 
 This application written in [Python](https://www.python.org) will solve the problem of TLauncher not recognizing the current directory as the main `.minecraft` folder.
 
## Explaination

This application searches for the `tlauncher-2.0.properties` file inside the `.tlauncher` directory and edits the `minecraft.gamedir` value to the `.minecraft` folder existing in the USB Drive.

## How to Use

### Download the zip file from [here](https://github.com/moiSentineL/TL-directoryeditor/releases/download/1.0/tl-directoryeditor.zip)

Extract it onto the root folder of the Portable Minecraft (i.e. the folder which contains the `tlauncher.jar`.
Open the folder and run `tl-directoryeditor.exe`. You **MUST** run the file from correct directory,

**Correct Directory Example:**

    Root Folder
    |
    |- tlauncher.jar
    |- tl-directoryeditor
    |  |- tl-directoryeditor.exe
    |- JavaPortableLauncher
    |  |- Data
    |     |- AppData
    |	  	 |- .minecraft
    |		 |- .tlauncher
    |- CommonFiles

 

## Currently works only for [Portable Minecraft](https://www.reddit.com/r/TLAUNCHER/comments/tjc9r6/tlauncher_on_usb_final/)
