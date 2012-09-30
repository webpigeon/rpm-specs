Name:		pidgin-opensteamworks
Version:	1.0
Release:	1%{?dist}
Summary:	A pidgin plugin for talking to the messenger for Steam.

#Group:		
License:	GPLv3
URL:		https://code.google.com/p/pidgin-opensteamworks

# The source for this package was pulled from opensteamworks' vcs. Use the
# following commands to generate the tarball
#    svn checkout http://pidgin-opensteamworks.googlecode.com/svn/trunk/ pidgin-opensteamworks-1.0
#    wget https://raw.github.com/gist/3806494/8b4b1d2aeaa7e1343bdc3478bf911505c7d225d9/makefile -O pidgin-opensteamworks-1.0/steam-mobile/makefile
#    tar -cJvf pidgin-opensteamworks-20120930.tar.xz pidgin-opensteamworks-1.0
Source0:	pidgin-opensteamworks-20120930.tar.xz

BuildRequires:	libpurple-devel json-glib-devel glib2-devel
Requires:	telepathy-haze

%description


%prep
%setup -q


%build
cd %_builddir/pidgin-opensteamworks-1.0/steam-mobile/
make %{?_smp_mflags}


%install
cd %_builddir/pidgin-opensteamworks-1.0/steam-mobile/
make install DESTDIR=%{buildroot}


%files
%doc
%{_libdir}/purple-2/libsteam.so


%changelog

