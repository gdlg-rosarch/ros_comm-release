# Script generated with Bloom
pkgdesc="ROS - ROS communications-related packages, including core client libraries (roscpp, rospy) and graph introspection tools (rostopic, rosnode, rosservice, rosparam)."
url='http://www.ros.org/wiki/ros_comm'

pkgname='ros-lunar-ros-comm'
pkgver='1.13.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
)

depends=('ros-lunar-message-filters'
'ros-lunar-ros'
'ros-lunar-rosbag'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-rosgraph'
'ros-lunar-rosgraph-msgs'
'ros-lunar-roslaunch'
'ros-lunar-roslisp'
'ros-lunar-rosmaster'
'ros-lunar-rosmsg'
'ros-lunar-rosnode'
'ros-lunar-rosout'
'ros-lunar-rosparam'
'ros-lunar-rospy'
'ros-lunar-rosservice'
'ros-lunar-rostest'
'ros-lunar-rostopic'
'ros-lunar-roswtf'
'ros-lunar-std-srvs'
'ros-lunar-topic-tools'
'ros-lunar-xmlrpcpp'
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

