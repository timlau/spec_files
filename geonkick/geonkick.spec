%global owner   iurie-sw
%global pname   geonkick

Name:           lv2-%{pname}
Version:        2.8.0
Release:        1%{?dist}
Summary:        Geonkick - a free software percussion synthesizer

License:        GPLv3
URL:            https://github.com/%{owner}/%{pname}
Source0:        https://github.com/%{owner}/%{pname}/archive/refs/tags/v%{version}.tar.gz
# https://github.com/iurie-sw/geonkick/archive/refs/tags/v2.8.0.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(cairo)

%description
Geonkick is a synthesizer that can synthesize elements of percussion. The most basic examples are: kicks, snares, hit-hats, shakers, claps.

%prep
%autosetup -p1 -n %{pname}-%{version}


%build
%cmake -DGKICK_STANDALONE=OFF
%cmake_build

%install
rm -rf $RPM_BUILD_ROOT
%cmake_install


%files
%license LICENSE
%doc README.md
%{_libdir}/lv2/geonkick*.lv2/*
%{_datadir}/%{pname}/
%{_datadir}/icons/hicolor/*/apps/%{pname}*.png
%{_datadir}/icons/hicolor/*/apps/%{pname}*.svg
%{_datadir}/mime/packages/%{pname}.xml

%changelog
* Tue Apr 27 2021 Tim Lauridsen <tla@rasmil.dk> - 2.8.0-1
- Initial SPEC
