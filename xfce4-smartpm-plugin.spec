Summary: 	A Smart plugin for the Xfce panel
Name: 		xfce4-smartpm-plugin
Version: 	0.4.0
Release: 	10
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


%changelog
* Thu Apr 26 2012 Crispin Boylan <crisb@mandriva.org> 0.4.0-10
+ Revision: 793581
- Use gksu instead of old ktsuss

* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 0.4.0-9
+ Revision: 791565
- Rebuild

* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 0.4.0-8
+ Revision: 790057
- Rebuild for xfce 4.10

* Tue Apr 19 2011 Funda Wang <fwang@mandriva.org> 0.4.0-7
+ Revision: 656003
- rebuild for libnotify 0.7

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-6mdv2011.0
+ Revision: 615629
- the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-5mdv2010.1
+ Revision: 543438
- rebuild for mdv 2010.1

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 0.4.0-4mdv2010.0
+ Revision: 446135
- rebuild

* Thu Mar 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-3mdv2009.1
+ Revision: 349479
- rebuild for xfce-4.6.0

* Sat Dec 06 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.0-2mdv2009.1
+ Revision: 311325
- update to new version 0.4.0

* Sat Nov 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-4mdv2009.1
+ Revision: 305939
- obsolete xfce-smart-plugin

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-3mdv2009.1
+ Revision: 295028
- rebuild for new Xfce4.6 beta1

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 0.3.2-2mdv2009.0
+ Revision: 269793
- rebuild early 2009.0 package (before pixel changes)

* Wed May 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.2-1mdv2009.0
+ Revision: 209634
- update to new version 0.3.2

* Sat Mar 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.1-2mdv2008.1
+ Revision: 182169
- use ktsuss for su/sudo actions

* Sat Feb 02 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.1-1mdv2008.1
+ Revision: 161514
- new version

* Thu Jan 10 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-1mdv2008.1
+ Revision: 147735
- new version
- enable notifications with use of libnotify

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.2-2mdv2008.1
+ Revision: 110138
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- do not package COPYING file
- add REAMDE file to the docs
- use upstream name

* Tue Oct 09 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.2-1mdv2008.1
+ Revision: 96288
- new version

* Sun Sep 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.1-1mdv2008.0
+ Revision: 93974
- new version

* Sat Aug 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-1mdv2008.0
+ Revision: 71216
- new version
- new name
- fix file list
- remove scriplets
- change name, closer to upstream

* Fri May 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.2-1mdv2008.0
+ Revision: 31183
- Import xfce-smart-plugin

