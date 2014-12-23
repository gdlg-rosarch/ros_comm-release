Name:           ros-indigo-rosconsole
Version:        1.11.10
Release:        0%{?dist}
Summary:        ROS rosconsole package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/rosconsole
Source0:        %{name}-%{version}.tar.gz

Requires:       apr-devel
Requires:       apr-util
Requires:       log4cxx-devel
Requires:       ros-indigo-cpp-common
Requires:       ros-indigo-rosbuild
Requires:       ros-indigo-rostime
BuildRequires:  apr-devel
BuildRequires:  apr-util
BuildRequires:  boost-devel
BuildRequires:  log4cxx-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cpp-common
BuildRequires:  ros-indigo-rostime
BuildRequires:  ros-indigo-rosunit

%description
ROS console output library.

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
* Mon Dec 22 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.10-0
- Autogenerated by Bloom

* Mon Aug 18 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.9-0
- Autogenerated by Bloom

* Mon Aug 04 2014 Dirk Thomas <dthomas@osrfoundation.org> - 1.11.8-0
- Autogenerated by Bloom

