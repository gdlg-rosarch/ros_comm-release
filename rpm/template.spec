Name:           ros-jade-rospy
Version:        1.11.20
Release:        0%{?dist}
Summary:        ROS rospy package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rospy
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       PyYAML
Requires:       numpy
Requires:       python-rospkg
Requires:       ros-jade-genpy
Requires:       ros-jade-roscpp
Requires:       ros-jade-rosgraph
Requires:       ros-jade-rosgraph-msgs >= 1.10.3
Requires:       ros-jade-roslib
Requires:       ros-jade-std-msgs
BuildRequires:  ros-jade-catkin >= 0.5.78

%description
rospy is a pure Python client library for ROS. The rospy client API enables
Python programmers to quickly interface with ROS Topics, Services, and
Parameters. The design of rospy favors implementation speed (i.e. developer
time) over runtime performance so that algorithms can be quickly prototyped and
tested within ROS. It is also ideal for non-critical-path code, such as
configuration and initialization code. Many of the ROS tools are written in
rospy to take advantage of the type introspection capabilities. Many of the ROS
tools, such as rostopic and rosservice, are built on top of rospy.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
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

* Sat Sep 19 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.14-0
- Autogenerated by Bloom

* Tue Apr 28 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.13-0
- Autogenerated by Bloom

* Mon Apr 27 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.12-0
- Autogenerated by Bloom

* Thu Apr 16 2015 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.11-0
- Autogenerated by Bloom

* Fri Dec 26 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.10-0
- Autogenerated by Bloom

