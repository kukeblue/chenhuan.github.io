// All of the Node.js APIs are available in the preload process.
// It has the same sandbox as a Chrome extension.

window.addEventListener('DOMContentLoaded', () => {

    // const mainWindow = BrowserWindow.getAllWindows()
    // console.log('窗口启动成功，当前的x,y', mainWindow.x, mainWindow.y)
    // alert(12312312)
    // const replaceText = (selector, text) => {
    //     const element = document.getElementById(selector)
    //     if (element) element.innerText = text
    // }

    // for (const type of ['chrome', 'node', 'electron']) {
    //     replaceText(`${type}-version`, process.versions[type])
    // }
})