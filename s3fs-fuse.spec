Name:           s3fs-fuse
Version:        1.84
Release:        0%{?dist}
Summary:        FUSE-based file system backed by Amazon S3
Group:          System Environment/Base

License:        GPLv2
URL:            https://github.com/s3fs-fuse/s3fs-fuse
Source0:        https://github.com/s3fs-fuse/s3fs-fuse/archive/%{name}-%{version}.tar.gz

Requires:       fuse >= 2.8.4
Requires:       curl >= 7.0
Requires:       libxml2 >= 2.6
Requires:       openssl >= 0.9

BuildRequires:  automake
BuildRequires:  curl-devel >= 7.0
BuildRequires:  fuse-devel >= 2.8.4
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel >= 2.6
BuildRequires:  mailcap
BuildRequires:  openssl-devel

Conflicts:      fuse-s3fs
Obsoletes:      s3fs

%description
s3fs is a FUSE file system that allows you to mount an Amazon S3 bucket as a
local file system. It stores files natively and transparently in S3 (i.e.,
you can use other programs to access the same files). Maximum file size=64GB
(limited by s3fs, not Amazon).
.

s3fs is stable and is being used in number of production environments, e.g.,
rsync backup to s3.

%global debug_package %{nil}

%prep

%setup -q

%build

./autogen.sh

%configure

make %{?_smp_mflags}
sed -i 's/\r//' README.md

%install

make install DESTDIR=%{buildroot}

%files

%{_bindir}/s3fs
%{_mandir}/man1/s3fs.1*
%doc AUTHORS README.md


%changelog
* Mon Aug 20 2018 Nico Kadel-Garcia <nkadel@gmail.com> - 1.84
- Update to 1.84
- Add version dependencies to -devel packages for BuildRequires

* Fri Mar 17 2017 Eugene Peregudov <joniknsk@gmail.com> - 1.80
- Bump version to 1.80
- Changed document filename

* Tue Sep 22 2015 Eugene Peregudov <joniknsk@gmail.com> - 1.79-2
- Refactored spec-file from https://github.com/juliogonzalez/s3fs-fuse-rpm

* Thu Jul 30 2015 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.79-1
- Initial build of 1.78 from https://github.com/s3fs-fuse/s3fs-fuse

* Sat Apr 25 2015 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.78-1
- Initial build of 1.78 from https://github.com/s3fs-fuse/s3fs-fuse

* Mon Apr 28 2014 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.77-1
- Initial build of 1.77 from https://github.com/s3fs-fuse/s3fs-fuse

* Thu May 31 2012 Corey Gilmore <git@cfgci.com> - 1.61-1
- Initial build of 1.61. Disabled generation of useless debug package. Using spec from https://bugzilla.redhat.com/show_bug.cgi?id=725292

* Mon Aug 15 2011 Jorge A Gallegos <kad@blegh.net> - 1.58-5
- Minor mod to get rid of macro in changelog

* Sun Jul 31 2011 Jorge A Gallegos <kad@blegh.net> - 1.58-4
- Got rid of unnecessary buildroot cleaning

* Sun Jul 31 2011 Jorge A Gallegos <kad@blegh.net> - 1.58-3
- Moved passwd-s3fs to docs folder

* Wed Jul 27 2011 Jorge A Gallegos <kad@blegh.net> - 1.58-2
- Added docs to files section in spec
- Password file passwd-s3fs is installed as 0644 and changed in post

* Sun Jul 24 2011 Jorge A Gallegos <kad@blegh.net> - 1.58-1
- Initial build
