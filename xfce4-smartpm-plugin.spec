Summary: 	A Smart plugin for the Xfce panel
Name: 		xfce4-smartpm-plugin
Version: 	0.4.0
Release: 	%mkrel 10
License:	GPLv2+
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-smartpm-plugin
Source0: 	http://goodies.xfce.org/releases/xfce4-smartpm-plugin/%{name}-%{version}.tar.bz2
Patch0:		xfce4-smartpm-plugin-0.4.0-libnotify-0.7.patch
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	gksu
Requires:	gksu
Requires:	smart-gui
Obsoletes:	xfce-smartpm-plugin
Obsoletes:	xfce-smart-plugin
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
A Xfce panel plugin for Smart Package Manager.

%prep
%setup -q
%patch0 -p0

%build
export GKSU="/usr/bin/gksu"
export GKSUDO="/usr/bin/gksudo"
export SU="/bin/su"
export SUDO="/usr/bin/sudo"

%configure2_5x \
	--enable-libnotify
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang %{name}

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog AUTHORS README
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/xfce4-smart.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
