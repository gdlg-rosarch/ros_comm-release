Name:           ros-lunar-roscpp
Version:        1.13.2
Release:        0%{?dist}
Summary:        ROS roscpp package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roscpp
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-cpp-common >= 0.3.17
Requires:       ros-lunar-message-runtime
Requires:       ros-lunar-rosconsole
Requires:       ros-lunar-roscpp-serialization
Requires:       ros-lunar-roscpp-traits >= 0.3.17
Requires:       ros-lunar-rosgraph-msgs >= 1.10.3
Requires:       ros-lunar-rostime >= 0.6.4
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-xmlrpcpp
BuildRequires:  pkgconfig
BuildRequires:  ros-lunar-catkin >= 0.5.78
BuildRequires:  ros-lunar-cpp-common >= 0.3.17
BuildRequires:  ros-lunar-message-generation
BuildRequires:  ros-lunar-rosconsole
BuildRequires:  ros-lunar-roscpp-serialization
BuildRequires:  ros-lunar-roscpp-traits >= 0.3.17
BuildRequires:  ros-lunar-rosgraph-msgs >= 1.10.3
BuildRequires:  ros-lunar-roslang
BuildRequires:  ros-lunar-rostime >= 0.6.4
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-xmlrpcpp

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
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Tue Aug 15 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.2-0
- Autogenerated by Bloom

* Thu Jul 27 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.1-0
- Autogenerated by Bloom

* Wed Feb 22 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.0-0
- Autogenerated by Bloom

