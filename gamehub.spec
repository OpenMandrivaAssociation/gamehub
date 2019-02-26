%define unstablever .1-31-dev
%define oname GameHub

Name:           gamehub
Version:        0.13.1
Release:        0%{unstablever}
Summary:        Unified library for all your games, written in Vala using GTK+3
License:        GPLv3
Group:          Games
URL:            https://tkashkin.tk/projects/gamehub/
Source0:        https://github.com/tkashkin/GameHub/archive/0.13.1-31-dev/%{name}-%{version}%{unstablever}.tar.gz

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  vapigen
BuildRequires:  ninja
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
#{_bindir}/%{name}
