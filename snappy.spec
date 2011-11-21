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

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
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

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/libsnappy.so.*

%files devel
%doc format_description.txt
%{_includedir}/snappy*.h
%{_libdir}/libsnappy.so
