Name: properties-cpp
Summary: properties-cpp
Version: 0.0.1
Release: 1
Group: Development/Libraries
License: LGPL
URL: https://github.com/sreehax
Source: %{name}-%{version}.tar.bz2

%description
properties-cpp

%prep
%setup -q -n %{name}-%{version}

%install
%define include %{buildroot}/usr/include/properties-cpp
%define pkgconfig %{buildroot}/usr/lib/pkgconfig
mkdir -p %{include}
mkdir -p %{pkgconfig}
install -Dm 644 include/connection.h %{include}
install -Dm 644 include/property.h %{include}
install -Dm 644 include/signal.h %{include}
install -Dm 644 pkgconfig/properties-cpp.pc %{pkgconfig}

%files
%defattr(-,root,root,-)
/usr/lib/pkgconfig/properties-cpp.pc
/usr/include/properties-cpp/signal.h
/usr/include/properties-cpp/property.h
/usr/include/properties-cpp/connection.h
