%global debug_package %{nil}
%global gitdate .git20250225.cc2adc9
%global builddest bin

Name:           vst3sdk
Version:        1.0.0
Release:        1%{?gitdate}%{?dist}
Summary:        VST3 SDK for audio plugin development

License:        GPLv3+
URL:            hhttps://github.com/steinbergmedia/vst3sdk

# The source for this package was pulled from upstream's vcs.
# check here : https://github.com/timlau/spec_files/tree/master/plpugins/
# for a Makefile that can be used to create the source tarball
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(xcb-keysyms)

%description
A VST plug-in is an audio processing component that is utilized within a host application. This host application provides the audio or/and event streams that are processed by the plug-in's code. Generally speaking, a VST plug-in can take a stream of audio data, apply a process to the audio, and return the result to the host application. A VST plug-in performs its process normally using the processor of the computer. The audio stream is broken down into a series of blocks. The host supplies the blocks in sequence. The host and its current environment control the block-size. The VST plug-in maintains the status of all its own parameters relating to the running process: The host does not maintain any information about what the plug-in did with the last block of data it processed.

%prep
%autosetup

%build
%cmake -DSMTG_ENABLE_VST3_PLUGIN_EXAMPLES=OFF -DSMTG_ENABLE_VST3_HOSTING_EXAMPLES=OFF 
%cmake_build

%install
%cmake_install


%files 
%license LICENSE.txt
%doc README.md


%changelog
* Sun Feb 23 2025 Tim Lauridsen <tla@rasmil.dk> - 1.0.0-1
- Initial package