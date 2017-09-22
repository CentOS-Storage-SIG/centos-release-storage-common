Summary: Common release file to establish shared metadata for CentOS Storage SIG
Name: centos-release-storage-common
Epoch: 0
Version: 2
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
Source0: RPM-GPG-KEY-CentOS-SIG-Storage
Source1: CentOS-Storage-common.repo
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
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 644 %SOURCE1 $RPM_BUILD_ROOT/etc/yum.repos.d/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-Storage
/etc/yum.repos.d/CentOS-Storage-common.repo

%changelog
* Fri Sep 22 2017 Niels de Vos <ndevos@redhat.com> - 2-1
- Add CentOS-Storage-common.repo with shared debuginfo repo

* Thu Nov 12 2015 Niels de Vos <ndevos@redha.com> - 1-2
- rebuild for CentOS Extras

* Thu Nov 12 2015 Niels de Vos <ndevos@redha.com> - 1-1
- Basic setup with the gpg key
- Based on the centos-release-virt-common package
