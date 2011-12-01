Name:           powertop
Version:        1.11
Release:        3.1%{?dist}
Summary:        Power consumption monitor

Group:          Applications/System
License:        GPLv2
URL:            http://www.lesswatts.org/
Source0:	http://www.lesswatts.org/projects/%{name}/download/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gettext
BuildRequires: ncurses-devel

Patch1: powertop-1.7-strncpy.patch

%description
PowerTOP is a tool that finds the software component(s) that make your
computer use more power than necessary while it is idle.

%prep
%setup -q
%patch1 -p1 -b .strncpy

%build
export CFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING README
%{_bindir}/powertop
%{_mandir}/man1/powertop.1*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.11-3.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Adam Jackson <ajax@redhat.com> 1.11-1
- powertop 1.11

* Thu Nov 20 2008 Adam Jackson <ajax@redhat.com>
- Spec only change, fix URL.

* Thu Nov  6 2008 Josh Boyer <jwboyer@gmail.com> - 1.10-1
- Update to latest release
- Drop upstreamed patch

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.9-4
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.9-3
- Autorebuild for GCC 4.3

* Tue Jan 22 2008 Adam Jackson <ajax@redhat.com> 1.9-2
- Use full path when invoking hciconfig. (Ville Skyttä, #426721)

* Mon Dec 10 2007 Josh Boyer <jwboyer@gmail.com> 1.9-1
- Update to latest release

* Mon Aug 20 2007 Josh Boyer <jwboyer@jdub.homelinux.org> 1.8-1
- Update to latest release

* Mon Jul 23 2007 Bill Nottingham <notting@redhat.com> 1.7-4
- add patch to allow dumping output to stdout

* Mon Jul 09 2007 Adam Jackson <ajax@redhat.com> 1.7-3
- powertop-1.7-strncpy.patch: Use strncpy() to avoid stack smash. Patch from
  Till Maas. (#246796)

* Thu Jul 05 2007 Adam Jackson <ajax@redhat.com> 1.7-2
- Don't suggest disabling g-p-m.  Any additional power consumption is more
  than offset by the ability to suspend.

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 1.7-1
- powertop 1.7.

* Mon Jun 11 2007 Adam Jackson <ajax@redhat.com> 1.6-1
- powertop 1.6.

* Tue May 29 2007 Adam Jackson <ajax@redhat.com> 1.5-1
- powertop 1.5.

* Mon May 21 2007 Adam Jackson <ajax@redhat.com> 1.3-1
- powertop 1.3.

* Tue May 15 2007 Adam Jackson <ajax@redhat.com> 1.2-1
- powertop 1.2.  Fixes power reports on machines that report power in Amperes
  instead of Watts.

* Sun May 13 2007 Adam Jackson <ajax@redhat.com> 1.1-1
- powertop 1.1.

* Fri May 11 2007 Adam Jackson <ajax@redhat.com> 1.0-1
- Initial revision.
