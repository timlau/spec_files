%global debug_package %{nil}
%global github_release v0.9.8

Name:           dexed
Version:        0.9.8
Release:        1%{?dist}
Summary:        Dexed is a multi platform, multi format plugin synth that is closely modeled on the Yamaha DX7

License:        GPLv3
URL:            https://github.com/asb2m10/dexed
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
Dexed is also a midi cartridge librarian/manager for the DX7

%prep
%autosetup


%build
%cmake
%cmake_build

%install
%cmake_install


%files
%doc README.md
%license doc/GPL.txt
%{_libdir}/lv2/Dexed.lv2/*

%changelog
* Tue Feb 18 2025 Tim Lauridsen <tla@rasmil.dk>
- 
