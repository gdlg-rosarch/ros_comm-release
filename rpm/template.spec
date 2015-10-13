Name:           ros-jade-ros-comm
Version:        1.11.15
Release:        0%{?dist}
Summary:        ROS ros_comm package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/ros_comm
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-message-filters
Requires:       ros-jade-ros
Requires:       ros-jade-rosbag
Requires:       ros-jade-rosconsole
Requires:       ros-jade-roscpp
Requires:       ros-jade-rosgraph
Requires:       ros-jade-rosgraph-msgs
Requires:       ros-jade-roslaunch
Requires:       ros-jade-roslisp
Requires:       ros-jade-rosmaster
Requires:       ros-jade-rosmsg
Requires:       ros-jade-rosnode
Requires:       ros-jade-rosout
Requires:       ros-jade-rosparam
Requires:       ros-jade-rospy
Requires:       ros-jade-rosservice
Requires:       ros-jade-rostest
Requires:       ros-jade-rostopic
Requires:       ros-jade-roswtf
Requires:       ros-jade-std-srvs
Requires:       ros-jade-topic-tools
Requires:       ros-jade-xmlrpcpp
BuildRequires:  ros-jade-catkin

%description
ROS communications-related packages, including core client libraries (roscpp,
rospy) and graph introspection tools (rostopic, rosnode, rosservice, rosparam).

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

