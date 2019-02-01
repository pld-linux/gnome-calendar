Summary:	Calendar application for GNOME
Summary(pl.UTF-8):	Aplikacja kalendarza dla GNOME
Name:		gnome-calendar
Version:	3.30.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-calendar/3.30/%{name}-%{version}.tar.xz
# Source0-md5:	786dbad4252f803a69c4aa738aa67260
URL:		https://wiki.gnome.org/Apps/Calendar
BuildRequires:	appstream-glib-devel
BuildRequires:	evolution-data-server-devel >= 3.18.0
BuildRequires:	geoclue2-devel >= 2.4
BuildRequires:	geocode-glib-devel >= 3.24.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gnome-online-accounts-devel >= 3.2.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.22.0
BuildRequires:	gtk+3-devel >= 3.22.20
BuildRequires:	libdazzle-devel >= 3.26.1
BuildRequires:	libgweather-devel >= 3.28.0
BuildRequires:	libical-devel >= 1.0.1
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	meson >= 0.42.0
BuildRequires:	ninja
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.727
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.44.0
Requires:	evolution-data-server >= 3.18.0
Requires:	glib2 >= 1:2.44.0
Requires:	gnome-online-accounts >= 3.2.0
Requires:	gsettings-desktop-schemas >= 3.22.0
Requires:	gtk+3 >= 3.22.20
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
%doc CONTRIBUTING.md HACKING.md NEWS README.md THANKS.md TODO.md
%attr(755,root,root) %{_bindir}/gnome-calendar
%{_datadir}/metainfo/org.gnome.Calendar.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Calendar.service
%{_datadir}/glib-2.0/schemas/org.gnome.calendar.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.calendar.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Calendar.search-provider.ini
%{_desktopdir}/org.gnome.Calendar.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.Calendar.png
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Calendar-symbolic.svg
