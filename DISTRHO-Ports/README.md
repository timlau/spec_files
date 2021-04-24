# Building DISTRORHO-Ports packages for Fedora 34

https://github.com/DISTRHO/DISTRHO-Ports


## Install tool for local build

```
sudo dnf install fedora-packager
rpmdev-setuptree

```

## Install build requirements

```
sudo dnf install gcc-c++ meson fftw-devel alsa-lib-devel freetype-devel \
                 libX11-devel libXext-devel mesa-libGL-devel libXcursor-devel
```

## Build from spec

Download sources to ~/rpmbuild/SOURCES

```
spectool -g -R lv2-DISTRHO.spec
rpmbuild -ba lv2-DISTRORHO.spec
```

## Rebuild from .SRPM

```
rpmbuild --rebuild lv2-DISTRHO-0-0.1.2021_03_15.fc34.src.rpm
```

### List RPMs created 
```
ls ~/rpmbuild/RPMS/x86_64/
lv2-DISTRHO-Arctican-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-dexed-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-dRowAudio-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-drumsynth-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-EasySSP-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-eqinox-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-HiReSam-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-JuceOPL-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-KlangFalter-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-LUFS-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-Luftikus-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-Obxd-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-PitchedDelay-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-ReFine-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-StereoSourceSeparation-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-SwankyAmp-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-TAL-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-Temper-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-Vex-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-vitalium-0-0.1.2021_03_15.fc34.x86_64.rpm
lv2-DISTRHO-Wolpertinger-0-0.1.2021_03_15.fc34.x86_64.rpm
```

### Install RPMs

'''
sudo dnf install ~/rpmbuild/RPMS/x86_64/lv2-DISTRHO-*.rpm
'''
