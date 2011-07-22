Summary:	Unicode input engine (using Gucharmap) for IBus platform
Name:		ibus-gucharmap
Version:	1.4.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://github.com/downloads/ueno/ibus-gucharmap/%{name}-%{version}.tar.gz
# Source0-md5:	bb7ead40aecc7c2e75b6db81d33d6d19
URL:		http://github.com/ueno/ibus-gucharmap/
BuildRequires:	gucharmap-devel
BuildRequires:	ibus-devel >= 1.3.99
BuildRequires:	sqlite3-devel
BuildRequires:	vala
Requires:	ibus >= 1.3.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
A Unicode input engine (using Gucharmap) for IBus, which supports
character-map view and searching by Unicode names with easy key
navigation.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_libexecdir}/ibus-engine-gucharmap
%attr(755,root,root) %{_libexecdir}/ibus-setup-gucharmap
%{_datadir}/ibus/component/gucharmap.xml
%{_datadir}/ibus-gucharmap/unicodenames.sqlite3
%{_datadir}/ibus-gucharmap/setup/ibus-gucharmap-preferences.ui
