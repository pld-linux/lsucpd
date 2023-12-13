Summary:	List USB-C ports, pd objects and associated info on Linux
Name:		lsucpd
Version:	0.91
Release:	1
License:	BSD
Group:		Applications/System
Source0:	https://github.com/doug-gilbert/lsucpd/archive/r%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6812e5995de948336a903ffb8ad47706
URL:		https://github.com/doug-gilbert/lsucpd
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
List USB-C ports, pd objects and associated info on Linux.

%prep
%setup -q -n %{name}-r%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog LICENSE README
%attr(755,root,root) %{_bindir}/lsucpd
%{_mandir}/man8/lsucpd.8*
%{_mandir}/man8/lsucpd_json.8*
