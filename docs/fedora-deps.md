
### Mapping common used ubuntu build deps to fedora deps.

Best practice in Fedora packages is to use the **pkgconfig(dependcy)** format to define build requirements

#### Example

```
BuildRequires:  pkgconfig(alsa)
```

### Mappings

| ubuntu build deps      | Fedora BuildRequire:                          |
| -----------------------| ----------------------------------------------|
| libasound2-dev         | pkgconfig(alsa)                               |
| libjack-jackd2-dev     | pipewire-jack-audio-connection-kit-devel      |
| libfreetype-dev        | pkgconfig(freetype2)                          |
| libfontconfig1-dev     | pkgconfig(fontconfig)                         |
| libx11-dev             | pkgconfig(x11)                                |
| libxcursor-dev         | pkgconfig(xcursor)                            |
| libxext-dev            | pkgconfig(xext)                               |
| libxinerama-dev        | pkgconfig(xinerama)                           |
| libxrandr-dev          | pkgconfig(xrandr)                             |
| libxrender-dev         | pkgconfig(xrender)                            |
| libwebkit2gtk-4.0-dev  | pkgconfig(webkit2gtk-4.0)                     |
| libwebkit2gtk-4.1-dev  | pkgconfig(webkit2gtk-4.1)                     |
| libglu1-mesa-dev       | pkgconfig(gl)                                 |
| mesa-common-dev        | pkgconfig(gl)                                 |
| libxcomposite-dev      | pkgconfig(xcomposite)                         |
| ladspa-sdk             | ladspa-devel                                  |
| libx11-xcb-dev         | pkgconfig(xcb)                                |
| libxcb-util-dev        | pkgconfig(xcb-util)                           |
| libxcb-cursor-dev      | pkgconfig(xcb-cursor)                         |
| libxcb-xkb-dev         | pkgconfig(xkb)                                |
| libxcb-keysyms1-dev    | pkgconfig(xcb-keysyms)                        |
| libxkbcommon-dev       | pkgconfig(xkbcommon)                          |
| libxkbcommon-x11-dev   | pkgconfig(xkbcommon-x11)                      |
| libcairo2-dev          | pkgconfig(cairo)                              |
| libgtkmm-3.0-dev       | pkgconfig(gtkmm-3.0)                          |
| libsqlite3-dev         | pkgconfig(sqlite3)                            |
