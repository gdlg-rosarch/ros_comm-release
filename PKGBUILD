# Script generated with Bloom
pkgdesc="ROS - rostopic contains the rostopic command-line tool for displaying debug information about ROS <a href="http://www.ros.org/wiki/Topics">Topics</a>, including publishers, subscribers, publishing rate, and ROS <a href="http://www.ros.org/wiki/Messages">Messages</a>. It also contains an experimental Python library for getting information about and interacting with topics dynamically. This library is for internal-use only as the code API may change, though it does provide examples of how to implement dynamic subscription and publication behaviors in ROS."
url='http://ros.org/wiki/rostopic'

pkgname='ros-melodic-rostopic'
pkgver='1.13.6_3'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-melodic-catkin>=0.5.78'
'ros-melodic-rostest'
)

depends=('ros-melodic-genpy>=0.5.4'
'ros-melodic-rosbag'
'ros-melodic-rospy'
)

conflicts=()
replaces=()

_dir=rostopic
source=()
md5sums=()

prepare() {
    cp -R $startdir/rostopic $srcdir/rostopic
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

