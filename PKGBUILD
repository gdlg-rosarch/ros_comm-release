# Script generated with Bloom
pkgdesc="ROS - ROS communications-related packages, including core client libraries (roscpp, rospy) and graph introspection tools (rostopic, rosnode, rosservice, rosparam)."
url='http://www.ros.org/wiki/ros_comm'

pkgname='ros-kinetic-ros-comm'
pkgver='1.12.13_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-message-filters'
'ros-kinetic-ros'
'ros-kinetic-rosbag'
'ros-kinetic-rosconsole'
'ros-kinetic-roscpp'
'ros-kinetic-rosgraph'
'ros-kinetic-rosgraph-msgs'
'ros-kinetic-roslaunch'
'ros-kinetic-roslisp'
'ros-kinetic-rosmaster'
'ros-kinetic-rosmsg'
'ros-kinetic-rosnode'
'ros-kinetic-rosout'
'ros-kinetic-rosparam'
'ros-kinetic-rospy'
'ros-kinetic-rosservice'
'ros-kinetic-rostest'
'ros-kinetic-rostopic'
'ros-kinetic-roswtf'
'ros-kinetic-std-srvs'
'ros-kinetic-topic-tools'
'ros-kinetic-xmlrpcpp'
)

conflicts=()
replaces=()

_dir=ros_comm
source=()
md5sums=()

prepare() {
    cp -R $startdir/ros_comm $srcdir/ros_comm
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

