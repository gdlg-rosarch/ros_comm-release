# Script generated with Bloom
pkgdesc="ROS - rosservice contains the rosservice command-line tool for listing and querying ROS <a href="http://www.ros.org/wiki/Services">Services</a>. It also contains a Python library for retrieving information about Services and dynamically invoking them. The Python library is experimental and is for internal-use only."
url='http://ros.org/wiki/rosservice'

pkgname='ros-kinetic-rosservice'
pkgver='1.12.13_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin>=0.5.78'
)

depends=('ros-kinetic-genpy'
'ros-kinetic-rosgraph'
'ros-kinetic-roslib'
'ros-kinetic-rosmsg'
'ros-kinetic-rospy'
)

conflicts=()
replaces=()

_dir=rosservice
source=()
md5sums=()

prepare() {
    cp -R $startdir/rosservice $srcdir/rosservice
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

