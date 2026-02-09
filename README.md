# ORM image packer
An ORM image packer based on python.

## Instalation
Download the .exe file in the release section of the repository.

## How to Use the Application
### 1. Select Channel Images

The interface contains four buttons, each labeled with the name of a texture channel (for example: Red, Green, Blue, Alpha).

Click a channel button to select an image for that specific channel.

A file dialog will open, allowing you to choose an image from your computer.

Once selected, a preview of the image will appear to the right of the button.

### 2. Clear a Selected Image

Next to each “Select Image” button, there is a small “X” button.

Click the X button to remove the currently selected image for that channel.

The preview will be cleared and reset.

### 3. Preview Area

Each channel has its own preview square, showing the currently selected image.

This allows you to visually confirm that the correct image is assigned to each channel before proceeding.

### 4. Create the ORM Texture

At the bottom of the window, you will find the “Create ORM Texture” button.

Click this button to generate the ORM texture using the selected channel images.

Below the button, a status text will appear, indicating the current state of the process (e.g. Processing…, Completed, or Error).

### 5. Creation Status

While the ORM texture is being created, the status text will update to reflect the progress.

Once finished, the status message will confirm that the texture has been successfully created.
