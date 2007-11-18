%define oname xfce4-smartpm-plugin

Summary: 	A Smart plugin for the Xfce panel
Name: 		xfce-smartpm-plugin
Version: 	0.2.2
Release: 	%mkrel 1
License:	GPL
Group: 		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-smartpm-plugin
Source0: 	http://goodies.xfce.org/releases/xfce4-smartpm-plugin/%{oname}-%{version}.tar.bz2
Requires:	xfce-panel >= 4.4
BuildRequires:	xfce-panel-devel >= 4.4
BuildRequires:	libxfcegui4-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	intltool
Requires:	smart-gui
Obsoletes:	xfce-smart-plugin
Provides:	xfce-smart-plugin
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
A Smart plugin for the Xfce panel.

%prep
%setup -qn %{oname}-%{version}

%build

%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

%find_lang %{oname}

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{oname}.lang
%defattr(-,root,root)
%doc ChangeLog COPYING AUTHORS
%{_libdir}/xfce4/panel-plugins/*
%{_datadir}/xfce4/panel-plugins/xfce4-smart.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
