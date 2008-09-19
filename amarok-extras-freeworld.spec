Name:           amarok-extras-freeworld
Summary:        Additional functionality for the amaroK media player
Version:        1.4.10
Release:        1%{?dist}

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://amarok.kde.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

Requires:       amarok >= %{version}
Requires:       xine-lib-extras-freeworld
Requires:       libtunepimp-extras-freeworld

# obsolete old livna package
Provides:       amarok-extras-nonfree = %{version}-%{release}
Obsoletes:      amarok-extras-nonfree < 1.4.8-2


%description
This package provides additional functionality for the amaroK media
player.


%prep
mkdir -p $RPM_BUILD_DIR/%{name}-%{version}
cd $RPM_BUILD_DIR/%{name}-%{version}
cat > README << EOF
Now that xine-lib is in Fedora, most additional functionalities are
provided by the libtunepimp-extras-freeworld (mp3 musicbrainz plugin)
and xine-lib-extras-freeworld (mp3 playback) packages.

Thus, this is only a virtual package which depends on 
libtunepimp-extras-freeworld
xine-lib-extras-freeworld
to provide an upgrade path.

You can safely remove this package if you want to.
EOF


%files
%defattr(-,root,root,-)
%doc %{name}-%{version}/README


%changelog
* Fri Sep 19 2008 Rex Dieter <rdieter@fedoraproject.org> 1.4.10-1
- 1.4.10, (re)build for rpmfusion

* Tue Aug 19 2008 Aurelien Bompard <abompard@fedoraproject.org> 1.4.8-3
- set noarch

* Mon Aug 11 2008 Thorsten Leemhuis <fedora [at] leemhuis.info> 1.4.8-2
- rename to amarok-extras-freeworld
- add provides and requires
- adjust other requires for freeworld name

* Thu Apr 03 2008 Rex Dieter <rdieter@fedoraproject.org> 1.4.8-1
- Requires: libtunepimp-extras-nonfree (lvn #1498)

* Tue Oct 31 2006 Aurelien Bompard <abompard@fedoraproject.org> 1.4.4-1
- now that xine-lib is in Fedora Extras, this package is superseeded
  by xine-lib-extras-nonfree. I'm keeping a dummy package because
  there may be extra nonfree plugins for amarok in the future which are
  independent of xine (like mp4 tagging for example)

* Fri Oct 27 2006 Aurelien Bompard <abompard@fedoraproject.org> 1.4.4-1
- version 1.4.4

* Fri Sep 15 2006 Aurelien Bompard <abompard@fedoraproject.org> 1.4.3-1
- version 1.4.3

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 1.4.2-1
- version 1.4.2

* Sun Jul 09 2006 Aurelien Bompard <abompard@fedoraproject.org> 1.4.1-2
- BuildRequires ruby

* Sat Jul 08 2006 Aurelien Bompard <abompard@fedoraproject.org> 1.4.1-1
- version 1.4.1

* Sun May 21 2006 Aurelien Bompard <gauret[AT]free.fr> 1.4.0-1
- version 1.4 final

* Mon Apr 10 2006 Aurelien Bompard <gauret[AT]free.fr> 1.4-0.2.beta3
- beta3
- ship the xine logo (removed from the FE package)

* Sat Apr  1 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4-0.1.beta2
- First build.
