Name:           ros-indigo-roscpp
Version:        1.11.14
Release:        0%{?dist}
Summary:        ROS roscpp package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roscpp
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cpp-common >= 0.3.17
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-rosconsole
Requires:       ros-indigo-roscpp-serialization
Requires:       ros-indigo-roscpp-traits >= 0.3.17
Requires:       ros-indigo-rosgraph-msgs >= 1.10.3
Requires:       ros-indigo-rostime
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-xmlrpcpp
BuildRequires:  pkgconfig
BuildRequires:  ros-indigo-catkin >= 0.5.78
BuildRequires:  ros-indigo-cpp-common >= 0.3.17
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-rosconsole
BuildRequires:  ros-indigo-roscpp-serialization
BuildRequires:  ros-indigo-roscpp-traits >= 0.3.17
BuildRequires:  ros-indigo-rosgraph-msgs >= 1.10.3
BuildRequires:  ros-indigo-roslang
BuildRequires:  ros-indigo-rostime
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-xmlrpcpp

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

