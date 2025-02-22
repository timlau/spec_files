# RPM spec files and Makefile's to build audio applications & plugins for Fedora

Build packages are available in the [timlau/audio](https://copr.fedorainfracloud.org/coprs/timlau/audio/) Fedora Copr Repository

## Applications/Plugins

#### AIDA-X
AIDA-X is an Amp Model Player, allowing it to load models of AI trained music gear, which you can then play through guitar

#### dexed
Dexed is a multi platform, multi format plugin synth that is closely modeled on the Yamaha DX7.
Dexed is also a midi cartridge librarian/manager for the DX7.

#### geonkick
Geonkick is a synthesizer that can synthesize elements of percussion. The most basic examples are: kicks, snares, hit-hats, shakers, claps.

#### neural-amp-modeler
LV2 plugin for using neural network machine learning amp models

#### sfizz
Sfizz is a musical sampler, available as LV2 and VST plugins for musicians


## Make targets
Each application/plugin subdirectory contains a Makefile with the following target

#### Clonning the upstream source git repo
```
make clone
```

#### Making an source archive (will clone if needed)
```
make archive
```

#### Making an source src.rpm (will make archive if needed)
```
make srpm
```

#### Building in local mock (will build a new .src.rpm)
```
make mockbuild
```

#### Building in Fedora Copr  (will build a new .src.rpm)
```
make coprbuild
```