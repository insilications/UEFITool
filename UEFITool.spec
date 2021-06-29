#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : UEFITool
Version  : 21.04.04
Release  : 11
URL      : file:///aot/build/clearlinux/packages/UEFITool/UEFITool-v21.04.04.tar.gz
Source0  : file:///aot/build/clearlinux/packages/UEFITool/UEFITool-v21.04.04.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: UEFITool-bin = %{version}-%{release}
Requires: UEFITool-data = %{version}-%{release}
BuildRequires : binutils-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : bzip2-dev
BuildRequires : bzip2-staticdev
BuildRequires : gcc-dev
BuildRequires : glibc-dev
BuildRequires : glibc-staticdev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libstdc++
BuildRequires : libstdc++-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : mesa-dev
BuildRequires : ncurses-dev
BuildRequires : openssl-dev
BuildRequires : openssl-staticdev
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(Qt5Concurrent)
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5DBus)
BuildRequires : pkgconfig(Qt5Designer)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Help)
BuildRequires : pkgconfig(Qt5Multimedia)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5OpenGL)
BuildRequires : pkgconfig(Qt5PrintSupport)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5QuickControls2)
BuildRequires : pkgconfig(Qt5QuickTest)
BuildRequires : pkgconfig(Qt5QuickWidgets)
BuildRequires : pkgconfig(Qt5Sql)
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(Qt5X11Extras)
BuildRequires : pkgconfig(Qt5Xml)
BuildRequires : pkgconfig(zlib)
BuildRequires : qtbase
BuildRequires : qtbase-dev
BuildRequires : qtsvg
BuildRequires : qtsvg-dev
BuildRequires : qttools-dev
BuildRequires : readline-dev
BuildRequires : sqlite-autoconf-dev
BuildRequires : sqlite-autoconf-lib
BuildRequires : sqlite-autoconf-staticdev
BuildRequires : tcl
BuildRequires : tcl-dev
BuildRequires : tcl-staticdev
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# UEFITool
UEFITool is a viewer and editor of firmware images conforming to UEFI Platform Interface (PI) Specifications.

%package bin
Summary: bin components for the UEFITool package.
Group: Binaries
Requires: UEFITool-data = %{version}-%{release}

%description bin
bin components for the UEFITool package.


%package data
Summary: data components for the UEFITool package.
Group: Data

%description data
data components for the UEFITool package.


%prep
%setup -q -n UEFITool
cd %{_builddir}/UEFITool

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624954866
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-g -Os -march=native -mtune=native -Wall -Wl,--as-needed -fuse-ld=bfd -fPIC -pthread -static-libstdc++ -static-libgcc"
## -fno-tree-vectorize: disable -ftree-vectorize thus disable -ftree-loop-vectorize and -ftree-slp-vectorize
## -funroll-loops maybe dangerous
export CXXFLAGS="-g -Os -march=native -mtune=native -Wall -Wl,--as-needed -fuse-ld=bfd -fPIC -pthread -static-libstdc++ -static-libgcc"
#
export FCFLAGS="-g -Os -march=native -mtune=native -Wall -Wl,--as-needed -fuse-ld=bfd -fPIC -pthread -static-libstdc++ -static-libgcc"
export FFLAGS="-g -Os -march=native -mtune=native -Wall -Wl,--as-needed -fuse-ld=bfd -fPIC -pthread -static-libstdc++ -static-libgcc"
export CFFLAGS="-g -Os -march=native -mtune=native -Wall -Wl,--as-needed -fuse-ld=bfd -fPIC -pthread -static-libstdc++ -static-libgcc"
#
export LDFLAGS="-g -Os -march=native -mtune=native -Wall -Wl,--as-needed -fuse-ld=bfd -fPIC -pthread -static-libstdc++ -static-libgcc -lpthread"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
#
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/dri:/usr/lib64/haswell:/usr/lib64:/usr/lib:/usr/share"
#
export LIBRARY_PATH="$LIBRARY_PATH:/usr/nvidia/lib64:/usr/nvidia/lib64/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/dri:/usr/lib64/haswell:/usr/lib64:/usr/lib:/usr/share"
#
export PATH="$PATH:/usr/local/cuda/bin:/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
#
export CPATH="$CPATH:/usr/local/cuda/include"
#
export DISPLAY=:0
export __GL_ALLOW_UNOFFICIAL_PROTOCOL=1
export __GL_SYNC_TO_VBLANK=0
export __GL_SYNC_DISPLAY_DEVICE=DFP-1
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=DFP-1
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
## altflags1 end
pushd ../UEFITool
qmake uefitool.pro CONFIG+=optimize_size PREFIX=/usr
make -j16 V=1 VERBOSE=1
popd
pushd ../UEFIExtract
cmake -G "Unix Makefiles" -DCMAKE_CXX_FLAGS="-Os" -DCMAKE_C_FLAGS="-Os" -DCMAKE_INSTALL_SBINDIR=%{_sbindir} -DLIB_INSTALL_DIR=%{_libdir} -DLIB_SUFFIX=64 -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ -DCMAKE_INSTALL_LIBDIR=%{_libdir} -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_SBINDIR=%{_sbindir} -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON .
make -j16 V=1 VERBOSE=1
popd
pushd ../UEFIFind
cmake -G "Unix Makefiles" -DCMAKE_CXX_FLAGS="-Os" -DCMAKE_C_FLAGS="-Os" -DCMAKE_INSTALL_SBINDIR=%{_sbindir} -DLIB_INSTALL_DIR=%{_libdir} -DLIB_SUFFIX=64 -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ -DCMAKE_INSTALL_LIBDIR=%{_libdir} -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_SBINDIR=%{_sbindir} -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON .
make -j16 V=1 VERBOSE=1
popd

## make_macro content
echo Done
## make_macro end
## ccache stats
ccache -s || :
## ccache stats
popd

%install
export SOURCE_DATE_EPOCH=1624954866
rm -rf %{buildroot}
## install_macro start
pushd UEFITool
install -dm 0755 %{buildroot}/usr/bin/
install -m 755 -p UEFITool %{buildroot}/usr/bin/
sed -i 's/^Path=.*/Path=\/usr\/bin\/UEFITool/' uefitool.desktop
install -dm 0755 %{buildroot}/usr/share/applications/
install -m 755 -p uefitool.desktop %{buildroot}/usr/share/applications/
popd
pushd UEFIExtract
install -m 755 -p UEFIExtract %{buildroot}/usr/bin/
popd
pushd UEFIFind
install -m 755 -p UEFIFind %{buildroot}/usr/bin/
popd
## install_macro end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/UEFIExtract
/usr/bin/UEFIFind
/usr/bin/UEFITool

%files data
%defattr(-,root,root,-)
/usr/share/applications/uefitool.desktop
