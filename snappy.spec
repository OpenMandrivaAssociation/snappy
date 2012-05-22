%define	major	1
%define	libname		%mklibname %{name} %{major}
%define	develname	%mklibname %{name} -d

Summary:	Fast compression and decompression library
Name:		snappy
Version:	1.0.5
Release:	2
Group:		System/Libraries
License:	BSD
URL:		http://code.google.com/p/snappy/
Source0:	http://snappy.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRequires:	gtest-devel

%description
Snappy is a compression/decompression library. It does not aim for maximum 
compression, or compatibility with any other compression library; instead, it 
aims for very high speeds and reasonable compression. For instance, compared to 
the fastest mode of zlib, Snappy is an order of magnitude faster for most 
inputs, but the resulting compressed files are anywhere from 20% to 100% 
bigger. 

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for %{name}
%rename		%{name}

%description -n %{libname}
Snappy is a compression/decompression library. It does not aim for maximum 
compression, or compatibility with any other compression library; instead, it 
aims for very high speeds and reasonable compression. For instance, compared to 
the fastest mode of zlib, Snappy is an order of magnitude faster for most 
inputs, but the resulting compressed files are anywhere from 20% to 100% 
bigger. 

This package contains shared libraries for %{name}.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
This package contains libraries and header files for developing applications 
that use %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std
rm -rf %{buildroot}%{_datadir}/doc/snappy/

%check
make check

%files -n %{libname}
%doc COPYING 
%{_libdir}/libsnappy.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog NEWS README
%doc format_description.txt
%{_includedir}/snappy*.h
%{_libdir}/libsnappy.so

