Name:           autoconf-archive
Version:        2019.01.06
Release:        1
Summary:        The Autoconf Macro Archive
License:        GPLv3+ with exceptions
URL:            http://www.gnu.org/software/autoconf-archive/
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch
Requires:       autoconf

%description
The GNU Autoconf Archive is a collection of more than 450 macros for
GNU Autoconf that have been contributed as free software by friendly
supporters of the cause from all over the Internet.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
ln -sf ../gnulib gnulib
echo %{version} | cut -d '+' -f 1 > .tarball-version
cp .tarball-version .version
# We do not want to depend on git, but we should find nicer thing to do here :/
sed -i '/build-aux\/gitlog-to-changelog/d' ./bootstrap.sh
sed -i '/gen-authors.sh/d' ./bootstrap.sh
sed -i "s/ doc//" Makefile.am
sed -i "s/ doc\/Makefile//" configure.ac
touch AUTHORS
rm -rf .git
./bootstrap.sh
%configure
#make maintainer-all
%make_build

%install
%make_install INSTALL="install -p"
# remove dir file which will be generated by /sbin/install-info
rm -frv %{buildroot}%{_infodir}/dir
# document files are installed another location
rm -frv %{buildroot}%{_datadir}/doc/%{name}

%files
%doc AUTHORS NEWS README TODO
%license COPYING*
%{_datadir}/aclocal/*.m4
#%{_infodir}/autoconf-archive.info*
