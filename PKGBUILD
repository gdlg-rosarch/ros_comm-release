# Script generated with Bloom
pkgdesc="ROS - This is a set of tools for recording from and playing back to ROS topics. It is intended to be high performance and avoids deserialization and reserialization of the messages."
url='http://ros.org/wiki/rosbag'

pkgname='ros-lunar-rosbag'
pkgver='1.13.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'python2-pillow'
'ros-lunar-catkin>=0.5.78'
'ros-lunar-cpp-common'
'ros-lunar-rosbag-storage'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-roscpp-serialization'
'ros-lunar-std-srvs'
'ros-lunar-topic-tools'
'ros-lunar-xmlrpcpp'
)

depends=('boost'
'python2-rospkg'
'ros-lunar-genmsg'
'ros-lunar-genpy'
'ros-lunar-rosbag-storage'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-roslib'
'ros-lunar-rospy'
'ros-lunar-std-srvs'
'ros-lunar-topic-tools'
'ros-lunar-xmlrpcpp'
)

conflicts=()
replaces=()

_dir=rosbag
source=()
md5sums=()

prepare() {
    cp -R $startdir/rosbag $srcdir/rosbag
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

