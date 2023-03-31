%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Fast compression and decompression library
Name:		snappy
Version:	1.1.7
Release:	4
Group:		System/Libraries
License:	BSD
URL:		http://google.github.io/snappy/
Source0:	http://github.com/google/snappy/releases/download/%{version}/%{name}-%{version}.tar.gz
# add missing dependency on gtest to snappy_unittest
Patch0:		%{name}-gtest.patch
# fix version macros in snappy-stubs-public.h.in (BZ #1527850)
Patch1:		%{name}-version-macros.patch

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	gtest-devel
BuildRequires:	pkgconfig(lzo2)
BuildRequires:	pkgconfig(zlib)

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
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains libraries and header files for developing applications 
that use %{name}.

%prep
%autosetup -p1
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

# create pkgconfig file
cat << EOF >snappy.pc
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
includedir=%{_includedir}
libdir=%{_libdir}

Name: %{name}
Description: A fast compression/decompression library
Version: %{version}
Cflags: -I\${includedir}
Libs: -L\${libdir} -lsnappy
EOF

install -m644 -D snappy.pc %{buildroot}%{_libdir}/pkgconfig/snappy.pc

%files -n %{libname}
%{_libdir}/libsnappy.so.%{major}*

%files -n %{develname}
%doc format_description.txt
%{_includedir}/snappy*.h
%{_libdir}/libsnappy.so
%{_libdir}/cmake/Snappy
%{_libdir}/pkgconfig/snappy.pc
