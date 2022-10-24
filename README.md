# pynput/objc example issues on macos monterey

These happen on an M1 Processor. I don't know if they hapen on an Intel processor. I also don't know if they're pynput or objc issues, but since I'm using objc directly, I'm listing them as pynput issues.

## caps_lock.py

I don't know if it's a objc or pynput issue, but on macos monterey listening for caps lock crashes the app.

## nested_crash.py

When starting the Listener AFTER QT6, the whole thing crashes.
