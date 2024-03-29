#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-LatencyUtils
Version  : 2.0.3
Release  : 1
URL      : https://github.com/LatencyUtils/LatencyUtils/archive/LatencyUtils-2.0.3.tar.gz
Source0  : https://github.com/LatencyUtils/LatencyUtils/archive/LatencyUtils-2.0.3.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/latencyutils/LatencyUtils/2.0.3/LatencyUtils-2.0.3.jar
Source2  : https://repo.maven.apache.org/maven2/org/latencyutils/LatencyUtils/2.0.3/LatencyUtils-2.0.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0
Requires: mvn-LatencyUtils-data = %{version}-%{release}
Requires: mvn-LatencyUtils-license = %{version}-%{release}

%description
LatencyUtils
============
A latency stats tracking package
The LatencyUtils package includes useful utilities for tracking latencies. Especially
in common in-process recording scenarios, which can exhibit significant coordinated
omission sensitivity without proper handling. LatencyStats instances are used to
track recorded latencies in the common use case the often follow this pattern:

%package data
Summary: data components for the mvn-LatencyUtils package.
Group: Data

%description data
data components for the mvn-LatencyUtils package.


%package license
Summary: license components for the mvn-LatencyUtils package.
Group: Default

%description license
license components for the mvn-LatencyUtils package.


%prep
%setup -q -n LatencyUtils-LatencyUtils-2.0.3

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-LatencyUtils
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-LatencyUtils/LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/latencyutils/LatencyUtils/2.0.3
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/latencyutils/LatencyUtils/2.0.3/LatencyUtils-2.0.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/latencyutils/LatencyUtils/2.0.3
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/latencyutils/LatencyUtils/2.0.3/LatencyUtils-2.0.3.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/latencyutils/LatencyUtils/2.0.3/LatencyUtils-2.0.3.jar
/usr/share/java/.m2/repository/org/latencyutils/LatencyUtils/2.0.3/LatencyUtils-2.0.3.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-LatencyUtils/LICENSE
