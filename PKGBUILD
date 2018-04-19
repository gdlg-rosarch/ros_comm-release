# Script generated with Bloom
pkgdesc="ROS - A package containing the unit tests for rosbag."
url='http://ros.org/wiki/rosbag'

pkgname='ros-melodic-test-rosbag'
pkgver='1.13.6_3'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'bzip2'
'python2-pillow'
'python2-rospkg'
'ros-melodic-catkin>=0.5.68'
'ros-melodic-cpp-common'
'ros-melodic-genmsg'
'ros-melodic-genpy'
'ros-melodic-message-generation'
'ros-melodic-message-runtime'
'ros-melodic-rosbag'
'ros-melodic-rosconsole'
'ros-melodic-roscpp'
'ros-melodic-roscpp-serialization'
'ros-melodic-rosgraph-msgs'
'ros-melodic-roslib'
'ros-melodic-rospy'
'ros-melodic-rostest'
'ros-melodic-rosunit'
'ros-melodic-topic-tools'
'ros-melodic-xmlrpcpp'
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
  [ -f /opt/ros/melodic/setup.bash ] && source /opt/ros/melodic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/melodic \
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

