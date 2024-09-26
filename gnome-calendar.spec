# TODO: use gtk4-update-icon-cache
Summary:	Calendar application for GNOME
Summary(pl.UTF-8):	Aplikacja kalendarza dla GNOME
Name:		gnome-calendar
Version:	47.0
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-calendar/47/%{name}-%{version}.tar.xz
# Source0-md5:	9964ceacaa560d4e07f226f1aa0b7492
Patch0:		%{name}-no-update.patch
URL:		https://wiki.gnome.org/Apps/Calendar
# libedataserverui4-1.0, libedataserver-1.2, libecal-2.0
BuildRequires:	evolution-data-server-devel >= 3.45.1
BuildRequires:	evolution-data-server-gtk4-devel >= 3.45.1
BuildRequires:	geoclue2-devel >= 2.4
BuildRequires:	geocode-glib2-devel >= 3.26.3
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.67.5
BuildRequires:	gsettings-desktop-schemas-devel >= 3.22.0
BuildRequires:	gtk4-devel >= 4.15.2
BuildRequires:	libadwaita-devel >= 1.6
BuildRequires:	libgweather4-devel >= 4.0
BuildRequires:	libical-devel >= 1.0.1
BuildRequires:	libsoup3-devel >= 3.0
BuildRequires:	meson >= 0.58.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.67.5
Requires:	evolution-data-server >= 3.45.1
Requires:	evolution-data-server-gtk4-libs >= 3.45.1
Requires:	geoclue2 >= 2.4
Requires:	geocode-glib2 >= 3.26.3
Requires:	glib2 >= 1:2.67.5
Requires:	gsettings-desktop-schemas >= 3.22.0
Requires:	gtk4 >= 4.15.2
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.6
Requires:	libgweather4 >= 4.0
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
%patch0 -p1

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%doc NEWS README.md THANKS.md TODO.md
%attr(755,root,root) %{_bindir}/gnome-calendar
%{_datadir}/dbus-1/services/org.gnome.Calendar.service
%{_datadir}/glib-2.0/schemas/org.gnome.calendar.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.calendar.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Calendar.search-provider.ini
%{_datadir}/metainfo/org.gnome.Calendar.metainfo.xml
%{_desktopdir}/org.gnome.Calendar.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Calendar.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Calendar.Devel.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Calendar-symbolic.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Calendar.Devel-symbolic.svg
