Name:           ros-indigo-rosbag
Version:        1.11.12
Release:        0%{?dist}
Summary:        ROS rosbag package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosbag
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       python-rospkg
Requires:       ros-indigo-genmsg
Requires:       ros-indigo-genpy
Requires:       ros-indigo-rosbag-storage
Requires:       ros-indigo-rosconsole
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roslib
Requires:       ros-indigo-rospy
Requires:       ros-indigo-topic-tools
Requires:       ros-indigo-xmlrpcpp
BuildRequires:  boost-devel
BuildRequires:  python-pillow
BuildRequires:  python-pillow-qt
BuildRequires:  ros-indigo-catkin >= 0.5.78
BuildRequires:  ros-indigo-cpp-common
BuildRequires:  ros-indigo-rosbag-storage
BuildRequires:  ros-indigo-rosconsole
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roscpp-serialization
BuildRequires:  ros-indigo-topic-tools
BuildRequires:  ros-indigo-xmlrpcpp

%description
This is a set of tools for recording from and playing back to ROS topics. It is
intended to be high performance and avoids deserialization and reserialization
of the messages.

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

