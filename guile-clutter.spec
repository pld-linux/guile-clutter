Summary:	Clutter library wrapper for Guile Scheme
Summary(pl.UTF-8):	Wrapper biblioteki Clutter dla Guile Scheme
Name:		guile-clutter
Version:	1.12.2.1
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/guile-gnome/guile-clutter/%{name}-%{version}.tar.gz
# Source0-md5:	db566c9e3148fc92daad7235921ccf96
Patch0:		%{name}-info.patch
Patch1:		%{name}-nox.patch
URL:		http://www.gnu.org/software/guile-gnome/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.12
BuildRequires:	cogl-devel >= 1.12.2
BuildRequires:	clutter-devel >= 1.12.2
BuildRequires:	g-wrap-devel >= 1.9.15
#BuildRequires:	guile-cairo >= 1.10.0
BuildRequires:	guile-cairo >= 1.4.0
BuildRequires:	guile-devel >= 5:2.0.11
BuildRequires:	guile-gnome-atk >= 2.16.4
BuildRequires:	guile-gnome-cairo >= 2.16.4
BuildRequires:	guile-gnome-glib-devel >= 2.16.4
BuildRequires:	guile-gnome-gtk >= 2.16.4
BuildRequires:	guile-gnome-pango >= 2.16.4
BuildRequires:	guile-gnome-platform >= 2.16.4
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	texinfo
Requires:	clutter >= 1.12.2
Requires:	cogl >= 1.12.2
Requires:	g-wrap >= 1.9.15
Requires:	guile >= 5:2.0.11
Requires:	guile-gnome-glib >= 2.16.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Guile-Clutter wraps the Clutter library for Guile Scheme.

%description -l pl.UTF-8
Guile-Clutter obudowuje bibliotekę Clutter dla Guile Scheme.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgw-guile-*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
/sbin/ldconfig
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
/sbin/ldconfig
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libgw-guile-gnome-clutter.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgw-guile-gnome-clutter.so.0
%attr(755,root,root) %{_libdir}/libgw-guile-gnome-clutter.so
%attr(755,root,root) %{_libdir}/libgw-guile-gnome-clutter-glx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgw-guile-gnome-clutter-glx.so.0
%attr(755,root,root) %{_libdir}/libgw-guile-gnome-clutter-glx.so
%{_datadir}/guile-gnome-2/gnome/clutter*.scm
%{_datadir}/guile-gnome-2/gnome/defs/clutter*.defs
%{_datadir}/guile-gnome-2/gnome/defs/cogl-types.defs
%{_datadir}/guile-gnome-2/gnome/gw/clutter*.scm
%{_datadir}/guile-gnome-2/gnome/overrides/clutter*.defs*
%{_pkgconfigdir}/guile-clutter-1.0.pc
%{_infodir}/guile-gnome-clutter.info*
%{_infodir}/guile-gnome-clutter-glx.info*
