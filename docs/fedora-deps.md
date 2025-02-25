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
| libjack-jackd2-dev     | pipewire-jack-audio-connection-kit-devel [^1] |
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
|                        |                                               |
|                        |                                               |
|                        |                                               |
|                        |                                               |
|                        |                                               |
|                        |                                               |
|                        |                                               |
|                        |                                               |
|                        |                                               |
|                        |                                               |
|                        |                                               |
|                        |                                               |
|                        |                                               |
|                        |                                               |
 

 [^1]: sometimes pkgconfig(jack) is needed if the package has problems with building with the pipewire-jack 