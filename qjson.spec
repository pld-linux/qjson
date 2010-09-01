#
Summary:	Qt implementation of JSON
Summary(pl.UTF-8):	Implementacja Qt formatu JSON
Name:		qjson
Version:	0.7.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://downloads.sourceforge.net/project/qjson/qjson/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	5a833ad606c164ed8aa69f0873366ace
URL:		http://qjson.sourceforge.net/
BuildRequires:	QtCore-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QJson is a qt-based library that maps JSON data to QVariant objects:
JSON arrays will be mapped to QVariantList instances, while JSON
objects will be mapped to QVariantMap.

%package devel
Summary:	Header files for qjson
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki qjson
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for qjson.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla qjson.

%prep
%setup -q -n %{name}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

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
%attr(755,root,root) %ghost %{_libdir}/libqjson.so.0
%attr(755,root,root) %{_libdir}/libqjson.so.0.7.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqjson.so
%{_libdir}/pkgconfig/QJson.pc
%{_includedir}/qjson
%{_datadir}/apps/cmake/modules/FindQJSON.cmake
