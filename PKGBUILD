# Script generated with Bloom
pkgdesc="ROS - roscpp is a C++ implementation of ROS. It provides a <a href="http://www.ros.org/wiki/Client%20Libraries">client library</a> that enables C++ programmers to quickly interface with ROS <a href="http://ros.org/wiki/Topics">Topics</a>, <a href="http://ros.org/wiki/Services">Services</a>, and <a href="http://ros.org/wiki/Parameter Server">Parameters</a>. roscpp is the most widely used ROS client library and is designed to be the high-performance library for ROS."
url='http://ros.org/wiki/roscpp'

pkgname='ros-kinetic-roscpp'
pkgver='1.12.13_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('pkg-config'
'ros-kinetic-catkin>=0.5.78'
'ros-kinetic-cpp-common>=0.3.17'
'ros-kinetic-message-generation'
'ros-kinetic-rosconsole'
'ros-kinetic-roscpp-serialization'
'ros-kinetic-roscpp-traits>=0.3.17'
'ros-kinetic-rosgraph-msgs>=1.10.3'
'ros-kinetic-roslang'
'ros-kinetic-rostime>=0.6.4'
'ros-kinetic-std-msgs'
'ros-kinetic-xmlrpcpp'
)

depends=('ros-kinetic-cpp-common>=0.3.17'
'ros-kinetic-message-runtime'
'ros-kinetic-rosconsole'
'ros-kinetic-roscpp-serialization'
'ros-kinetic-roscpp-traits>=0.3.17'
'ros-kinetic-rosgraph-msgs>=1.10.3'
'ros-kinetic-rostime>=0.6.4'
'ros-kinetic-std-msgs'
'ros-kinetic-xmlrpcpp'
)

conflicts=()
replaces=()

_dir=roscpp
source=()
md5sums=()

prepare() {
    cp -R $startdir/roscpp $srcdir/roscpp
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

