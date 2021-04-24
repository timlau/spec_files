# Building DISTRORHO-Ports packages for Fedora 34


## Install tool for local build

'''
sudo dnf install fedora-packager
rpmdev-setuptree

'''

## Install build requirements
'''
sudo dnf install gcc-c++ meson fftw-devel alsa-lib-devel freetype-devel libX11-devel libXext-devel mesa-libGL-devel libXcursor-devel
'''

## Build from spec

Download sources to ~/rpmbuild/SOURCES
'''
spectool -g -R lv2-DISTRHO.spec
rpmbuild -ba lv2-DISTRORHO.spec
'''

## Rebuild from .SRPM

'''
rpmbuild --rebuild lv2-DISTRHO-0-0.1.2021_03_15.fc34.src.rpm
'''
