%define		major 0
%define		apiver 1.2
%define		libname %mklibname %{name} %{apiver} %{major}
%define		develname %mklibname %{name} -d
%define		_disable_lto 1

Summary:	Simple DirectMedia Layer - network
Name:		SDL_net
Version:	1.2.8
Release:	17
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.libsdl.org/projects/SDL_net/
Source0:	http://www.libsdl.org/projects/SDL_net/release/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(sdl)
BuildRequires:	texinfo

%description
This is an example portable network library for use with SDL. Note that this
isn't necessarily how you would want to write a chat program, but it
demonstrates how to use the basic features of the network and GUI libraries.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	pkgconfig(sdl)
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/lib*%{apiver}.so.%{major}*

%files -n %{develname}
%doc README CHANGES
%{_includedir}/SDL/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Mon Mar 19 2012 Andrey Bondrov <abondrov@mandriva.org> 1.2.8-1mdv2012.0
+ Revision: 785486
- New version 1.2.8, do not build static lib, update file list

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-8
+ Revision: 671972
- mass rebuild

* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 1.2.7-7
+ Revision: 634986
- rebuild
- tighten BR

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-6mdv2011.0
+ Revision: 520006
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-5mdv2010.0
+ Revision: 413011
- rebuild

* Sat Mar 21 2009 Funda Wang <fwang@mandriva.org> 1.2.7-4mdv2009.1
+ Revision: 359982
- recon is not needed
- autoreconf

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.2.7-4mdv2009.0
+ Revision: 225429
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 13 2008 Anssi Hannula <anssi@mandriva.org> 1.2.7-3mdv2008.1
+ Revision: 151078
- obsolete old library name
- provide %%name-devel
- versionize obsoletes
- do not provide old -devel name

* Sun Jan 13 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.7-2mdv2008.1
+ Revision: 150947
- new license policy
- new devel library policy
- drop not needed buildrequire on esound-devel (?)
- spec file clean
- correct libification

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Thu Jul 26 2007 Funda Wang <fwang@mandriva.org> 1.2.7-1mdv2008.0
+ Revision: 55749
- New version 1.2.7

* Mon May 21 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.6-2mdv2008.0
+ Revision: 29276
- rebuild


* Sun Jan 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.6-1mdv2007.0
+ Revision: 114684
- Import SDL_net

* Sun Jan 28 2007 Götz Waschk <waschk@mandriva.org> 1.2.6-1mdv2007.1
- rebuild

* Fri May 19 2006 Götz Waschk <waschk@mandriva.org> 1.2.6-1mdk
- source URL
- new version

* Sat Jan 07 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.2.5-5mdk
- Rebuild

* Sat Nov 13 2004 Götz Waschk <waschk@linux-mandrake.com> 1.2.5-4mdk
- rebuild

* Fri Jun 04 2004 Götz Waschk <waschk@linux-mandrake.com> 1.2.5-3mdk
- fix build

