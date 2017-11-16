Name:           ros-kinetic-rosservice
Version:        1.12.12
Release:        0%{?dist}
Summary:        ROS rosservice package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosservice
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-genpy
Requires:       ros-kinetic-rosgraph
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-rosmsg
Requires:       ros-kinetic-rospy
BuildRequires:  ros-kinetic-catkin >= 0.5.78

%description
rosservice contains the rosservice command-line tool for listing and querying
ROS Services. It also contains a Python library for retrieving information about
Services and dynamically invoking them. The Python library is experimental and
is for internal-use only.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Nov 16 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.12-0
- Autogenerated by Bloom

* Tue Nov 07 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.11-0
- Autogenerated by Bloom

* Mon Nov 06 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.10-0
- Autogenerated by Bloom

* Mon Nov 06 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.9-0
- Autogenerated by Bloom

* Mon Nov 06 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.8-0
- Autogenerated by Bloom

* Fri Feb 17 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.7-0
- Autogenerated by Bloom

* Wed Oct 26 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.6-0
- Autogenerated by Bloom

* Fri Sep 30 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.5-0
- Autogenerated by Bloom

* Mon Sep 19 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.4-0
- Autogenerated by Bloom

* Fri Jun 03 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.2-0
- Autogenerated by Bloom

* Fri Mar 18 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.12.0-0
- Autogenerated by Bloom

* Fri Mar 11 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.17-0
- Autogenerated by Bloom

