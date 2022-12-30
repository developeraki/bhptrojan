
import base64
import win32api
import win32con
import win32gui
import win32ui

def get_dimension():
    width  = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    top    = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    left   = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)

    return (width, top, left, height)

def screenshot(name='screenshot'):
    hdesktop = win32gui.GetDesktopWindow()
    width, height, left, top = get_dimension()
    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32gui.CreateDCFromHandle(desktop_dc)
    mem_dc = img_dc.CreateCompatibleDC()

    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)

    mem_dc.BitBlt((0,0), (width, height), img_dc, (left, top), win32con.SRCCOPY)
    screenshot.SaveBitmapFile(mem_dc, f'{name}.bmp')

    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())

def run():
    screenshot()
    with open('screenshot.bmp') as f:
        img = f.read()
    return img

if __name__ == '__main__':
    screenshot()