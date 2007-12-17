%define name SDL_net
%define version 1.2.7
%define release %mkrel 1
%define lib_name_orig lib%{name}
%define lib_major 1.2
%define lib_name %mklibname %name %{lib_major}

Summary: Simple DirectMedia Layer - network
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.libsdl.org/projects/SDL_net/release/%{name}-%{version}.tar.bz2
License: LGPL
Group: System/Libraries
URL: http://www.libsdl.org/projects/SDL_net/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	X11-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	esound-devel
BuildRequires:	texinfo
BuildRequires:  automake

%description
This is an example portable network library for use with SDL. Note that this
isn't necessarily how you would want to write a chat program, but it
demonstrates how to use the basic features of the network and GUI libraries.

%package -n %{lib_name}
Summary: Main library for %{name}
Group: System/Libraries
Obsoletes: %{name}
Provides: %{name}

%description -n %{lib_name}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{lib_name}-devel
Summary: Headers for developing programs that will use %{name}
Group: Development/C
Requires: %{lib_name} = %{version}
Requires: libSDL-devel
Provides: %{lib_name_orig}-devel = %{version}-%{release}
Obsoletes: %{name}-devel
Provides: %{name}-devel

%description -n %{lib_name}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
rm -f configure
aclocal
autoconf
automake -a -c --foreign

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root)
%doc README CHANGES
%{_libdir}/lib*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%doc README CHANGES
%{_includedir}/SDL/*
%{_libdir}/lib*.so
%{_libdir}/*a
