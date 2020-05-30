Name:		nano
Version:	4.9.3
Release:	0
Summary:	Nano is now part of Apache CouchDB
License:	GPLv3+
URL:		https://www.nano-editor.org
Source0:	https://www.nano-editor.org/dist/latest/%{name}-%{version}.tar.xz

BuildRequires:	file-devel gettext-devel gcc git ncurses-devel sed texinfo groff
Conflicts:	filesystem < 3

%description
Nano is now part of Apache CouchDB.

%package_help

%prep
%autosetup -S git


%build
install -d build
cd build
%global _configure ../configure
%configure
%make_build

sed -e 's/# set nowrap/set nowrap/' \
    -e 's/^#.*set speller.*$/set speller "hunspell"/' \
    -e 's|^# \(include "/usr/share/nano/\*.nanorc"\)|\1|' \

%install
cd build
%make_install
rm -rf %{buildroot}%{_infodir}/dir
rm -rf %{buildroot}%{_docdir}/nano/{nano,nano.1,nanorc.5,rnano.1}.html

install -d %{buildroot}%{_sysconfdir}

%find_lang %{name}

%files -f build/%{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%license COPYING

%{_bindir}/*
%{_datadir}/nano
%{_infodir}/nano.info*

%files help
%defattr(-,root,root)
%doc ChangeLog INSTALL NEWS README THANKS TODO
%doc build/doc/sample.nanorc
%doc doc/nano.html
%{_mandir}/man*/*
%{_defaultdocdir}/nano/faq.html

%changelog
* Sat May 30 2020 SimpleUpdate Robot <tc@openeuler.org>
- Update to version 4.9.3

* Fri Jan 17 2020 Lei Zhang <ricky.z@huawei.com> - 4.5-2
- Remove useless nanorc config file

* Tue Nov 26 2019 openEuler Buildteam <buildteam@openeuler.org> - 4.5-1
- Package init
