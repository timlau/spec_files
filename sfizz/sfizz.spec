Name:           sfizz
Version:        1.2.3
Release:        2%{?dist}
Summary:        Sampler plugin and library for SFZ instruments

License:        BSD-2-Clause
URL:            https://github.com/sfztools/sfizz-ui

# The source for this package was pulled from upstream's vcs.
# chech here : https://github.com/timlau/spec_files/tree/master/sfizz
# for a Makefile that can be used to create the source tarball

Source0:        %{name}-%{version}.tar.gz

BuildRequires: pipewire-jack-audio-connection-kit-devel
BuildRequires: freetype-devel
BuildRequires: libX11-devel 
BuildRequires: libxcb-devel 
BuildRequires: xcb-util-devel 
BuildRequires: xcb-util-cursor-devel 
BuildRequires: xcb-util-keysyms-devel 
BuildRequires: libxkbcommon-devel 
BuildRequires: libxkbcommon-x11-devel 
BuildRequires: fontconfig-devel 
BuildRequires: cairo-devel 
BuildRequires: pango-devel
BuildRequires: cmake
BuildRequires: clang

%description
Sfizz is a musical sampler, available as LV2 and VST plugins for musicians,
and a library for developers.

%package vst3
Summary:   Sfizz VST3 plugin

%description vst3
Sfizz VST3 Plugins

%package lv2
Summary:   sfizz LV2 plugin

%description lv2
Sfizz LV2 Plugins

%package pd
Summary:   Sfizz puredata (pd) plugin

%description pd
Sfizz puredata (pd) plugin

%package -n libsfizz1
Summary:   Library files for Sfizz
Group:     Development/Libraries/C and C++

%description -n libsfizz1
Runtime files for the Sfizz library.

%package -n libsfizz1-devel
Summary:   Development files for Sfizz
Requires:  libsfizz1 = %{version}-%{release}
Group:     Development/Libraries/C and C++

%description -n libsfizz1-devel
Development files for the Sfizz library.

%prep
%setup

%build
%cmake -DPLUGIN_PUREDATA=ON -DENABLE_LTO=OFF -DLV2_PLUGIN_INSTALL_DIR=%{_libdir}/lv2 -DVST3_PLUGIN_INSTALL_DIR=%{_libdir}/vst3 -DPD_PLUGIN_INSTALL_DIR=%{_libdir}/pd/extra -DBUILD_SHARED_LIBS=OFF -DCMAKE_CXX_STANDARD=17 .
%cmake_build

%install
%cmake_install

%files
%doc README.md
%{_bindir}/sfizz_jack
%{_bindir}/sfizz_render
%{_mandir}/man1/sfizz_jack.1.gz
%{_mandir}/man1/sfizz_render.1.gz

%files vst3
%dir %{_libdir}/vst3/sfizz.vst3
%{_libdir}/vst3/sfizz.vst3/*

%files lv2
%dir %{_libdir}/lv2/sfizz.lv2
%{_libdir}/lv2/sfizz.lv2/*

%files pd
%dir %{_libdir}/pd/extra/sfizz
%{_libdir}/pd/extra/sfizz/*


%files -n libsfizz1
%{_libdir}/libsfizz.so.*

%files -n libsfizz1-devel
%{_libdir}/libsfizz.so
%{_includedir}/sfizz.h
%{_includedir}/sfizz.hpp
%{_includedir}/sfizz_message.h
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/sfizz.pc


%post -n libsfizz1 -p /sbin/ldconfig
%postun -n libsfizz1 -p /sbin/ldconfig

%post -n libsfizz1-devel -p /sbin/ldconfig
%postun -n libsfizz1-devel -p /sbin/ldconfig

%changelog
* Thu Feb 20 2025 Tim Lauridsen <tla@rasmil.dk> - 1.2.3-2
- package released version not the git version
* Tue Feb 18 2025 Tim Lauridsen <tla@rasmil.dk> - 1.2.3-1
- Initial build based on the Open Suse build 
- Added VST3,LV2 & PD subpackages
