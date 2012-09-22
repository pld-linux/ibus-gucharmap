Summary:	Unicode input engine (using Gucharmap) for IBus platform
Summary(pl.UTF-8):	Unikodowy silnik wejściowy (wykorzystujący Gucharmap) dla platformy IBus
Name:		ibus-gucharmap
Version:	1.4.0
Release:	2
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/ueno/ibus-charmap/downloads
Source0:	https://github.com/downloads/ueno/ibus-charmap/%{name}-%{version}.tar.gz
# Source0-md5:	bb7ead40aecc7c2e75b6db81d33d6d19
URL:		http://github.com/ueno/ibus-charmap/
BuildRequires:	gettext-devel >= 0.16.1
BuildRequires:	gucharmap-devel >= 3
BuildRequires:	ibus-devel >= 1.3.99
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	sqlite3-devel
# not needed for releases (which contain generated C sources)
#BuildRequires:	vala >= 2:0.12.0
Requires:	ibus >= 1.3.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
A Unicode input engine (using Gucharmap) for IBus, which supports
character-map view and searching by Unicode names with easy key
navigation.

%description -l pl.UTF-8
Unikodowy silnik wejściowy (wykorzystujący Gucharmap) dla platformy
IBus. Obsługuje widok z mapą znaków i wyszukiwaniem po nazwach znaków
unikodowych z łatwą nawigacją przy użyciu klawiszy.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not yet (only empty translation exist)

#find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libexecdir}/ibus-engine-gucharmap
%attr(755,root,root) %{_libexecdir}/ibus-setup-gucharmap
%{_datadir}/ibus/component/gucharmap.xml
%{_datadir}/ibus-gucharmap
