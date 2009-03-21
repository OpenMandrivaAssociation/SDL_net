%define major 0
%define apiver 1.2
%define libname %mklibname %{name} %{apiver} %{major}
%define develname %mklibname %{name} -d

Summary:	Simple DirectMedia Layer - network
Name:		SDL_net
Version:	1.2.7
Release:	%mkrel 4
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.libsdl.org/projects/SDL_net/
Source0:	http://www.libsdl.org/projects/SDL_net/release/%{name}-%{version}.tar.bz2
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	X11-devel
BuildRequires:	libalsa-devel
BuildRequires:	texinfo
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This is an example portable network library for use with SDL. Note that this
isn't necessarily how you would want to write a chat program, but it
demonstrates how to use the basic features of the network and GUI libraries.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}SDL_net1.2 < 1.2.7-2

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	libSDL-devel
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}SDL_net1.2-devel < 1.2.7-2

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*%{apiver}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README CHANGES
%{_includedir}/SDL/*
%{_libdir}/lib*.so
%{_libdir}/*a
