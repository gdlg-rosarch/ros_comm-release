Name:           ros-jade-roscpp
Version:        1.11.16
Release:        0%{?dist}
Summary:        ROS roscpp package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roscpp
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-cpp-common >= 0.3.17
Requires:       ros-jade-message-runtime
Requires:       ros-jade-rosconsole
Requires:       ros-jade-roscpp-serialization
Requires:       ros-jade-roscpp-traits >= 0.3.17
Requires:       ros-jade-rosgraph-msgs >= 1.10.3
Requires:       ros-jade-rostime
Requires:       ros-jade-std-msgs
Requires:       ros-jade-xmlrpcpp
BuildRequires:  pkgconfig
BuildRequires:  ros-jade-catkin >= 0.5.78
BuildRequires:  ros-jade-cpp-common >= 0.3.17
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-rosconsole
BuildRequires:  ros-jade-roscpp-serialization
BuildRequires:  ros-jade-roscpp-traits >= 0.3.17
BuildRequires:  ros-jade-rosgraph-msgs >= 1.10.3
BuildRequires:  ros-jade-roslang
BuildRequires:  ros-jade-rostime
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-xmlrpcpp

%description
roscpp is a C++ implementation of ROS. It provides a client library that enables
C++ programmers to quickly interface with ROS Topics, Services, and Parameters.
roscpp is the most widely used ROS client library and is designed to be the
high-performance library for ROS.

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

