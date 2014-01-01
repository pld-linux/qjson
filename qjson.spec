Summary:	Qt implementation of JSON
Summary(pl.UTF-8):	Implementacja Qt formatu JSON
Name:		qjson
Version:	0.8.1
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://downloads.sourceforge.net/qjson/%{name}-%{version}.tar.bz2
# Source0-md5:	323fbac54a5a20c0b8fe45c1ced03e2d
URL:		http://qjson.sourceforge.net/
BuildRequires:	QtCore-devel >= 4
BuildRequires:	cmake >= 2.8.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4
BuildRequires:	qt4-qmake >= 4
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QJson is a Qt-based library that maps JSON data to QVariant objects:
JSON arrays will be mapped to QVariantList instances, while JSON
objects will be mapped to QVariantMap.

%description -l pl.UTF-8
QJson to oparta na Qt biblioteka odwzorowująca dane JSON na obiekty
QVariant: tablice JSON na instancje QVariantList, a obiekty JSON na
QVariantMap.

%package devel
Summary:	Header files for QJson library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki QJson
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= 4

%description devel
Header files for QJson library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki QJson.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README.md
%attr(755,root,root) %{_libdir}/libqjson.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqjson.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqjson.so
%{_pkgconfigdir}/QJson.pc
%{_includedir}/qjson
%{_libdir}/cmake/qjson
