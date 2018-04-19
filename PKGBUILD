# Script generated with Bloom
pkgdesc="ROS - This is a set of tools for recording from and playing back to ROS topics. It is intended to be high performance and avoids deserialization and reserialization of the messages."
url='http://ros.org/wiki/rosbag'

pkgname='ros-melodic-rosbag'
pkgver='1.13.6_3'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'python2-pillow'
'ros-melodic-catkin>=0.5.78'
'ros-melodic-cpp-common'
'ros-melodic-rosbag-storage'
'ros-melodic-rosconsole'
'ros-melodic-roscpp'
'ros-melodic-roscpp-serialization'
'ros-melodic-std-srvs'
'ros-melodic-topic-tools'
'ros-melodic-xmlrpcpp'
)

depends=('boost'
'python2-rospkg'
'ros-melodic-genmsg'
'ros-melodic-genpy'
'ros-melodic-rosbag-storage'
'ros-melodic-rosconsole'
'ros-melodic-roscpp'
'ros-melodic-roslib'
'ros-melodic-rospy'
'ros-melodic-std-srvs'
'ros-melodic-topic-tools'
'ros-melodic-xmlrpcpp'
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

