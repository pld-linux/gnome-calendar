Summary:	Calendar application for GNOME
Summary(pl.UTF-8):	Aplikacja kalendarza dla GNOME
Name:		gnome-calendar
Version:	3.18.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-calendar/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	0f105e3e3e230688246ba8e06876ff41
URL:		https://wiki.gnome.org/Apps/Calendar
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	evolution-data-server-devel >= 3.18.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gnome-common
BuildRequires:	gnome-online-accounts-devel >= 3.2.0
BuildRequires:	gtk+3-devel >= 3.16.0
BuildRequires:	intltool >= 0.40.6
BuildRequires:	libical-devel >= 1.0.1
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.44.0
Requires:	evolution-data-server >= 3.18.0
Requires:	glib2 >= 1:2.44.0
Requires:	gtk+3 >= 3.16.0
Requires:	hicolor-icon-theme
Requires:	libical >= 1.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Calendar is a simple and beautiful calendar application designed
to perfectly fit the GNOME desktop. By reusing the components which
the GNOME desktop is build on, Calendar nicely integrates with the
GNOME ecosystem.

%description -l pl.UTF-8
GNOME Calendar to prosta i ładna aplikacja kalendarza zaprojektowana
tak, aby idealnie pasowała do środowiska GNOME. Poprzez używanie tych
samych komponentów, z których zbudowane jest środowisko, Calendar
ładnie integruje się z ekosystemem GNOME.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/gnome-calendar
%{_datadir}/appdata/org.gnome.Calendar.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Calendar.service
%{_datadir}/glib-2.0/schemas/org.gnome.calendar.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.calendar.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Calendar.search-provider.ini
%{_desktopdir}/org.gnome.Calendar.desktop
%{_iconsdir}/hicolor/*x*/apps/gnome-calendar.png
