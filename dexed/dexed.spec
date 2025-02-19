%global debug_package %{nil}

# relative directory where the build results is placed
%global builddest redhat-linux-build/Source/Dexed_artefacts
%global gitref gite087754

Name:           dexed
Version:        0.9.8
Release:        1.%{gitref}%{?dist}
Summary:        Standalone version of Dexed a synth that is closely modeled on the Yamaha DX7

License:        GPLv3
URL:            https://github.com/asb2m10/dexed

# Make a tarball of the source code with all submodules included
# git clone --recurse-submodules git@github.com:asb2m10/dexed.git  
# git ls-files --recurse-submodules | tar caf ~/rpmbuild/SOURCES/dexed-0.9.8.tar.gz --xform s:^:dexed-0.9.8/: --verbatim-files-from -T- 

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  pkgconfig(alsa) 
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(x11) 
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(libcurl)

%description
Dexed is a multi platform, multi format plugin synth that is closely modeled on the Yamaha DX7.
Dexed is also a midi cartridge librarian/manager for the DX7.
This package contains the standalone version of Dexed.

%package clap
Summary:	CLAP plugin of Dexed a synth that is closely modeled on the Yamaha DX7

%description clap
Dexed is a multi platform, multi format plugin synth that is closely modeled on the Yamaha DX7.
Dexed is also a midi cartridge librarian/manager for the DX7.
This package contains Dexed as a CLAP plugin.

%package vst3
Summary:	VST3 plugin of Dexed a synth that is closely modeled on the Yamaha DX7

%description vst3
Dexed is a multi platform, multi format plugin synth that is closely modeled on the Yamaha DX7.
Dexed is also a midi cartridge librarian/manager for the DX7.
This package contains Dexed as a VST3 plugin.


%prep
%autosetup


%build
%cmake
%cmake_build

%install
%cmake_install
# cmake does not install the files in the correct directories
# so we need to do it manually
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_libdir}/vst3
install -d -m 755 %{buildroot}%{_libdir}/clap
cp -R %{builddest}/VST3/Dexed.vst3 %{buildroot}%{_libdir}/vst3/ 
install %{builddest}/CLAP/Dexed.clap %{buildroot}%{_libdir}/clap/
install %{builddest}/Standalone/Dexed %{buildroot}%{_bindir}/

%files clap
%{_libdir}/clap/Dexed.clap

%files vst3
%{_libdir}/vst3/Dexed.vst3/*

%files
%doc README.md
%license LICENSE
%{_bindir}/Dexed

%changelog
* Wed Feb 19 2025 Tim Lauridsen <tla@rasmil.dk> - 0.9.8-1.gite087754
  Initial package
