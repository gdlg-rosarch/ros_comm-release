Name:           ros-indigo-rosbag-storage
Version:        1.11.21
Release:        0%{?dist}
Summary:        ROS rosbag_storage package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       bzip2-devel
Requires:       console-bridge-devel
Requires:       ros-indigo-cpp-common >= 0.3.17
Requires:       ros-indigo-roscpp-serialization
Requires:       ros-indigo-roscpp-traits >= 0.3.17
Requires:       ros-indigo-roslz4
Requires:       ros-indigo-rostime
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  console-bridge-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cpp-common >= 0.3.17
BuildRequires:  ros-indigo-roscpp-serialization
BuildRequires:  ros-indigo-roscpp-traits >= 0.3.17
BuildRequires:  ros-indigo-roslz4
BuildRequires:  ros-indigo-rostime

%description
This is a set of tools for recording from and playing back ROS message without
relying on the ROS client library.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Mar 06 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.21-0
- Autogenerated by Bloom

* Mon Jun 27 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.20-0
- Autogenerated by Bloom

* Tue Apr 19 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.19-0
- Autogenerated by Bloom

* Thu Mar 17 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.18-0
- Autogenerated by Bloom

* Mon Nov 09 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.16-0
- Autogenerated by Bloom

* Tue Oct 13 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.15-0
- Autogenerated by Bloom

* Sun Sep 20 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.14-0
- Autogenerated by Bloom

* Tue Apr 28 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.13-0
- Autogenerated by Bloom

* Mon Apr 27 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.12-0
- Autogenerated by Bloom

* Thu Apr 16 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.11-0
- Autogenerated by Bloom

* Mon Dec 22 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.10-0
- Autogenerated by Bloom

* Mon Aug 18 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.9-0
- Autogenerated by Bloom

* Mon Aug 04 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.8-0
- Autogenerated by Bloom

