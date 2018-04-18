# Script generated with Bloom
pkgdesc="ROS - A package containing the unit tests for rosbag."
url='http://ros.org/wiki/rosbag'

pkgname='ros-lunar-test-rosbag'
pkgver='1.13.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'bzip2'
'python2-pillow'
'python2-rospkg'
'ros-lunar-catkin>=0.5.68'
'ros-lunar-cpp-common'
'ros-lunar-genmsg'
'ros-lunar-genpy'
'ros-lunar-message-generation'
'ros-lunar-message-runtime'
'ros-lunar-rosbag'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-roscpp-serialization'
'ros-lunar-rosgraph-msgs'
'ros-lunar-roslib'
'ros-lunar-rospy'
'ros-lunar-rostest'
'ros-lunar-rosunit'
'ros-lunar-topic-tools'
'ros-lunar-xmlrpcpp'
)

depends=()

conflicts=()
replaces=()

_dir=test_rosbag
source=()
md5sums=()

prepare() {
    cp -R $startdir/test_rosbag $srcdir/test_rosbag
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
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

