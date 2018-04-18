# Script generated with Bloom
pkgdesc="ROS - Integration test suite based on roslaunch that is compatible with xUnit frameworks."
url='http://ros.org/wiki/rostest'

pkgname='ros-kinetic-rostest'
pkgver='1.12.13_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'ros-kinetic-catkin>=0.7.9'
'ros-kinetic-rosunit'
)

depends=('boost'
'ros-kinetic-rosgraph'
'ros-kinetic-roslaunch'
'ros-kinetic-rosmaster'
'ros-kinetic-rospy'
'ros-kinetic-rosunit'
)

conflicts=()
replaces=()

_dir=rostest
source=()
md5sums=()

prepare() {
    cp -R $startdir/rostest $srcdir/rostest
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

