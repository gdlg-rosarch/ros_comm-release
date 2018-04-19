# Script generated with Bloom
pkgdesc="ROS - ROS communications-related packages, including core client libraries (roscpp, rospy) and graph introspection tools (rostopic, rosnode, rosservice, rosparam)."
url='http://www.ros.org/wiki/ros_comm'

pkgname='ros-melodic-ros-comm'
pkgver='1.13.6_3'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-melodic-catkin'
)

depends=('ros-melodic-message-filters'
'ros-melodic-ros'
'ros-melodic-rosbag'
'ros-melodic-rosconsole'
'ros-melodic-roscpp'
'ros-melodic-rosgraph'
'ros-melodic-rosgraph-msgs'
'ros-melodic-roslaunch'
'ros-melodic-roslisp'
'ros-melodic-rosmaster'
'ros-melodic-rosmsg'
'ros-melodic-rosnode'
'ros-melodic-rosout'
'ros-melodic-rosparam'
'ros-melodic-rospy'
'ros-melodic-rosservice'
'ros-melodic-rostest'
'ros-melodic-rostopic'
'ros-melodic-roswtf'
'ros-melodic-std-srvs'
'ros-melodic-topic-tools'
'ros-melodic-xmlrpcpp'
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

