Name:		obs-studio	
Version:	master
Release:	1%{?dist}
Summary:	Software for broadcasting to twitch and recording.

Group:		Applications/Multimedia
License:	GPLv2
URL:		https://obsproject.com
Source0:	https://github.com/jp9000/obs-studio/archive/master.zip

BuildRequires:  cmake gcc-c++ qt5-qtbase-devel qt5-qtx11extras-devel ffmpeg-compat-devel ffmpeg-devel jansson-devel libXinerama-devel  libXinerama libv4l-devel x264-devel libXcomposite-devel libgudev1-devel freetype-devel fontconfig-devel pulseaudio-libs-devel v4l-utils qt5-qtmultimedia-devel faac faac-devel gstreamer-plugins-bad gstreamer-plugins-ugly gstreamer-ffmpeg libtool	
Requires:	qt5 pulseaudio vlc

%description


%prep
%setup -q

%build
mkdir build && cd build
cmake -DUNIX_STRUCTURE=1 -DCMAKE_INSTALL_PREFIX=/usr ..
make %{?_smp_mflags}


%install
cd build
make install DESTDIR=%{buildroot}

%files
/usr/bin/obs
/usr/include/obs
/usr/lib/cmake/LibObs
/usr/lib/obs-plugins
/usr/lib/libobs-opengl.so
/usr/lib/libobs.so
/usr/lib/libobs.so.0
/usr/lib/libobsglad.so
/usr/lib/libobsglad.so.0
/usr/share/obs
/usr/share/applications/obs.desktop
/usr/share/icons/hicolor/256x256/apps/obs.png
%doc



%changelog

