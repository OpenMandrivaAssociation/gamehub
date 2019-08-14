%define unstablever -16-dev
%define badunstablever .16.dev
%define oname GameHub

Name:           gamehub
Version:        0.14.2
Release:        0%{badunstablever}
Summary:        Unified library for all your games, written in Vala using GTK+3
License:        GPLv3
Group:          Games
URL:            https://tkashkin.tk/projects/gamehub/
Source0:        https://github.com/tkashkin/GameHub/archive/%{version}%{unstablever}/%{oname}-%{version}%{unstablever}.tar.gz

BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  vala
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(polkit-gobject-1)

#Optional
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(manette-0.2)

%description
GameHub allows to view, download, install, run and uninstall games from supported sources.

%prep
%setup -qn %{oname}-%{version}%{unstablever}

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/com.github.tkashkin.gamehub
%{_bindir}/com.github.tkashkin.gamehub-overlayfs-helper
%{_datadir}/applications/com.github.tkashkin.gamehub.desktop
%{_datadir}/com.github.tkashkin.gamehub/compat/dosbox/windowed.conf
%{_datadir}/glib-2.0/schemas/com.github.tkashkin.gamehub.gschema.xml
%{_iconsdir}/hicolor/*/apps/com.github.tkashkin.gamehub.svg
%{_datadir}/locale/*/LC_MESSAGES/com.github.tkashkin.gamehub.mo
%{_datadir}/metainfo/com.github.tkashkin.gamehub.appdata.xml
%{_datadir}/polkit-1/actions/com.github.tkashkin.gamehub.policy
