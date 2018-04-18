# Script generated with Bloom
pkgdesc="ROS - A set of message filters which take in messages and may output those messages at a later time, based on the conditions that filter needs met."
url='http://ros.org/wiki/message_filters'

pkgname='ros-lunar-message-filters'
pkgver='1.13.6_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('boost'
'ros-lunar-catkin>=0.5.68'
'ros-lunar-rosconsole'
'ros-lunar-roscpp'
'ros-lunar-rostest'
'ros-lunar-rosunit'
)

depends=('ros-lunar-rosconsole'
'ros-lunar-roscpp'
)

conflicts=()
replaces=()

_dir=message_filters
source=()
md5sums=()

prepare() {
    cp -R $startdir/message_filters $srcdir/message_filters
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

