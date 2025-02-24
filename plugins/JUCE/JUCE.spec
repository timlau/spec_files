%global debug_package %{nil}
%global gitdate .git20250222.a74ffd3
%global builddest bin

Name:           JUCE
Version:        8.0.6
Release:        1%{?gitdate}%{?dist}
Summary:        JUCE is an open-source cross-platform C++ application framework

License:        GPLv3+
URL:            https://github.com/juce-framework/JUCE

Source0:        https://github.com/juce-framework/%{name}/archive/refs/tags/%{version}.tar.gz
Patch0:         0001-fix-install-location.patch
Patch1:         0002-fix-install-location.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(alsa) 
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(xcomposite)

%description
JUCE is an open-source cross-platform C++ application framework for creating desktop and mobile applications, including VST, VST3, AU, AUv3, AAX and LV2 audio plug-ins and plug-in hosts.

%prep
%autosetup

%build
# set(JUCE_MODULE_PATH "include/JUCE-${JUCE_VERSION}/modules")
%cmake 
%cmake_build 

%install
%cmake_install --prefix %{_prefix}

%files 
%license LICENSE.md
%doc README.md
%{_bindir}/*
%{_libdir}/*    
%{_includedir}/*


%changelog
* Sun Feb 23 2025 Tim Lauridsen <tla@rasmil.dk> - 1.0.0-1
- Initial package