const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');

let mainWindow;

app.on('ready', () => {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            contextIsolation: true, // Use safer settings
            preload: path.join(__dirname, 'preload.js') // Load the preload script
        }
    });

    mainWindow.loadFile('index.html');
});

ipcMain.on('change-color', (event, color) => {
    // Send the color change event back to the renderer process
    mainWindow.webContents.send('set-color', color);
});
