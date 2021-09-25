Summary:	Calendar application for GNOME
Summary(pl.UTF-8):	Aplikacja kalendarza dla GNOME
Name:		gnome-calendar
Version:	41.0
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-calendar/41/%{name}-%{version}.tar.xz
# Source0-md5:	a7bae93e5d76ee02405499a116a681b3
URL:		https://wiki.gnome.org/Apps/Calendar
BuildRequires:	evolution-data-server-devel >= 3.33.2
BuildRequires:	geoclue2-devel >= 2.4
BuildRequires:	geocode-glib-devel >= 3.24.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.67.5
BuildRequires:	gnome-online-accounts-devel >= 3.2.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.22.0
BuildRequires:	gtk+3-devel >= 3.22.20
BuildRequires:	libdazzle-devel >= 3.33.1
BuildRequires:	libgweather-devel >= 40.0
BuildRequires:	libhandy1-devel >= 1.0.0
BuildRequires:	libical-devel >= 1.0.1
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	meson >= 0.53.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.67.5
Requires:	evolution-data-server >= 3.33.2
Requires:	geoclue2 >= 2.4
Requires:	geocode-glib >= 3.24.0
Requires:	glib2 >= 1:2.67.5
Requires:	gnome-online-accounts >= 3.2.0
Requires:	gsettings-desktop-schemas >= 3.22.0
Requires:	gtk+3 >= 3.22.20
Requires:	hicolor-icon-theme
Requires:	libdazzle >= 3.33.1
Requires:	libgweather >= 40.0
Requires:	libhandy1 >= 1.0.0
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
%{_datadir}/metainfo/org.gnome.Calendar.appdata.xml
%{_desktopdir}/org.gnome.Calendar.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Calendar.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Calendar.Devel.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Calendar-symbolic.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Calendar.Devel-symbolic.svg
