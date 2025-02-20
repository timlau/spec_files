# Files for building .rpms files for Fedora 

It contains a the following files
- **.spec** file for building Fedora rpms.
- **Makefile** for 
  - Clonning the upstream source git repo
  - Making an source archive
  - Making an source src.rpm
  - Building in local mock
  - Building in local mock

## Make targets

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