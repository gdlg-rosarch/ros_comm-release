# Script generated with Bloom
pkgdesc="ROS - rospy is a pure Python client library for ROS. The rospy client API enables Python programmers to quickly interface with ROS <a href="http://ros.org/wiki/Topics">Topics</a>, <a href="http://ros.org/wiki/Services">Services</a>, and <a href="http://ros.org/wiki/Parameter Server">Parameters</a>. The design of rospy favors implementation speed (i.e. developer time) over runtime performance so that algorithms can be quickly prototyped and tested within ROS. It is also ideal for non-critical-path code, such as configuration and initialization code. Many of the ROS tools are written in rospy to take advantage of the type introspection capabilities. Many of the ROS tools, such as <a href="http://ros.org/wiki/rostopic">rostopic</a> and <a href="http://ros.org/wiki/rosservice">rosservice</a>, are built on top of rospy."
url='http://ros.org/wiki/rospy'

pkgname='ros-kinetic-rospy'
pkgver='1.12.13_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin>=0.5.78'
)

depends=('python2-numpy'
'python2-rospkg'
'python2-yaml'
'ros-kinetic-genpy'
'ros-kinetic-roscpp'
'ros-kinetic-rosgraph'
'ros-kinetic-rosgraph-msgs>=1.10.3'
'ros-kinetic-roslib'
'ros-kinetic-std-msgs'
)

conflicts=()
replaces=()

_dir=rospy
source=()
md5sums=()

prepare() {
    cp -R $startdir/rospy $srcdir/rospy
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

