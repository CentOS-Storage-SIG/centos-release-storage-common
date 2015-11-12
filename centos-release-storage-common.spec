Summary: Common release file to establish shared metadata for CentOS Storage SIG
Name: centos-release-storage-common
Epoch: 0
Version: 1
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
Source0: RPM-GPG-KEY-CentOS-SIG-Storage
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
BuildArch: noarch

Provides: centos-release-storage-common
Requires: centos-release

BuildRoot: %{_tmppath}/%{name}-root

%description
Common files needed by other centos-release components in the Storage SIG

%prep
%setup -q -n %{name} -T -c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/pki/rpm-gpg/
install -m 644 %SOURCE0 $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-Storage

%changelog
* Thu Nov 12 2015 Niels de Vos <ndevos@redha.com> - 1-1
- Basic setup with the gpg key
- Based on the centos-release-virt-common package
