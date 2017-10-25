Name:           ros-lunar-rosnode
Version:        1.13.3
Release:        0%{?dist}
Summary:        ROS rosnode package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosnode
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-lunar-rosgraph
Requires:       ros-lunar-rostopic
BuildRequires:  ros-lunar-catkin >= 0.5.68
BuildRequires:  ros-lunar-rostest

%description
rosnode is a command-line tool for displaying debug information about ROS Nodes,
including publications, subscriptions and connections. It also contains an
experimental library for retrieving node information. This library is intended
for internal use only.

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
* Wed Oct 25 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.3-0
- Autogenerated by Bloom

* Tue Aug 15 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.2-0
- Autogenerated by Bloom

* Thu Jul 27 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.1-0
- Autogenerated by Bloom

* Wed Feb 22 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.0-0
- Autogenerated by Bloom

