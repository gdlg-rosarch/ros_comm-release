Name:           ros-lunar-topic-tools
Version:        1.13.0
Release:        0%{?dist}
Summary:        ROS topic_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/topic_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-message-runtime
Requires:       ros-lunar-rosconsole
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-rostime
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-xmlrpcpp
BuildRequires:  ros-lunar-catkin >= 0.5.78
BuildRequires:  ros-lunar-cpp-common
BuildRequires:  ros-lunar-message-generation
BuildRequires:  ros-lunar-rosconsole
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-rostest
BuildRequires:  ros-lunar-rostime
BuildRequires:  ros-lunar-rosunit
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-xmlrpcpp

%description
Tools for directing, throttling, selecting, and otherwise messing with ROS
topics at a meta level. None of the programs in this package actually know about
the topics whose streams they are altering; instead, these tools deal with
messages as generic binary blobs. This means they can be applied to any ROS
topic.

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
* Wed Feb 22 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.0-0
- Autogenerated by Bloom

