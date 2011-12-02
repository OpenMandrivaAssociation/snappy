%define major   1
%define libname %mklibname	snappy %major
%define devname %mklibname	snappy -d


Name:           snappy
Version:        1.0.4
Release:        2
Summary:        Fast compression and decompression library
Group:          System/Libraries
License:        BSD
URL:            http://code.google.com/p/snappy/
Source0:        http://snappy.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRequires:  gtest-devel

%description
Snappy is a compression/decompression library. It does not aim for maximum 
compression, or compatibility with any other compression library; instead, it 
aims for very high speeds and reasonable compression. For instance, compared to 
the fastest mode of zlib, Snappy is an order of magnitude faster for most 
inputs, but the resulting compressed files are anywhere from 20% to 100% 
bigger. 


%package -n %libname
Summary:	Fast compression and decompression library
Group:		System/Libraries


%description -n %libname
Shared libraries of snappy for software using it.




%package -n	%devname
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description -n	%devname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
autoreconf -v --install

%configure CXXFLAGS="%{optflags} -DNDEBUG" --disable-static
%make

%install
%makeinstall_std
rm -rf %{buildroot}%{_datadir}/doc/snappy/
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%check
make check

%files -n %libname
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/libsnappy.so.*

%files -n %devname
%doc format_description.txt
%{_includedir}/snappy*.h
%{_libdir}/libsnappy.so
