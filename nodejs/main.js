const { app, BrowserWindow } = require('electron')
process.env['ELECTRON_DISABLE_SECURITY_WARNINGS'] = 'true';

function createWindow () {
    let win = new BrowserWindow({
        width: 1024,
        height: 768,
        webPreferences: {
          nodeIntegration: true
        }
    })

    win.loadFile('index.html')
    win.setFullScreen(true)
    // win.webContents.openDevTools()

    win.on('closed', () => {
        win = null;
    })
}

app.on('ready', createWindow)

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})

app.on('activate', () => {
    if (win === null) {
        createWindow()
    }
})