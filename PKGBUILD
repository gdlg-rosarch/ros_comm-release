# Script generated with Bloom
pkgdesc="ROS - This is a set of tools for recording from and playing back to ROS topics. It is intended to be high performance and avoids deserialization and reserialization of the messages."
url='http://ros.org/wiki/rosbag'

pkgname='ros-kinetic-rosbag'
pkgver='1.12.13_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'python2-pillow'
'ros-kinetic-catkin>=0.5.78'
'ros-kinetic-cpp-common'
'ros-kinetic-rosbag-storage'
'ros-kinetic-rosconsole'
'ros-kinetic-roscpp'
'ros-kinetic-roscpp-serialization'
'ros-kinetic-std-srvs'
'ros-kinetic-topic-tools'
'ros-kinetic-xmlrpcpp'
)

depends=('boost'
'python2-rospkg'
'ros-kinetic-genmsg'
'ros-kinetic-genpy'
'ros-kinetic-rosbag-storage'
'ros-kinetic-rosconsole'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'ros-kinetic-rospy'
'ros-kinetic-std-srvs'
'ros-kinetic-topic-tools'
'ros-kinetic-xmlrpcpp'
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

