Name:		nano
Version:	6.4
Release:	1
Summary:	Nano is a tiny GNU editor
License:	GPLv3+
URL:		https://www.nano-editor.org
Source0:	https://www.nano-editor.org/dist/v6/%{name}-%{version}.tar.xz

BuildRequires:	file-devel gettext-devel gcc ncurses-devel sed texinfo groff
Conflicts:	filesystem < 3

%description
Nano is a tiny GNU editor

%package_help

%prep
%autosetup -p1


%build
install -d build
cd build
%global _configure ../configure
%configure
%make_build

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
* Wed Aug 31 2022 hkgy <kaguyahatu@outlook.com> - 6.4-1
- Update to 6.4

* Sun Jun 12 2022 YukariChiba <i@0x7f.cc> - 6.3-1
- Upgrade version to 6.3
- Fix source url

* Fri May 06 2022 misaka00251 <misaka00251@misakanet.cn> - 6.2-2
- Delete incomplete stuff

* Wed Feb 23 2022 misaka00251 <misaka00251@misakanet.cn> - 6.2-1
- Update to version 6.2

* Mon Aug 02 2021 chenyanpanHW <chenyanpan@huawei.com> - 4.9.3-2
- DESC: delete -S git from %autosetup, and delete BuildRequires git

* Thu Sep 10 2020 baizhonggui <baizhonggui@huawei.com> - 4.9.3-1
- Modify source0

* Sat May 30 2020 SimpleUpdate Robot <tc@openeuler.org>
- Update to version 4.9.3

* Fri Jan 17 2020 Lei Zhang <ricky.z@huawei.com> - 4.5-2
- Remove useless nanorc config file

* Tue Nov 26 2019 openEuler Buildteam <buildteam@openeuler.org> - 4.5-1
- Package init
